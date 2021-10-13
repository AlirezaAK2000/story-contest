from pathlib import Path
import os
from decouple import config

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config('DEBUG' , cast=bool)

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'users',
    'crispy_forms',
    'ibm',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'first.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'first.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media')
MEDIA_URL = '/media/'


# IBM text to speech
IBM_TEXT_TO_SPEECH_API_KEY = config("IBM_TEXT_TO_SPEECH_API_KEY")
IBM_TEXT_TO_SPEECH_URL = config("IBM_TEXT_TO_SPEECH_URL")
READER_VOICE = config("READER_VOICE")

# IBM NLU
IBM_NLU_API_KEY = config("IBM_NLU_API_KEY")
IBM_NLU_URL = config("IBM_NLU_URL")

# ARVAN
ARVAN_STORAGE_ENDPOINT_URL = config("ARVAN_STORAGE_ENDPOINT_URL")
ARVAN_STORAGE_ACCESS_KEY_ID = config("ARVAN_STORAGE_ACCESS_KEY_ID")
ARVAN_STORAGE_SECRET_ACCESS_KEY = config("ARVAN_STORAGE_SECRET_ACCESS_KEY")
ARVAN_STORAGE_BUCKET_NAME = config("ARVAN_STORAGE_BUCKET_NAME")
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_ACCESS_KEY_ID = config("ARVAN_STORAGE_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = config("ARVAN_STORAGE_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("ARVAN_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = config("ARVAN_STORAGE_ENDPOINT_URL")
AWS_DEFAULT_ACL = 'public-read'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'stmp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
