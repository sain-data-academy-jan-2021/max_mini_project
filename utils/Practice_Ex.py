import os

os.system("clear")
import utils.functions as functions
import login
import csv

hot_drinks = []
cold_drinks = []
alco_drinks = []

with open("data/hot_drinks.txt", "r") as file:
    for product in file:
        hot_drinks.append(product.strip())

with open("data/cold_drinks.txt", "r") as file:
    for product in file:
        cold_drinks.append(product.strip())

with open("data/alco_drinks.txt", "r") as file:
    for product in file:
        alco_drinks.append(product.strip())

menu_select = ""
acceptable_values = [0, 1, 2, 3, 4]

while menu_select not in acceptable_values:
    menu_select = functions.main_menu()

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
while menu_select != "0":
    if menu_select == 1:

        num_select = input(
            "1.) Hot Drinks Menu     2.) Cold Drinks Menu    3.) Alcoholic Drinks Menu   0.) Exit. "
        )

        while num_select != "0":
            if num_select == "1":
                functions.item_menu("Hot Drink", hot_drinks)

            elif num_select == "2":
                functions.item_menu("Cold Drink", cold_drinks)

            elif num_select == "3":
                functions.item_menu("Alcoholic Drink", alco_drinks)

            else:
                print("Please enter a vaild number.")

            num_select = input(
                "1.) Hot Drinks Menu     2.) Cold Drinks Menu    3.) Alcoholic Drinks Menu   0.) Exit. "
            )

        with open("data/hot_drinks.txt", "w") as file:
            for drink in hot_drinks:
                file.write(drink + "\n")
        with open("data/cold_drinks.txt", "w") as file:
            for drink in cold_drinks:
                file.write(drink + "\n")
        with open("data/alco_drinks.txt", "w") as file:
            for drink in alco_drinks:
                file.write(drink + "\n")

        print("Thankyou. Here is our full menu list.")
        print(hot_drinks)
        print(cold_drinks)
        print(alco_drinks)

        menu_select = functions.main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 2:

        couriers = []

        with open("data/courier_list.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                couriers.append(row)

        functions.courier_menu("Courier ", couriers)

        with open("data/courier_list.csv", "w") as file:
            fieldnames = ["Name", "Age", "Vehicle", "Status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for row in couriers:
                writer.writerow(row)

        menu_select = functions.main_menu()

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 3:

        orders = []

        with open("data/order_info.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                orders.append(row)

        functions.order_menu("Order", orders)

        with open("data/order_info.csv", "w") as file:
            fieldnames = [
                "First_Name",
                "Second_Name",
                "Address",
                "Phone_Number",
                "Courier",
                "Status",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for row in orders:
                writer.writerow(row)

        menu_select = functions.main_menu()
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 0:
        print("Thankyou!")
        break

functions.rate_sys()
