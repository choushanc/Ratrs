from playhouse.pool import PooledPostgresqlExtDatabase
from data.conf.PsqlConf import psqlconf
database = PooledPostgresqlExtDatabase('jan', host=psqlconf.host, port=psqlconf.port, user=psqlconf.user, password=psqlconf.password)
database.connect()