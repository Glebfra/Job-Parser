import peewee

db = peewee.MySQLDatabase('db', host='localhost', user='root', password='root')


class Appliements(peewee.Model):
    name = peewee.CharField(255)
    url = peewee.CharField(1024)

    class Meta:
        database = db
