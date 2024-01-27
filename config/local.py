from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 현재 호스트(IP)가 유동 IP라서 AWS 재시동시 수정해야 함.
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += ['debug_toolbar',] 
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]