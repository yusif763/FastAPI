import os
import peewee


os.environ.get('API_KEY', '_taAIpgDRpSi5eHWhSB6AQ')


DATABASE_NAME = os.environ.get('DATABASE_NAME','test_db')
password = os.environ.get("DATABASE_PASSWORD",'123')
port = os.environ.get("PORT",3306)
PROD = os.environ.get("PROD")

db = peewee.MySQLDatabase(DATABASE_NAME, **{"charset":"utf8","sql_mode":"PIPES_AS_CONCAT","user":'root', "password":password,
                        "host":'db',"port":3306,"use_unicode":True})


