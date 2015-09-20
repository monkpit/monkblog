import os
from secrets import MYSQL_USER, MYSQL_PASS
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
DATABASE_URI = "mysql+pymysql://{user}:{password}@monkpit.mysql.pythonanywhere-services.com/monkpit$blog".format(user=MYSQL_USER, password=MYSQL_PASS)

