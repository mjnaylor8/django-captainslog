"""
Django settings for captains_log project production.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool('DEBUG', default=False)
DEBUG = False

ALLOWED_HOSTS = ["captainslog.thenaylors.co.uk",]

INSTALLED_APPS += [

]

MIDDLEWARE += []

INTERNAL_IPS = [
    # ...
    # '192.168.1.250',
    # ...
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 1
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True