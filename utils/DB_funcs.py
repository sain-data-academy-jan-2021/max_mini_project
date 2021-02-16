import pymysql
import os
from dotenv import load_dotenv


def db_connect():

    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    return pymysql.connect(host, user, password, database)

def check_name_in_db(cursor):

    rows = cursor.fetchall()
    if len(rows) != 0:
        print("Done!")
        return True
    else:
        print("Invalid Selection. Try Again.")
        return False



def import_prod_db(connection):

    cursor = connection.cursor()

    cursor.execute("SELECT product_id, drink, type, price, status FROM products")

    rows = cursor.fetchall()

    cursor.close()

    return rows


def import_cour_db(connection):

    cursor = connection.cursor()

    cursor.execute("SELECT courier_id, name, age, vehicle, status FROM couriers")

    rows = cursor.fetchall()

    cursor.close()

    return rows

