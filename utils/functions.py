import csv

menu_select = ""
acceptable_values = [0, 1, 2, 3]


def main_menu():

    try:
        selection = int(
            input(
                "1.) Product Menu    2.) Courier List    3.) Order Screen    0.) Exit. "
            )
        )
        if selection not in acceptable_values:
            print("Invalid number. Please try again. ")
        return selection
    except ValueError as err:
        print(err)


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

def drinks_menu(item, list):
    for drinks in list:
        print(drinks)
    drinks_option = input(
        f"1.) Print {item}  2.) Add A {item}    3.) Update A {item}  4.) Delete A {item}    0.) Exit "
    )
    while drinks_option != "0":
        if drinks_option == "1":
            for drinks in list:
                print(drinks)
        elif drinks_option == "2":
            idx = input("Number in list: ")
            prod = input("Name of drink: ")
            hoc = input("Hot or Cold drink: ")
            price = input("Price of drink: ")
            avail = input("Availble or Out Of Stock: ")
            drinks_dict = {
                "Index": idx,
                "Drink": prod,
                "Hot_Cold": hoc,
                "Price": price,
                "Status": avail,
            }

            list.append(drinks_dict)
            for drinks in list:
                print(drinks)
        elif drinks_option == "3":
            update_prod = input(
                "What is the Name of the Product you would like to update?: "
            )
            new_status = input("New Status of Product: ")
            current_drinks = False
            for drinks in list:
                if drinks["Drink"] == update_prod:
                    drinks["Status"] = new_status
                    for drinks in list:
                        print(drinks)
                    current_drinks = True
            if current_drinks == False:
                print("Sorry! Not a current drink.")

                return drinks
        elif drinks_option == "4":
            del_name = input(
                "What is the Name of the drink you would like to delete?: "
            )
            current_drinks = False
            for drinks in list:
                if drinks["Drink"] == del_name:
                    list.remove(drinks)
                    for drinks in list:
                        print(drinks)
                    current_drinks = True
            if current_drinks == False:
                print("Sorry! Not a current courier.")

        drinks_option = input(
            f"1.) Print {item}  2.) Add A {item}    3.) Update A {item}  4.) Delete A {item}   0.) Exit "
        )



# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def courier_menu(item, list):
    for courier in list:
        print(courier)
    courier_option = input(
        f"1.) Print {item}  2.) Add A {item}    3.) Update A {item}  4.) Delete A {item}    0.) Exit "
    )
    while courier_option != "0":
        if courier_option == "1":
            for courier in list:
                print(courier)
        elif courier_option == "2":
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
            for courier in list:
                print(courier)
        elif courier_option == "3":
            update_name = input(
                "What is the Name of the Courier you would like to update?: "
            )
            new_status = input("New Status of Courier: ")
            current_courier = False
            for courier in list:
                if courier["Name"] == update_name:
                    courier["Status"] = new_status
                    for courier in list:
                        print(courier)
                    current_courier = True
            if current_courier == False:
                print("Sorry! Not a current courier.")

                return courier
        elif courier_option == "4":
            del_name = input(
                "What is the First Name of the courier you would like to delete?: "
            )
            current_courier = False
            for courier in list:
                if courier["Name"] == del_name:
                    list.remove(courier)
                    for courier in list:
                        print(courier)
                    current_courier = True
            if current_courier == False:
                print("Sorry! Not a current courier.")

        courier_option = input(
            f"1.) Print {item}  2.) Add A {item}    3.) Update A {item}  4.) Delete A {item}   0.) Exit "
        )
    
    

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


def order_menu(item, list):
    for orders in list:
        print(orders)
    order_option = input(
        f"1.) Print {item}  2.) Add A {item}    3.) Update A {item}  4.) Delete A {item}    0.) Exit "
    )
    while order_option != "0":
        if order_option == "1":
            for order in list:
                print(order)
        elif order_option == "2":
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
                "Phone_Number": p_num,
                "Courier": cour,
                "Product(s)": prod,
                "Current_Status": stat,
            }

            list.append(order_dict)
            for order in list:
                print(order)
        elif order_option == "3":
            update_ord = input(
                "What is the Index of the order you would like to update?: "
            )
            new_status = input("New Status of order: ")
            current_order = False
            for order in list:
                if order["Index"] == update_ord:
                    order["Current_Status"] = new_status
                    for order in list:
                        print(order)
                    current_order = True
            if current_order == False:
                print("Sorry! Not a current order.")

                return order
        elif order_option == "4":
            del_ord = input(
                "What is the Index of the order you would like to delete?: "
            )
            current_order = False
            for order in list:
                if order["Index"] == del_ord:
                    list.remove(order)
                    for order in list:
                        print(order)
                    current_order = True
            if current_order == False:
                print("Sorry! Not a current order.")

        order_option = input(
            f"1.) Print {item}  2.) Add A {item}    3.) Update A {item}  4.) Delete A {item}   0.) Exit "
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
