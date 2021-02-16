import csv
from prettytable import PrettyTable
import os
from utils.DB_funcs import *
import pymysql
from dotenv import load_dotenv
from utils.drinks_funcs import *
from utils.couriers_funcs import *

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
            cursor = connection.cursor()
            drinks_add(connection)
            cursor.close()
            connection.commit()
            print_table_drinks(connection)
        elif drinks_option == "3":
            header()
            cursor = connection.cursor()
            drinks_update(connection)
            cursor.close()
            connection.commit()
            print_table_drinks(connection)
        elif drinks_option == "4":
            header()
            cursor = connection.cursor()
            drinks_delete(connection)
            cursor.close()
            connection.commit()
            print_table_drinks(connection)

        drinks_option = input(
            f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}   \n0.) Exit "
        )


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


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
            cursor = connection.cursor()
            cour_add(connection)
            cursor.close()
            connection.commit()
            print_table_couriers(connection)
        elif courier_option == "3":
            header()
            cursor = connection.cursor()
            cour_update(connection)
            cursor.close()
            connection.commit()
            print_table_couriers(connection)
        elif courier_option == "4":
            header()
            cursor = connection.cursor()
            cour_delete(connection)
            cursor.close()
            connection.commit()
            print_table_couriers(connection)

        courier_option = input(
            f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}   \n0.) Exit "
        )


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


def print_table_order(item_list):
    x = PrettyTable()
    x.field_names = [
        "Id",
        "Name",
        "Address",
        "Phone",
        "Courier",
        "Prodcut(s)",
        "Status",
    ]
    for items in item_list:
        x.add_row(
            (
                items["Id"],
                items["Name"],
                items["Address"],
                items["Phone"],
                items["Courier"],
                items["Products"],
                items["Status"],
            )
        )
    print(x)


def order_menu(item, list):
    print_table_order(list)

    order_option = input(
        f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}    \n0.) Exit "
    )
    header()
    while order_option != "0":
        if order_option == "1":
            header()
            print_table_order(list)
        elif order_option == "2":
            header()
            idx = input("Id: ")
            name = input("Name: ")
            add = input("Address: ")
            p_num = input("Phone Number: ")
            prod = input("Id of Product: ")
            cour = input("Id of Courier: ")
            stat = input("Current Status: ")

            order_dict = {
                "Id": idx,
                "Name": name,
                "Address": add,
                "Phone": p_num,
                "Courier": cour,
                "Products": prod,
                "Status": stat,
            }

            list.append(order_dict)
            print_table_order(list)
        elif order_option == "3":
            header()
            update_ord = input(
                "What is the Id of the order you would like to update?: "
            )
            new_status = input("New Status of order: ")
            current_order = False
            for order in list:
                if order["Id"] == update_ord:
                    order["Current_Status"] = new_status
                    print_table_order(list)
                    current_order = True
            if current_order == False:
                print("Sorry! Not a current order.")

                return order
        elif order_option == "4":
            header()
            del_ord = input("What is the Id of the order you would like to delete?: ")
            current_order = False
            for order in list:
                if order["Id"] == del_ord:
                    list.remove(order)
                    print_table_order(list)
                    current_order = True
            if current_order == False:
                print("Sorry! Not a current order.")

        order_option = input(
            f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}   \n0.) Exit "
        )


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def rate_sys():
    rate = input(
        "Thankyou for your order. Would you mind leaving a review for us today? "
    )

    rate_y = ["Yes", "yes", "y", "Y"]
    rate_n = ["No", "no", "n", "N"]
    rate_stars = [1, 2, 3, 4, 5]

    if rate in rate_y:
        rate_stars_y = int(
            input("Thankyou! How many stars out of 5 would you give our service? ")
        )
        print("Thanks, we'll take that onboard. Until next time!")
    elif rate in rate_n:
        print("Ok no problem. Until next time!")
    else:
        print("Sorry, invalid selection. Please try again.")
    return rate
