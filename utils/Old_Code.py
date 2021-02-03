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






def item_menu(item, list):
    print(list)
    choose_option = input(
        f"1.) Add A {item}  2.) Remove A {item}    3.) Update A {item}    0.) Exit "
    )
    while choose_option != "0":
        if choose_option == "1":
            add_item = input(f"What {item.lower()} would you like to add? ")
            list.append(add_item)
            print(list)
        elif choose_option == "2":
            remove_item = input(
                f"Ok. Which {item.lower()} would you like to take out? "
            )
            list.remove(remove_item)
            print(list)
        elif choose_option == "3":
            update_item = input(f"Sure. Which {item.lower()} needs updating? ")
            if update_item in list:
                update_item_new = input("What would you like to change it too? ")
                list.remove(update_item)
                list.append(update_item_new)
                print(list)
        choose_option = input(
            f"1.) Add A {item}  2.) Remove A {item}    3.) Update A {item}    0.) Exit "
        )