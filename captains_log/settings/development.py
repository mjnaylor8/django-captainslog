
"""
Django settings for captains_log project development.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool('DEBUG', default=False)
DEBUG = True

ALLOWED_HOSTS = ["192.168.1.250",
]

INSTALLED_APPS += [
  'leaflet',
  'rosetta',
  'debug_toolbar',
]


MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = [
    # ...
    '192.168.1.250',
    # ...
]

LEAFLET_CONFIG = {
    # conf here
    #'SPATIAL_EXTENT': (5.0, 44.0, 7.5, 46),
    'DEFAULT_ZOOM': 16,
    'DEFAULT_CENTER': (51.182250, -0.827610),
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'DEFAULT_PRECISION': 6,
    #'TILES': [],
    #'OVERLAYS': [],
    #'ATTRIBUTION_PREFIX': 'Powered by django-leaflet',
    'SCALE': 'both',
    'MINIMAP': True,
    #'PLUGINS': [],
}
