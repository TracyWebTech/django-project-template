from .base import *


SECRET_KEY = 'NOT A SECRET'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '{{ project_name }}',
    }
}


# Set template debug true
for template in TEMPLATES:
    template['OPTIONS']['debug'] = True


# django-devserver: http://github.com/dcramer/django-devserver
try:
    import devserver
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'devserver',
    )
    MIDDLEWARE_CLASSES += (
        'devserver.middleware.DevServerMiddleware',
    )


# django-debug-toolbar
#   https://github.com/django-debug-toolbar/django-debug-toolbar
try:
    import debug_toolbar
except ImportError:
    pass
else:
    INTERNAL_IPS = ('127.0.0.1', )
    INSTALLED_APPS += (
        'debug_toolbar.apps.DebugToolbarConfig',
    )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
    #    'INTERCEPT_REDIRECTS': False
    }
