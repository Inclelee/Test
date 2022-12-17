"""
Django settings for HelloWorld project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 绝对地址
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 加密盐
SECRET_KEY = 'django-insecure-rdq4b&go8-!6nl4$pwmj2p7bajfe#w*2c52g%61bgmowcj7_t-'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
DEBUG = True

# 允许ip访问
#                  [] 仅允许localhost访问
#               ['*'] 允许所有人访问
#   ['192.168.8.204'] 允许指定ip访问
ALLOWED_HOSTS = ['*']


# Application definition
# 应用管理
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 中间件管理
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',         # 127.0.0.1拒绝我们的连接请求 问题注释该行
]

# 指定了当前目录的根url，是Django的路由入口
ROOT_URLCONF = 'HelloWorld.urls'

# 模板读取配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],                  # 修改模板读取位置
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

# 项目部署时，Django 的内置服务器将使用的 WSGI 应用程序对象的完整 Python 路径
WSGI_APPLICATION = 'HelloWorld.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# 数据库配置信息
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'HOST': '49.235.204.77',
        'PORT': 4580,
        'USER': 'tester',
        'PASSWORD': 'Dr6getstqghsfDxcmQ'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# 密码验证器
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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# 语言配置项     英文：en-us (Default) | 中文：zh-Hans
LANGUAGE_CODE = 'zh-Hans'
# 服务端时区配置项      世界时区：UTC (Default) | 中国时区：Asia/Shanghai
TIME_ZONE = 'Asia/Shanghai'
# 国际化服务
USE_I18N = True
# 本地化服务
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# 静态资源的存放位置，静态资源包括 CSS、JS、Images
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 测试代码
if __name__ == '__main__':
    print(BASE_DIR)
