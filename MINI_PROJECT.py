import os

os.system("clear")
import login
from utils.main_functions import *
from utils.DB_funcs import * 

connection = db_connect()

menu_select = ""
acceptable_values = [0, 1, 2, 3]


header()

while menu_select not in acceptable_values:
    menu_select = main_menu()


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

header()

while menu_select != "0":
    if menu_select == 1:

        drinks = []

        drinks_menu("Drinks ", drinks, connection)

        menu_select = main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 2:

        couriers = []

        courier_menu("Courier ", couriers, connection)

        menu_select = main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    # elif menu_select == 3:

    #     orders = []

    #     functions.read_from_csv("data/order_info.csv", orders)

    #     functions.order_menu("Order", orders)

    #     fieldnames = [
    #         "Id",
    #         "Name",
    #         "Address",
    #         "Phone",
    #         "Courier",
    #         "Products",
    #         "Status",
    #     ]

    #     functions.write_to_csv("data/order_info.csv", orders, fieldnames)

    #     menu_select = main_functions.main_menu()
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 0:
        print("Thankyou!")
        break


rate_sys()

connection.close()
