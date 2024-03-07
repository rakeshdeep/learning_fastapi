from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
pymysql.install_as_MySQLdb()

# this will only just connect you to your demo db


MYSQL_DB_URL = "mysql://root:@localhost/fastapidb"

Engine  = create_engine(MYSQL_DB_URL)
sessionLocal = sessionmaker(autocommit= False, bind= Engine)
Base = declarative_base()

