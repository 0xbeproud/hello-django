from .base import *

print(BASE_DIR)
PHASE = 'local'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
SECRET_KEY = 'l5P$*lZ;sA>v.l2Z68gaD`zTH=&jmcrJ,,PE=q`%%(hvR-WM=K'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format': "%(asctime)s,%(msecs)d %(levelname)-6s [%(filename)s:%(lineno)d] - %(message)s",
        }
    },
    'loggers': {
        'api': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'users': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

CELERY_BROKER_URL = 'amqp://admin:admin123@localhost:5672/'
CELERY_RESULT_BACKEND = 'amqp://admin:admin123@localhost:5672/'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_PERSISTENT = 'json'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'test',
#         'USER': 'test',
#         'PASSWORD': 'test123',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'ATOMIC_REQUESTS': True,
#     }
# }
