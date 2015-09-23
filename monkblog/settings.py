import os
from local_settings import DATABASE_URI
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
CONNECTION_POOL_RECYCLE = 4
