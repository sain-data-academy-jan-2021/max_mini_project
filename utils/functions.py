import csv
from prettytable import PrettyTable
import os

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


def print_table_drinks(item_list):
    x = PrettyTable()
    x.field_names = ["Index", "Drink", "Type", "Price", "Status"]
    for items in item_list:
        x.add_row(
            (
                items["Index"],
                items["Drink"],
                items["Type"],
                items["Price"],
                items["Status"],
            )
        )
    print(x)


def drinks_menu(item, list):
    print_table_drinks(list)

    drinks_option = input(
        f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}    \n0.) Exit "
    )
    header()
    while drinks_option != "0":
        if drinks_option == "1":
            header()
            print_table_drinks(list)
        elif drinks_option == "2":
            header()
            idx = input("Number in list: ")
            prod = input("Name of drink: ")
            hca = input("Hot, Cold or Alcoholic: ")
            price = input("Price of drink: ")
            avail = input("Availble or Out Of Stock: ")
            drinks_dict = {
                "Index": idx,
                "Drink": prod,
                "Type": hca,
                "Price": price,
                "Status": avail,
            }

            list.append(drinks_dict)
            print_table_drinks(list)
        elif drinks_option == "3":
            header()
            update_prod = input(
                "What is the Name of the Product you would like to update?: "
            )
            new_status = input("New Status of Product: ")
            current_drinks = False
            for drinks in list:
                if drinks["Drink"] == update_prod:
                    drinks["Status"] = new_status
                    print_table_drinks(list)
                    current_drinks = True
            if current_drinks == False:
                print("Sorry! Not a current drink.")

                return drinks
        elif drinks_option == "4":
            header()
            del_name = input(
                "What is the Name of the drink you would like to delete?: "
            )
            current_drinks = False
            for drinks in list:
                if drinks["Drink"] == del_name:
                    list.remove(drinks)
                    print_table_drinks(list)
                    current_drinks = True
            if current_drinks == False:
                print("Sorry! Not a current courier.")

        drinks_option = input(
            f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}   \n0.) Exit "
        )


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def print_table_courier(item_list):
    x = PrettyTable()
    x.field_names = ["Index", "Name", "Age", "Vehicle", "Status"]
    for items in item_list:
        x.add_row(
            (
                items["Index"],
                items["Name"],
                items["Age"],
                items["Vehicle"],
                items["Status"],
            )
        )
    print(x)


def courier_menu(item, list):
    print_table_courier(list)

    courier_option = input(
        f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}    \n0.) Exit "
    )
    header()
    while courier_option != "0":
        if courier_option == "1":
            header()
            print_table_courier(list)
        elif courier_option == "2":
            header()
            idx = input("Number in list: ")
            name = input("First Name: ")
            age = input("Age: ")
            vehicle = input("Car or Bike: ")
            status = input("Free or Busy: ")

            courier_dict = {
                "Index": idx,
                "Name": name,
                "Age": age,
                "Vehicle": vehicle,
                "Status": status,
            }

            list.append(courier_dict)
            print_table_courier(list)
        elif courier_option == "3":
            header()
            update_name = input(
                "What is the Name of the Courier you would like to update?: "
            )
            new_status = input("New Status of Courier: ")
            current_courier = False
            for courier in list:
                if courier["Name"] == update_name:
                    courier["Status"] = new_status
                    print_table_courier(list)
                    current_courier = True
            if current_courier == False:
                print("Sorry! Not a current courier.")

                return courier
        elif courier_option == "4":
            header()
            del_name = input(
                "What is the First Name of the courier you would like to delete?: "
            )
            current_courier = False
            for courier in list:
                if courier["Name"] == del_name:
                    list.remove(courier)
                    print_table_courier(list)
                    current_courier = True
            if current_courier == False:
                print("Sorry! Not a current courier.")

        courier_option = input(
            f"1.) Print {item}  \n2.) Add A {item}    \n3.) Update A {item}  \n4.) Delete A {item}   \n0.) Exit "
        )


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


def print_table_order(item_list):
    x = PrettyTable()
    x.field_names = ["Index","Name","Address","Phone","Courier","Prodcut(s)","Status"]
    for items in item_list:
        x.add_row(
            (
                items["Index"],
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
            idx = input("Index: ")
            name = input("Name: ")
            add = input("Address: ")
            p_num = input("Phone Number: ")
            prod = input("Index of Product: ")
            cour = input("Index of Courier: ")
            stat = input("Current Status: ")

            order_dict = {
                "Index": idx,
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
                "What is the Index of the order you would like to update?: "
            )
            new_status = input("New Status of order: ")
            current_order = False
            for order in list:
                if order["Index"] == update_ord:
                    order["Current_Status"] = new_status
                    print_table_order(list)
                    current_order = True
            if current_order == False:
                print("Sorry! Not a current order.")

                return order
        elif order_option == "4":
            header()
            del_ord = input(
                "What is the Index of the order you would like to delete?: "
            )
            current_order = False
            for order in list:
                if order["Index"] == del_ord:
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


def read_from_csv(filename, list):

    with open(filename, "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            list.append(row)


def write_to_csv(filename, list, fieldnames):

    with open(filename, "w") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in list:
            writer.writerow(row)


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
