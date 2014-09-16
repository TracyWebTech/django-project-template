
from .base import *

ALLOWED_HOSTS = (
    #... Please set me!!
)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Tracy SysAdmin', 'sysadmin@tracy.com.br'),
)
MANAGERS = ADMINS


SECRET_KEY = get_env_setting('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': get_env_setting('DB_HOST'),
        'NAME': os.getenv('DB_NAME', '{{ project_name }}'),
        'USER': os.getenv('DB_USER', '{{ project_name }}'),
        'PASSWORD': get_env_setting('DB_PASSWORD'),
    }
}

RAVEN_CONFIG = {
    'dsn': get_env_setting('SENTRY_DSN'),
}

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = get_env_setting('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_setting('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

