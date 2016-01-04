"""
Local Django Settings File

INSTRUCTIONS
SAVE A COPY OF THIS FILE IN THIS DIRECTORY WITH THE NAME local_settings.py
MAKE YOUR LOCAL SETTINGS CHANGES IN THAT FILE AND DO NOT CHECK IT IN
CHANGES TO THIS FILE SHOULD BE TO ADD/REMOVE SETTINGS THAT NEED TO BE
MADE LOCALLY BY ALL INSTALLATIONS

local_settings.py, once created, should never be checked into source control
It is ignored by default by .gitignore, so if you don't mess with that, you should be fine.
"""
# pylint: disable=R0801, W0611
import os
import socket

# Set the root path of the project so it's not hard coded
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Explicitly Define test runner to silence 1_6.W001 Warning
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DEBUG = True

# List of Admin users to be emailed by error system
MANAGERS = ()
ADMINS = MANAGERS

# Domain Name to Prepend to MEDIA URL, used in feeds
MEDIA_DOMAIN = ""

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
if MEDIA_DOMAIN != "":
    MEDIA_URL = "http://{0}/media/".format(MEDIA_DOMAIN)  # this maps inside of a static_urls URL in gondor.yml
else:
    MEDIA_URL = "/media/"  # make sure this maps inside of a static_urls URL in gondor.yml

# Absolute path to the directory that holds media.
# Note that as of Django 1.3 - media is for uploaded files only.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'mediaroot')

# Staticfiles Config
THE_THEME = "pb2-jq"
STATIC_ROOT = PROJECT_ROOT + "/staticroot/"
ACCEL_REDIRECT = False
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, "themes", THE_THEME, "static"), ]
LOCALIZED_COVER_PLACEHOLDER = STATIC_URL + "images/cover-placeholder.jpg"
USE_COVER_PLACEHOLDERS_ONLY = False

# URL to Use for Feeds
FEED_URL = ""  # This will be overridden in prod conf with an alt protocol/domain

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, "themes", 'pb2-jq', 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'podiobooks.core.context_processors.current_site',
                'django.template.context_processors.debug',
                'podiobooks.core.context_processors.feed_settings',
                'podiobooks.core.context_processors.js_api_keys',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
            ],
            'debug': DEBUG,
        },
    }
]

MIDDLEWARE_CLASSES = (
    'podiobooks.core.middleware.StripAnalyticsCookies',
    'django.middleware.gzip.GZipMiddleware',  # Not running SSL, so gzip doesn't matter
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'x_robots_tag_middleware.middleware.XRobotsTagMiddleware',
#    'podiobooks.feeds.middleware.ga_tracking.GATracker',
    'podiobooks.feeds.middleware.redirect_exception.RedirectException',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'podiobooks.core.middleware.PermanentRedirectMiddleware',
)

ROOT_URLCONF = 'podiobooks.urls'

INSTALLED_APPS = (
    'adminactions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django_jenkins',
    'mub',
    'noodles',
    'podiobooks',
    'podiobooks.ads',
    'podiobooks.core',
    'podiobooks.libsyn',
    'podiobooks.feeds',
    'podiobooks.search',
    'podiobooks.ratings',
)

WSGI_APPLICATION = 'podiobooks.wsgi.application'

### DATABASE SETTINGS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'pb2.db'),
        'USER': 'pb2',
        'PASSWORD': '',
        #        'HOST': '127.0.0.1',
        #        'PORT': '', # Set to empty string for default.
        #        'SUPPORTS_TRANSACTIONS': 'true',
    }
}
FIXTURE_DIRS = {os.path.join(PROJECT_ROOT, "..", "..", "podiobooks_data")}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Cache Settings
CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    # },
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

# Celery Setup
BROKER_URL = 'memory'
CELERY_ALWAYS_EAGER = True  # Force immediate running of async tasks on dev

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Denver'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zv$+w7juz@(g!^53o0ai1u082)=jkz9my_r=3)fglrj5t8l$2#'

# Set a default timeout for external URL grabs, such as for the comments and for Google Analytics from Feeds
socket.setdefaulttimeout(2)  # 2 second timeout for grabbing feed

### DEBUG TOOLBAR
if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = ('127.0.0.1',)
    INSTALLED_APPS += ('debug_toolbar',)

##### Custom Variables Below Here #######

# Google Analytics ID
GOOGLE_ANALYTICS_ID = "UA-5071400-1"

# Facebook Application ID
FACEBOOK_APP_ID = "155134080235"

# <meta name="descripton"> default value
BASE_META_DESCRIPTION = "Free audio books delivered as podcasts. Subscribe for free to any book and start from chapter one. Podiobooks.com"

### TIPJAR
TIPJAR_BUSINESS_NAME = 'evo@podiobooks.com'

### MUB
MUB_CSS_ORDER = (
    ("jquery.pbshelf.css", "clear.css", "styles.css", "base-shelf.css"),
    ("ads.css", "gsc-overrides.css", "adaptive.css", "small-screen.css")
)
MUB_MINIFY = False

# This is to catch special domain names and redirect them to the main
REDIRECT_DOMAINS = []

# static feed caching
FEED_CACHE_ENDPOINT = ''
FEED_CACHE_TOKEN = ''  # generated by endpoint service
FEED_CACHE_SECRET = ''  # generated by endpoint service

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

X_ROBOTS_TAG = ['noindex', 'nofollow']

try:
    from podiobooks.settings_local import *
except ImportError:
    pass
