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

def cour_update(connection):

    cursor = connection.cursor()

    valid_courier = False

    while not valid_courier:
        update_cour = input("Name of courier you would like to update?: ")
        new_stat = input("New Status: ")
        cursor.execute(f'SELECT * from couriers WHERE name = "{update_cour}"')
        valid_courier = check_name_in_db(cursor)

    cursor.execute(
        f'UPDATE couriers status SET status = "{new_stat}" WHERE name = "{update_cour}"'
        )
    cursor.close()

def cour_delete(connection):

    cursor = connection.cursor()
    valid_courier = False

    while not valid_courier:
        del_cour = input("Name of courier you would like to delete: ")
        cursor.execute(f'SELECT * from couriers WHERE name = "{del_cour}"')
        valid_courier = check_name_in_db(cursor)

    cursor.execute(f'DELETE FROM couriers WHERE name = "{del_cour}"')
    cursor.close()

def cour_add(connection):

    cursor = connection.cursor()
    name = input("Courier Name: ")
    age = float(input("Courier Age: "))
    vehic = input("Vehicle: ")
    status = input("Courier Status: ")
    cursor.execute(
        f'INSERT INTO couriers (name, age, vehicle, status) VALUES ("{name}", "{age}", "{vehic}", "{status}")'
    )
    cursor.close()