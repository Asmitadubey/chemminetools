#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid
uuid._uuid_generate_random = None

import os
from django.contrib.messages import constants as messages



# load celery
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = {'pickle'}
#CELERY_BROKER_URL= "amqp://guest@localhost//"
CELERY_BROKER_URL = "amqp://remote_worker:askfj4l3nbb43@localhost//"
CELERY_RESULT_BACKEND="cache+memcached://127.0.0.1:11211/"
#CELERY_TASK_ACKS_LATE = True
#CELERY_WORKER_PREFETCH_MULTIPLIER = 1

gettext = lambda s: s

PROJECT_DIR = '/srv/chemminetools'

DEBUG = True
#TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS= ['example.com', 'localhost', '127.0.0.1']

ADMINS = ()

    # ('Your Name', 'your_email@domain.com'),

MANAGERS = ADMINS

LANGUAGES = [('en', 'English'),('en-us', 'English')]
DEFAULT_LANGUAGE = 0

DATABASES = {'default': {  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                           # Or path to database file if using sqlite3.
                           # Not used with sqlite3.
                           # Not used with sqlite3.
                           # Set to empty string for localhost. Not used with sqlite3.
                           # Set to empty string for default. Not used with sqlite3.
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'chemminetools',
    'USER': 'chemminetools',
    'PASSWORD': 'chemminetools',
    'HOST': 'localhost',
    'PORT': '',
    }}

CACHES = \
    {'default': {
        #'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
     'LOCATION': '127.0.0.1:11211'}}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.

TIME_ZONE = 'America/Los_Angeles'
DATETIME_FORMAT = '%b %d, %Y, %H:%M:%S'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.

USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale

USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"

STATIC_ROOT = PROJECT_DIR + '/static_production'
MEDIA_ROOT = PROJECT_DIR + '/working'

STATICFILES_DIRS = (PROJECT_DIR + '/static', )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

MEDIA_URL = '/working/'

STATIC_URL = '/static/'




# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
# A new key should be generated for you if you use the bootstrap script.
# If necessary, re-generate with:
# $ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.

#TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
                    #'django.template.loaders.app_directories.Loader')

MIDDLEWARE = (
    'middleware.http_headers.ForceHttpHeadersMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'guest.middleware.LogGuests',
    )

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.request',
#    'django.core.context_processors.media',
#    'django.core.context_processors.static',
#    'django.contrib.messages.context_processors.messages',
#    'cms.context_processors.media',
#    'sekizai.context_processors.sekizai',
#    )

#TEMPLATE_DIRS = (PROJECT_DIR + '/templates', )

CMS_TEMPLATES = (('template_1.html', 'Template One'), )

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
#    'APP_DIRS': True,
    'DIRS': (PROJECT_DIR + '/templates', ),
    'OPTIONS': {
        'debug': DEBUG,
        'context_processors':
            (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.template.context_processors.csrf',
            'django.template.context_processors.request',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',
            'cms.context_processors.cms_settings',
            #'cms.context_processors.media',
            ),
        'loaders': ('django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader'),
    },
},
]


ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'accounts',
    'userena',
    'guardian',
    'easy_thumbnails',
    'cms',
    'menus',
    'mptt',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_picture',
    'djangocms_link',
    'djangocms_file',
    'djangocms_googlemap',
    'sekizai',
    'bootstrap_toolkit',
    'bootstrap4',
    'guest',
    'compounddb',
    'myCompounds',
    'sdftools',
    'tools',
    'similarity',
    'ChemmineR',
    'structure_search',
    'pubchem_rest_interface',
    'django_cron',
    'filer',
    'targetsearch',
    'lockdown',
    )

CRON_CLASSES= [
        'guest.cron.DeleteOldGuests',
        'tools.cron.deleteOrphans',
        'tools.cron.deleteOldJobs',
        'tools.cron.deleteOldUsers',
        'ChemmineR.cron.deleteOldChemmineR',
        ]

WORK_DIR = PROJECT_DIR + '/working'


TOOLS_RESULTS = PROJECT_DIR + '/working'

BOOTSTRAP_BASE_URL = ADMIN_MEDIA_PREFIX + 'bootstrap/'
BOOTSTRAP_CSS_BASE_URL = BOOTSTRAP_BASE_URL + 'css/'
BOOTSTRAP_CSS_URL = BOOTSTRAP_CSS_BASE_URL + 'bootstrap.css'
BOOTSTRAP_JS_BASE_URL = BOOTSTRAP_BASE_URL + 'js/'

# setup twitter boostrap message tags

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-error',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-error',
    messages.ERROR: 'alert-error',
    }

# Django-guests options
# Override the default settings for cleaning up guests.

import datetime

# How long a guest user must have been inactive to get deleted.

GUEST_DELETE_TIME = datetime.timedelta(hours=72)

# How often we check guest users and delete old ones (in seconds).

GUEST_DELETE_FREQUENCY = 8640

# search tool options

ASSEI_SERVER = ('127.0.0.1', 50008)
QUERY_TIMEOUT = 60

# Script no longer exists. Variable nowhere to be found.
#PUBCHEM_DOWNLOADER = '/srv/chemminetools/eis/pubchemdl.py'

# hard limits

MAX_COMPOUND_LIMIT = 10000  # compounds allowed per upload
MAX_SDF_LENGTH = 10000  # lines per SDF allowed

# user auth settings
#deprecated ANONYMOUS_USER_ID = -1
ANONYMOUS_USER_NAME = 'AnonymousUser'
USERENA_DEFAULT_PRIVACY = 'closed'
USERENA_WITHOUT_USERNAMES = True 
USERENA_REDIRECT_ON_SIGNOUT = "/"
AUTH_PROFILE_MODULE = 'accounts.MyProfile'
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
USERENA_MUGSHOT_GRAVATAR = False
USERENA_DISABLE_PROFILE_LIST = True
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST='smtp.gmail.com'
#EMAIL_PORT=587
#EMAIL_HOST_USER=''
#EMAIL_HOST_PASSWORD=''
#EMAIL_USE_TLS=True
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

LOCKDOWN_PASSWORDS=('lockdown')

# ChEMBL database settings
CHEMBL_DB = {
    'DBHOST' : 'localhost',
    'DBNAME' : 'chembl',
    'DBUSER' : 'chemminetools',
    'DBPASS' : 'chemminetools',
}

# Uncomment these to allow usage of ChemmineTools in IFrames.
# Understand the security implications before doing so.
#CSRF_COOKIE_SAMESITE = None
#SESSION_COOKIE_SAMESITE = None
