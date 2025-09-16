import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente, se necessário
load_dotenv()

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = 'django-insecure-duka-seguradora-2025-development-key'
DEBUG = True  # Você pode usar os.getenv("DEBUG", "False") == "True" se quiser usar .env
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://dukaseguros.com', 'https://www.dukaseguros.com']

# Aplicativos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Bibliotecas de terceiros
    "crispy_forms",
    "crispy_bootstrap5",
    'django_bootstrap5',
    'django_filters',
    'widget_tweaks',

    # Apps locais
    'core',
    'accounts.apps.AccountsConfig',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ⚠️ já está aqui na posição correta
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principal
ROOT_URLCONF = 'duka_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# WSGI
WSGI_APPLICATION = 'duka_project.wsgi.application'

# ✅ BANCO DE DADOS (Corrigido)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dukaseguros_db_jrq5',
        'USER': 'admin',
        'PASSWORD': 'pZlPYGloETfx3aTbKYwsxuibjfwbZUmq',
        'HOST': 'dpg-d2n0p6ggjchc73d708c0-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos e mídia
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Campo padrão de ID
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# Login e Logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'login'

# E-mail (console e SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tempunus@gmail.com'
EMAIL_HOST_PASSWORD = 'qltt vmds mhbk llcm'
DEFAULT_FROM_EMAIL = 'Duka Seguros <tempunus@gmail.com>'
