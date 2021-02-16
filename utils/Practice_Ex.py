import csv
from prettytable import PrettyTable
import os
from utils.DB_funcs import import_prod_db
from utils.DB_funcs import import_cour_db

menu_select = ""
acceptable_values = [0, 1, 2, 3]


def header():
    os.system("clear")
    print("+---------------------------------+")
    print("|         Mad Max's Cafe          +")
    print("+---------------------------------+")


def main_menu():

    try:
        selection = int(
            input(
                """1.) Product Menu    \n2.) Courier List    \n3.) Order Screen    \n0.) Exit. """
            )
        )
        if selection not in acceptable_values:
            print("Invalid number. Please try again. ")
        return selection
    except ValueError as err:
        print(err)


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def print_table_drinks(connection):
    data_list = import_prod_db(connection)
    x = PrettyTable()
    x.field_names = ["Id", "Drink", "Type", "Price", "Status"]
    for items in data_list:
        x.add_row(
            (
                items[0],
                items[1],
                items[2],
                items[3],
                items[4],
            )
        )
    print(x)


def drinks_menu(item, list, connection):
    print_table_drinks(connection)

    drinks_option = input(
        f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}    \n0.) Exit "
    )
    header()
    while drinks_option != "0":
        if drinks_option == "1":
            header()
            print_table_drinks(connection)
        elif drinks_option == "2":
            header()
            name = input("Prodcut Name: ")
            ptype = input("Product Type: ")
            price = float(input("Product Price: "))
            status = input("Product Status: ")
            cursor = connection.cursor()
            cursor.execute(f'insert into products (drink, type, price, status) VALUES ("{name}", "{ptype}", {price}, "{status}")')
            cursor.close()
            connection.commit()
            print_table_drinks(connection)
        elif drinks_option == "3":
            header()
            cursor = connection.cursor()
            valid_drink = False
            
            while not valid_drink:
                update_prod = input("Name of product you would like to update?: ")
                new_price = float(input("New Price: "))
                cursor.execute(f'SELECT * from products WHERE drink = "{update_prod}"')
                rows = cursor.fetchall()
                if len(rows) != 0:
                    valid_drink = True
                    print("Done!")
                else:
                    print("Invalid Selection. Try Again.")

            cursor.execute(f'UPDATE products price SET price = "{new_price}" WHERE drink = "{update_prod}"')
            cursor.close()
            connection.commit()
            print_table_drinks(connection)
        elif drinks_option == "4":
            header()
            cursor = connection.cursor()
            valid_drink = False

            while not valid_drink:
                del_prod = input("Name of product you would like to delete: ")
                cursor.execute(f'SELECT * from products WHERE drink = "{del_prod}"')
                rows = cursor.fetchall()
                if len(rows) != 0:
                    valid_drink = True
                    print("Done!")
                else:
                    print("Invalid Selection. Try Again.")

            cursor.execute(f'DELETE FROM products WHERE drink = "{del_prod}"')
            cursor.close()
            connection.commit()
            print_table_drinks(connection)

        drinks_option = input(
            f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}   \n0.) Exit ")




def print_table_couriers(connection):
    data_list = import_cour_db(connection)
    x = PrettyTable()
    x.field_names = ["Id", "Name", "Age", "Vehicle", "Status"]
    for items in data_list:
        x.add_row(
            (
                items[0],
                items[1],
                items[2],
                items[3],
                items[4],
            )
        )
    print(x)


def courier_menu(item, list, connection):
    print_table_couriers(connection)

    courier_option = input(
        f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}    \n0.) Exit "
    )
    header()
    while courier_option != "0":
        if courier_option == "1":
            header()
            print_table_couriers(connection)
        elif courier_option == "2":
            header()
            name = input("Courier Name: ")
            age = input("Courier Age: ")
            vehic = float(input("Vehicle: "))
            status = input("Courier Status: ")
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO couriers (name, age, vehicle, status) VALUES ("{name}", "{age}", {vehic}, "{status}")')
            cursor.close()
            connection.commit()
            print_table_couriers(connection)
        elif courier_option == "3":
            header()
            cursor = connection.cursor()
            valid_courier = False
            
            while not valid_courier:
                update_cour = input("Name of courier you would like to update?: ")
                new_stat = input("New Status: "))
                cursor.execute(f'SELECT * from couriers WHERE name = "{update_cour}"')
                rows = cursor.fetchall()
                if len(rows) != 0:
                    valid_courier = True
                    print("Done!")
                else:
                    print("Invalid Selection. Try Again.")

            cursor.execute(f'UPDATE couriers status SET status = "{new_stat}" WHERE name = "{update_cour}"')
            cursor.close()
            connection.commit()
            print_table_couriers(connection)
        elif courier_option == "4":
            header()
            cursor = connection.cursor()
            valid_courier = False

            while not valid_courier:
                del_cour = input("Name of courier you would like to delete: ")
                cursor.execute(f'SELECT * from products WHERE name = "{del_cour}"')
                rows = cursor.fetchall()
                if len(rows) != 0:
                    valid_courier = True
                    print("Done!")
                else:
                    print("Invalid Selection. Try Again.")

            cursor.execute(f'DELETE FROM couriers WHERE name = "{del_cour}"')
            cursor.close()
            connection.commit()
            print_table_couriers(connection)

        courier_option = input(
            f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}   \n0.) Exit ")

