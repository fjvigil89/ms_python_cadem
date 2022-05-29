from app import app
from flaskext.mysql import MySQL
from os import environ

mysql = MySQL()


class Settings(object):
    db_host: str = environ.get("DB_HOST")
    db_port: str = environ.get("DB_PORT")
    db_name: str = environ.get("DB_NAME")
    db_user: str = environ.get("DB_USER")
    db_pass: str = environ.get("DB_PASS")


def get_settings():
    return Settings()


settings = get_settings()
# print('HOST: ', environ.get("DB_HOST"))

app.config['MYSQL_DATABASE_HOST'] = settings.db_host
# app.config['MYSQL_DATABASE_PORT'] = settings.db_port
app.config['MYSQL_DATABASE_DB'] = settings.db_name
app.config['MYSQL_DATABASE_USER'] = settings.db_user
app.config['MYSQL_DATABASE_PASSWORD'] = settings.db_pass

mysql.init_app(app)
