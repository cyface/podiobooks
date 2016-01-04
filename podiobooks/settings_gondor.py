"""GONDOR.IO specific settings"""

# pylint: disable=W0614,W0401,W0123

import os
import urlparse

from .settings import *

DEBUG = eval(os.environ.get("DEBUG", "False"))
TEMPLATE_DEBUG = DEBUG

ACCEL_REDIRECT = True

if "GONDOR_DATABASE_URL" in os.environ:
    urlparse.uses_netloc.append("postgres")
    DB_URL = urlparse.urlparse(os.environ["GONDOR_DATABASE_URL"])
    DATABASES = {
        "default": {
            "ENGINE": 'django.db.backends.postgresql_psycopg2',
            "NAME": DB_URL.path[1:],
            "USER": DB_URL.username,
            "PASSWORD": DB_URL.password,
            "HOST": DB_URL.hostname,
            "PORT": DB_URL.port
        }
    }

if "GONDOR_REDIS_URL" in os.environ:
    urlparse.uses_netloc.append("redis")
    DB_URL = urlparse.urlparse(os.environ["GONDOR_REDIS_URL"])
    GONDOR_REDIS_HOST = DB_URL.hostname
    GONDOR_REDIS_PORT = DB_URL.port
    GONDOR_REDIS_PASSWORD = DB_URL.password

    BROKER_URL = "redis://:%s@%s:%s/0" % (GONDOR_REDIS_PASSWORD, GONDOR_REDIS_HOST, GONDOR_REDIS_PORT)
    CELERY_ALWAYS_EAGER = False
    CELERY_REDIS_DB = 0

    CACHE_MIDDLEWARE_SECONDS = int(os.environ.get("CACHE_MIDDLEWARE_SECONDS", 5200))

    # Cache Settings
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.cache.RedisCache',
            'LOCATION': GONDOR_REDIS_HOST + ":" + str(GONDOR_REDIS_PORT) + ":" + "0",
            'OPTIONS': {
                'PASSWORD': GONDOR_REDIS_PASSWORD,
                'DB': 1,
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

if "GONDOR_DATA_DIR" in os.environ:
    GONDOR_DATA_DIR = os.environ["GONDOR_DATA_DIR"]
    FIXTURE_DIRS = (GONDOR_DATA_DIR,)

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
ALLOWED_HOSTS = ['.podiobooks.com', 'il086.gondor.co', 'lt832.gondor.co', 'sf602.gondor.co', 'jk134.gondor.co']
REDIRECT_DOMAINS = ['il086.gondor.co', 'lt832.gondor.co', 'sf602.gondor.co', 'jk134.gondor.co']

GOOGLE_ANALYTICS_ID = os.environ.get("GOOGLE_ANALYTICS_ID", GOOGLE_ANALYTICS_ID)

SECRET_KEY = os.environ.get("SECRET_KEY", 'zv$+w7juz@(g!^53o0ai1u082)=jkz9my_r=3)fglrj5t8l$2#')

DATA_DIR = os.environ["GONDOR_DATA_DIR"]

FEED_CACHE_ENDPOINT = str(os.environ.get("FEED_CACHE_ENDPOINT", ""))
FEED_CACHE_TOKEN = str(os.environ.get("FEED_CACHE_TOKEN", ""))  # generated by endpoint service
FEED_CACHE_SECRET = str(os.environ.get("FEED_CACHE_SECRET", ""))  # generated by endpoint service

INSTALLED_APPS += ()

MEDIA_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "mediaroot", )
STATIC_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "staticroot") + "/"

MEDIA_DOMAIN = os.environ.get("MEDIA_DOMAIN", "")
if MEDIA_DOMAIN != "":
    MEDIA_URL = "http://{0}/assets/media/".format(MEDIA_DOMAIN)  # this maps inside of a static_urls URL in gondor.yml
else:
    MEDIA_URL = "/assets/media/"  # make sure this maps inside of a static_urls URL in gondor.yml

STATIC_URL = "/assets/static/"  # make sure this maps inside of a static_urls URL in gondor.yml

# URL to use for Feeds
FEED_DOMAIN = os.environ.get("FEED_DOMAIN", "")
if FEED_DOMAIN != "":
    FEED_URL = "http://{0}".format(FEED_DOMAIN)
else:
    FEED_URL = ""

FILE_UPLOAD_PERMISSIONS = 0640

MUB_MINIFY = True

if os.environ.get("INSTANCE_TYPE", "") == 'production':
    X_ROBOTS_TAG = ['index', 'follow']
else:
    X_ROBOTS_TAG = ['noindex', 'nofollow']

# ## DEBUG TOOLBAR
# ## Replicated Here to Enable Picking Up Environment Setting from Gondor
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
