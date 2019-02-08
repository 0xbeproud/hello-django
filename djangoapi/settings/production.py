from djangoapi.settings.base import *

ALLOWED_HOSTS = ['django']
DEBUG = False
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 10

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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weproud',
        'USER': 'weproud',
        'PASSWORD': 'weproud123',
        'HOST': '192.168.65.2',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
    }
}
