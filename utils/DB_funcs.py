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

def execute_sql_select(connection, comment):
    cursor = connection.cursor()
    cursor.execute(comment)
    cursor.close()
    return cursor.fetchall()

def db_do(connection):
    cursor = connection.cursor()
    cursor.execute()
    cursor.close()
    connection.commit()


def check_id_in_db(cursor):

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


def import_ord_db(connection):

    cursor = connection.cursor()

    cursor.execute("SELECT order_id, name, address, phone, courier, status FROM orders")

    rows = cursor.fetchall()

    cursor.close()

    return rows


def orders_to_list_of_lists() :
    '''
    A simple function which will read all orders in my order table, turn each order into a list,
    then add each order to another list
    '''
    
    rows = %sql select * from Orders #reads in all data in the table
    list_of_orders = [] #creates a blank list to write too, will hold every order list
    
    for order in rows : #loop over every row returned by the sql command in line 7
        
        single_order_list = [] #create another blank list that will hold data for an individual order
        
        for i in range(0,8) : #loop over a single row. Each row contains 9 bits of data to be pulled out
            
            single_order_list.append(order[i]) #Append data for a particual order to it's list
            
        list_of_orders.append(single_order_list) #Append order data to list of lists
            
    return list_of_orders