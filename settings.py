import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
MYSQL_USER = os.environ.get('MYSQL_USER', None)
MYSQL_PASS = os.environ.get('MYSQL_PASS', None)
DATABASE_URI = "mysql+pymysql://{user}:{password}@monkpit.mysql.pythonanywhere-services.com/monkpit$mysite".format(user=MYSQL_USER, password=MYSQL_PASS)

