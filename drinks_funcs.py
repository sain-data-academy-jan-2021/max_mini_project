from DB_funcs import *

# DRINKS MENU FUNCTIONS.

# ----------------------------------------------------------------------------------------------


def drinks_add(connection):

    name = input("Product Name: ")
    ptype = input("Product Type: ")
    price = float(input("Product Price: "))
    status = input("Product Status: ")
    db_do(
        connection,
        f'insert into products (drink, type, price, status) VALUES ("{name}", "{ptype}", {price}, "{status}")',
    )


# ----------------------------------------------------------------------------------------------


def drinks_update(connection):

    valid_drink = False

    while not valid_drink:
        update_prod = input("Name of product you would like to update?: ")
        new_price = float(input("New Price: "))
        drinks_list = execute_sql_select(
            connection, f'SELECT * from products WHERE drink = "{update_prod}"'
        )
        if len(drinks_list) != 0:
            db_do(
                connection,
                f'UPDATE products price SET price = "{new_price}" WHERE drink = "{update_prod}"',
            )
            break
        else:
            print("Invalid Selection. Try Again. ")
            continue


# ----------------------------------------------------------------------------------------------


def drinks_delete(connection):

    valid_drink = False

    while not valid_drink:
        del_prod = input("Name of product you would like to delete: ")
        drink_list = execute_sql_select(
            connection, f'SELECT * from products WHERE drink = "{del_prod}"'
        )
        if len(drink_list) != 0:
            db_do(connection, f'DELETE FROM products WHERE drink = "{del_prod}"')
            break
        else:
            print("Invalid Selection. Try Again. ")
            continue
