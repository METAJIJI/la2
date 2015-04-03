"""
Django settings for la2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*%vx!6ipro9^cuig&@pw$^0=2+ekeeia_(mj@svnnzl2jt!9xm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (

    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django_comments',


    'mptt',
    'zinnia_bootstrap',
    'sorl.thumbnail',
    'tagging',
    'zinnia',

    'zinnia_markitup',
    'register',
    'check',


)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'la2.urls'

WSGI_APPLICATION = 'la2.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)

TEMPLATE_LOADERS = [
    'app_namespace.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader',
]

ZINNIA_ENTRY_CONTENT_TEMPLATES = [
    ('zinnia/_short_entry_detail.html', 'Short entry template'),
]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'la2_db',
        'USER': 'skver',
        'PASSWORD': '1989',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        },
    # 'server': {
    #     'NAME': 'server_db',
    #     'ENGINE': 'django.db.backends.mysql',
    #     'USER': 'skver',
    #     'PASSWORD': '1989'
    # }
    'server': {
        'NAME': 'vl2p-ls',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'vl2p',
        'PASSWORD': 'MEhYrf6en69YJ5Uh',
        'HOST': 'azure1.metajiji.tk',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
STATIC_URL = '/static/'
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Kiev'
SITE_ID = 1
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_JS_DIR = os.path.join(STATIC_ROOT, "js")
TINYMCE_JS_ROOT = os.path.join(STATIC_JS_DIR, "tiny_mce")

MEDIA_URL = '/media/'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


DATABASE_ROUTERS = ['register.router.RegisterRouter']
