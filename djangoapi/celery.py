from __future__ import absolute_import

import os
from datetime import timedelta

from celery import Celery

# Django의 세팅 모듈을 Celery의 기본으로 사용하도록 등록합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoapi.settings.local')

app = Celery('djangoapi')

# v3.1 일 경우
# app.config_from_object('django.conf:settings')
# v4.0 이상 일 경우
app.config_from_object('django.conf:settings', namespace='CELERY')

# v3.1 일 경우
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# v4.0 이상 일 경우
app.autodiscover_tasks()
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Asia/Seoul',
    CELERY_ENABLE_UTC=False,
    CELERYBEAT_SCHEDULE={
        'say_hello-every-seconds': {
            "task": "App.tasks.CheckSite",
            'schedule': timedelta(seconds=30),
            'args': ()
        },
    }
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
