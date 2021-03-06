"""Webfaction specific settings"""

# pylint: disable=W0614,W0401,W0123

import os

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ACCEL_REDIRECT = True


DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": "podiobooks_staging",
        "USER": "podiobooks",
        "PASSWORD": "podiobooks",
        "HOST": "127.0.0.1",
        "PORT": "5432"
    }
}

CACHE_MIDDLEWARE_SECONDS = int(os.environ.get("CACHE_MIDDLEWARE_SECONDS", 5200))

# Cache Settings
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': "127.0.0.1:18391:2",
        'OPTIONS': {
            'DB': 2,
        },
    },
}

MIDDLEWARE_CLASSES = (
    'podiobooks.core.middleware.StripAnalyticsCookies',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'x_robots_tag_middleware.middleware.XRobotsTagMiddleware',
    'podiobooks.feeds.middleware.redirect_exception.RedirectException',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'podiobooks.core.middleware.PermanentRedirectMiddleware',
)

EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "")
MANAGERS = eval(os.environ.get("MANAGERS", "(('Podiobooks DEV', 'podiobooksdev@gmail.com'),)"))
ADMINS = eval(os.environ.get("ADMINS", "(('Podiobooks DEV', 'podiobooksdev@gmail.com'),)"))
SEND_BROKEN_LINK_EMAILS = eval(os.environ.get("SEND_BROKEN_LINK_EMAILS", "False"))
ALLOWED_HOSTS = ['.podiobooks.com', 'pbdev.webfaction.com', 'wf-45-33-126-67.webfaction.com', '.reblender.com']
REDIRECT_DOMAINS = ['wf-45-33-126-67.webfaction.com', 'pbdev.webfaction.com']

GOOGLE_ANALYTICS_ID = os.environ.get("GOOGLE_ANALYTICS_ID", GOOGLE_ANALYTICS_ID)

SECRET_KEY = os.environ.get("SECRET_KEY", 'zv$+w7juz@(g!^53o0ai1u082)=jkz9my_r=3)fglrj5t8l$2#')

INSTALLED_APPS += ()

MEDIA_ROOT = "/home/pbdev/webapps/podiobooks_staging_media"
STATIC_ROOT = "/home/pbdev/webapps/podiobooks_staging_static"

MEDIA_DOMAIN = os.environ.get("MEDIA_DOMAIN", "")
if MEDIA_DOMAIN != "":
    MEDIA_URL = "http://{0}/assets/media/".format(MEDIA_DOMAIN)
else:
    MEDIA_URL = "/assets/media/"

STATIC_URL = "/assets/static/"

# URL to use for Feeds
FEED_DOMAIN = os.environ.get("FEED_DOMAIN", "")
if FEED_DOMAIN != "":
    FEED_URL = "http://{0}".format(FEED_DOMAIN)
else:
    FEED_URL = ""

FILE_UPLOAD_PERMISSIONS = 0o0640

MUB_MINIFY = True

X_ROBOTS_TAG = ['noindex', 'nofollow']

# ## DEBUG TOOLBAR
# ## Replicated Here to Enable Picking Up Environment Setting
if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
    }
    DEBUG_TOOLBAR_PATCH_SETTINGS = False  # Trying to get around gunicorn startup error

LOGGING = {
    'version': 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        "root": {
            "handlers": ["console"],
            'propagate': True,
            "level": "INFO",
        },
        'gunicorn': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

try:
    from podiobooks.settings_local import *
except ImportError:
    pass