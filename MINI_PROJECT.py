import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

os.system("clear")
import login
from main_functions import *
from DB_funcs import *
from rating_funcs import *

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

        drinks_menu("Drink ", drinks, connection)

        menu_select = main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 2:

        couriers = []

        courier_menu("Courier ", couriers, connection)

        menu_select = main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 3:

        orders = []

        order_menu("Order ", orders, connection)

        menu_select = main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 0:
        print("Thankyou!")
        break


rate_sys(connection)

connection.close()
