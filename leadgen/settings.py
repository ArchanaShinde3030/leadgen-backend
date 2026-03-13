
# # ORS_ALLOW_ALL_ORIGINS = True
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# # SECURITY
# SECRET_KEY = 'django-insecure-change-this-key'
# DEBUG = True
# ALLOWED_HOSTS = ['*']


# # Applications
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'corsheaders',
#     'rest_framework',
#     'leads',
# ]


# # Middleware
# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]



# ROOT_URLCONF = 'leadgen.urls'


# # Templates
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]


# ROOT_URLCONF = 'leadgen.urls'
# WSGI_APPLICATION = 'leadgen.wsgi.application'



# import os

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('DB_NAME', 'lead_db6'),       # environment variable DB_NAME
#         'USER': os.environ.get('DB_USER', 'root'),          # environment variable DB_USER
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'root'),  # environment variable DB_PASSWORD
#         'HOST': os.environ.get('DB_HOST', 'localhost'),     # environment variable DB_HOST
#         'PORT': os.environ.get('DB_PORT', '3306'),          # environment variable DB_PORT
#     }
# }
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.mysql',
# #         'NAME': 'lead_db6',
# #         'USER': 'root',
# #         'PASSWORD': 'root',
# #         'HOST': 'localhost',
# #         'PORT': '3306',
# #     }
# # }
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.mysql',
# #         'NAME': 'archanaShinde$lead_db6', 
# #         'USER': 'archanaShinde',
# #         'PASSWORD': 'root',
# #         'HOST': 'archanaShinde.mysql.pythonanywhere-services.com',
# #         'PORT': '3306',
# #     }
# # }


# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
# ]


# # Language & Time
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True


# # Static files
# BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC_URL = '/static/'

# # Optional for dev: tell Django where to find extra static files
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# # Optional for production: collect all static files here
# STATIC_ROOT = BASE_DIR / "staticfiles"


# # CORS (IMPORTANT for Nuxt frontend)
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True


# # Celery (optional, as you had)
# CELERY_BROKER_URL = 'redis://127.0.0.1:6381/0'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6381/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'


# # Default primary key
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "INFO",
#     },
# }
# CORS_ALLOW_ALL_ORIGINS = True

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'archanakb4u@gmail.com'
# EMAIL_HOST_PASSWORD = 'zetpblvqefmvwzli'

from pathlib import Path
import os

# Base
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-change-this-key'
DEBUG = True
ALLOWED_HOSTS = ['*']  # Hugging Face space साठी '*'

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'leads',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'leadgen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'leadgen.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'lead_db6'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'root'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),  # Hugging Face वर cloud MySQL वापरा
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

# Language & Time
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Celery (optional: Hugging Face free space मध्ये Redis local नाही)
# CELERY_BROKER_URL = 'redis://127.0.0.1:6381/0'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6381/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

# Email (optional)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER', 'archanakb4u@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'your-email-password')