import mysql.connector
from mysql.connector import errorcode
from config.loadconfig import Db
from logger import get_logger

def connect():
    try:
        global cnx
        global cursor
        cnx = mysql.connector.connect(**Db.config)
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Database Error! Something is wrong with user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("Database Error! Database does not exist")
        else:
            logger.error(err)

def close():
    try:
        cnx.close()
        cursor.close()
    except NameError:
        logger.error('Database Error! No connection to close')
