import os

os.system("clear")
import utils.functions as functions
import login
from utils.main_functions import *
from utils.DB_funcs import *

connection = db_connect()

menu_select = ""
acceptable_values = [0, 1, 2, 3]


header()

while menu_select not in acceptable_values:
    menu_select = functions.main_menu()


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

header()

while menu_select != "0":
    if menu_select == 1:

        drinks = []

        functions.drinks_menu("Drinks ", drinks, connection)

        menu_select = functions.main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 2:

        couriers = []

        functions.courier_menu("Courier ", couriers, connection)

        menu_select = functions.main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 3:

        orders = []

        functions.read_from_csv("data/order_info.csv", orders)

        functions.order_menu("Order", orders)

        fieldnames = [
            "Id",
            "Name",
            "Address",
            "Phone",
            "Courier",
            "Products",
            "Status",
        ]

        functions.write_to_csv("data/order_info.csv", orders, fieldnames)

        menu_select = functions.main_menu()
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 0:
        print("Thankyou!")
        break


functions.rate_sys()

connection.close()
