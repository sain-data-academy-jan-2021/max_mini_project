from utils.DB_funcs import *


def drinks_add(connection):

    cursor = connection.cursor()

    name = input("Prodcut Name: ")
    ptype = input("Product Type: ")
    price = float(input("Product Price: "))
    status = input("Product Status: ")
    cursor.execute(
        f'insert into products (drink, type, price, status) VALUES ("{name}", "{ptype}", {price}, "{status}")'
    )
    cursor.close()


def drinks_update(connection):

    cursor = connection.cursor()
    valid_drink = False

    while not valid_drink:
        update_prod = input("ID of product you would like to update?: ")
        new_price = float(input("New Price: "))
        cursor.execute(f'SELECT * from products WHERE product_id = "{update_prod}"')
        valid_drink = check_id_in_db(cursor)
    cursor.execute(
        f'UPDATE products price SET price = "{new_price}" WHERE drink = "{update_prod}"'
    )
    cursor.close()


def drinks_delete(connection):

    cursor = connection.cursor()
    valid_drink = False

    while not valid_drink:
        del_prod = input("Name of product you would like to delete: ")
        cursor.execute(f'SELECT * from products WHERE drink = "{del_prod}"')
        valid_drink = check_id_in_db(cursor)

    cursor.execute(f'DELETE FROM products WHERE drink = "{del_prod}"')
    cursor.close()