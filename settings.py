import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
MYSQL_USER = os.environ.get('blog_mysql_user', None)
MYSQL_PASS = os.environ.get('blog_mysql_pass', None)
DATABASE_URI = "mysql+pymysql://{user}:{pass}@monkpit.mysql.pythonanywhere-services.com/monkpit$mysite".format(
        {'user': MYSQL_USER, 'pass': MYSQL_PASS})

