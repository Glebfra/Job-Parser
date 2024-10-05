import os

import peewee

db = os.getenv('DATABASE_DB')
db_host = os.getenv('DATABASE_HOST')
db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')
db = peewee.MySQLDatabase(db, host=db_host, user=db_user, password=db_password)


class Appliements(peewee.Model):
    name = peewee.CharField(255)
    url = peewee.CharField(1024)

    class Meta:
        database = db
