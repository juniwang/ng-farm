# MYSQL_HOST = "jbw-1.cpmvfibm3vjp.ap-southeast-1.rds.amazonaws.com"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "redatom"
MYSQL_PWD = "redatom"
MYSQL_DB = "redatom"

Config = {
    "mysql": {
        "connection": 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    }
}
