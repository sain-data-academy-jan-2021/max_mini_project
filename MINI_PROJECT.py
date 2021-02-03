import os

os.system("clear")
import utils.functions as functions
import login
import csv

menu_select = ""
acceptable_values = [0, 1, 2, 3]

while menu_select not in acceptable_values:
    menu_select = functions.main_menu()
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
while menu_select != "0":
    if menu_select == 1:

        drinks = []

        functions.read_from_csv("data/drinks_list.csv", drinks)

        functions.drinks_menu("Drinks ", drinks)

        fieldnames = [
            "Index",
            "Drink",
            "Hot_Cold",
            "Price",
            "Status",
        ]

        functions.write_to_csv("data/drinks_list.csv", drinks, fieldnames)

        menu_select = functions.main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 2:

        couriers = []

        functions.read_from_csv("data/courier_list.csv", couriers)

        functions.courier_menu("Courier ", couriers)

        fieldnames = [
            "Index",
            "Name",
            "Age",
            "Vehicle",
            "Status",
        ]

        functions.write_to_csv("data/courier_list.csv", couriers, fieldnames)

        menu_select = functions.main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 3:

        orders = []

        functions.read_from_csv("data/order_info.csv", orders)

        functions.order_menu("Order", orders)

        fieldnames = [
            "Index",
            "Name",
            "Address",
            "Phone_Number",
            "Courier",
            "Product(s)",
            "Current_Status",
        ]

        functions.write_to_csv("data/order_info.csv", orders, fieldnames)

        menu_select = functions.main_menu()
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 0:
        print("Thankyou!")
        break

functions.rate_sys()
