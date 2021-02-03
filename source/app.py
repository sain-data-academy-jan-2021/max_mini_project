user_name = input("Username: ")
pass_word = input("Password: ")
print("Welcome back " + user_name + " to ???, It's good to see you again!")


hot_drinks = ['Tea', 'Coffee', 'Hot Chocolate'] 
cold_drinks = ['Water', 'Coke', 'Fanta', 'Sprite', 'Orange Juice']
alco_drinks = ['Beer', 'Red Wine', 'White Wine',]
menu_select = ""
acceptable_values = [0, 1, 2] 

def main_menu():
    try:
        selection = int(input("Press 1 to see product menus, 2 to see Courier information, press 0 to exit. "))
        if selection not in acceptable_values:
            print("Invalid number. Please try again. ")
        return selection
    except ValueError as err:
        print(err)
   

while menu_select not in acceptable_values:
    menu_select = main_menu()


if menu_select == 1:
   
    num_select = input("Please enter '1' for Hot Drinks menu, '2' for Cold Drinks, '3' for Alcoholic Drinks, or 0 to exit. ")
    while num_select != '0':


        if num_select == "1":
            print(hot_drinks)
            options_hot = input("To add a product press 1, to remove press 2, to update press 3, or to return press 0. ")
            while options_hot != '0':
                if options_hot == '1' :
                    hot_drink_name = input("What product would you like to add? ")
                    hot_drinks.append(hot_drink_name)
                    print(hot_drinks)
                elif options_hot == '2' :
                    remove_hot = input("Ok. Which product would you like to take out? ")
                    hot_drinks.remove(remove_hot)
                    print(hot_drinks)
                elif options_hot == '3' :
                    update_hot = input("Sure. Which product needs updating? ")
                    if update_hot in hot_drinks:
                        update_hot_new = input("What would you like to change it too? ")
                        hot_drinks.remove(update_hot)
                        hot_drinks.append(update_hot_new)
                        print(hot_drinks)
                options_hot = input("To add a product press 1, to remove press 2, to update press 3, or to return press 0. ")

        elif num_select == "2":
            print(cold_drinks)
            options_cold = input("To add a product press 1, to remove press 2, to update press 3, or to return press 0 ")
            while options_cold != '0':
                if options_cold == '1' :
                    cold_drink_name = input("What product would you like to add? ")
                    cold_drinks.append(cold_drink_name)
                    print(cold_drinks)
                elif options_cold == '2' :
                    remove_cold = input("Ok. Which product would you like to take out? ")
                    cold_drinks.remove(remove_cold)
                    print(cold_drinks)
                elif options_cold == '3' :
                    update_cold = input("Sure. Which product needs updating? ")
                    if update_cold in cold_drinks:
                        update_cold_new = input("What would you like to change it too? ")
                        cold_drinks.remove(update_cold)
                        cold_drinks.append(update_cold_new)
                        print(cold_drinks)
                options_cold = input("To add a product press 1, to remove press 2, to update press 3, or to return press 0. ")
            
            
        elif num_select == "3":
            print(alco_drinks)
            options_alco = input("To add a product press 1, to remove press 2, to update press 3, or to return press 0")
            while options_alco != '0':
                if options_alco == '1' :
                    alco_drink_name = input("What product would you like to add? ")
                    alco_drinks.append(alco_drink_name)
                    print(alco_drinks)
                elif options_alco == '2' :
                    remove_alco = input("Ok. Which product would you like to take out? ")
                    alco_drinks.remove(remove_alco)
                    print(alco_drinks)
                elif options_alco == '3' :
                    update_alco = input("Sure. Which product needs updating? ")
                    if update_alco in alco_drinks:
                        update_alco_new = input("What would you like to change it too? ")
                        alco_drinks.remove(update_alco)
                        alco_drinks.append(update_alco_new)
                        print(alco_drinks)
                options_alco = input("To add a product press 1, to remove press 2, to update press 3, or to return press 0. ")
    
    

        else:
            print("Please enter a vaild number.")

        num_select = input("Please enter '1' for Hot Drinks menu, '2' for Cold Drinks, '3' for Alcoholic Drinks, or 0 to exit. ")



    print("Thankyou. Here is our full menu list.")
    print(hot_drinks)
    print(cold_drinks)
    print(alco_drinks)

    drinks = input("Thanks! Alright, Lets get you started. What would you like to drink? ")

    drink_amount = [1, 2, 3, 4, 5]


    if drinks in hot_drinks:
        how_many_hot = input("Nice choice on a cold day like today! How many would you like? ")
        how_many_num_hot = int(how_many_hot)
        if how_many_num_hot in drink_amount:
            print("Great, we'll have those ready for you in a moment.")
        else:
            print("Sorry, maximum 5 per customer. Please try again.")  



    elif drinks in cold_drinks:
        how_many_cold = input("Nothing better that a nice cold refreshment! How many would you like? ")
        how_many_num_cold = int(how_many_cold)
        if how_many_num_cold in drink_amount:
            print("Great, we'll have those ready for you in a moment.")
        else:
            print("Sorry, maximum 5 per customer. Please try again.")


    elif drinks in alco_drinks:
        age_check = int(input("Awesome, we just need to make sure you are old enough. Please enter age: "))
        age_limit = 18
        if age_check >= age_limit:
            how_many_alco = input("Thankyou. How many would you like? ")
            how_many_num_alco = int(how_many_alco)
            if how_many_num_alco in drink_amount:
                print("Great, we'll have those ready for you soon!")
            else:
                print("Sorry, maximum 5 per customer. Please try again.")
        elif age_check < age_limit:
            print("Sorry, you are too young to buy these products. Please try again.")
        else:
            print("Sorry, invalid selection. Please try again.")

        
    else:
        print("Sorry we dont have that available right now. Please make another selection.")

    


elif menu_select == 2:

    courier_first = {
        'First Name': 'James',
        'Last Name' : 'M.',
        'age' : 38
    }
    courier_second = {
        'First Name': 'Martin',
        'Last Name' : 'C.',
        'age' : 27
    }
    courier_third = {
        'First Name': 'Sheila',
        'Last Name' : 'H.',
        'Age' : 20
    }
    couriers = [courier_first, courier_second, courier_third]
    for courier in couriers:
        print(*courier.items())

elif menu_select == '0':
    print('Thankyou!')
    exit()


    


  

rate = input("Thankyou for your order. Would you mind leaving a review for us today? ")

rate_y = ["Yes", "yes", "y", "Y"]
rate_n = ["No", "no", "n", "N"]
rate_stars = [1,2,3,4,5]

if rate in rate_y:
        rate_stars_y = int(input("Thankyou! How many stars out of 5 would you give our service? "))
        print("Thanks, we'll take that onboard. Until next time!")
elif rate in rate_n:
    print("Ok no problem. Until next time!")
else:
        print("Sorry, invalid selection. Please try again.")



    
