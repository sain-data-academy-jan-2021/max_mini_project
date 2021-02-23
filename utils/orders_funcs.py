from utils.DB_funcs import *
from utils.main_functions import *


def print_table_drinks(connection):
    data_list = import_prod_db(connection)
    x = PrettyTable()
    x.field_names = ["Id", "Drink", "Type", "Price", "Status"]
    for items in data_list:
        x.add_row(
            (
                items[0],
                items[1],
                items[2],
                items[3],
                items[4],
            )
        )
    print(x)


def print_table_summary(connection, order_id):
    data_list = print_order_summary(connection, order_id)
    x = PrettyTable()
    x.field_names = ["ID", "Name", "Address", "Phone Number", "Status", "Product(s)"]
    products = []
    for item in data_list:
        products.append(item[5])
    x.add_row(
        (
            data_list[0][0],
            data_list[0][1],
            data_list[0][2],
            data_list[0][3],
            data_list[0][4],
            products,
        )
    )
    print(x)


def ord_add(connection):

    cursor = connection.cursor()

    name = input("Customer Name: ")
    add = input("Customer Address: ")
    pnum = input("Phone: ")
    cour = input("Courier: ")
    status = "Pending."
    prods = choose_prods_for_ord(connection)
    cursor.execute(
        f'INSERT INTO orders (name, address, phone, courier, status) VALUES ("{name}", "{add}", "{pnum}", {cour}, "{status}")'
    )
    order_id = execute_sql_select(connection, "select MAX(order_id) from orders")[0][0]
    for prod in prods:
        db_do(
            connection,
            f"insert into orders_products (order_id, product_id) values ('{order_id}', '{prod}')",
        )
    print_table_summary(connection, order_id)


def print_order_summary(connection, order_id):

    cursor = connection.cursor()

    summary = execute_sql_select(
        connection,
        f"SELECT o.order_id, o.name, o.address, o.phone, o.status, p.drink, p.price FROM orders_products op JOIN orders o on op.order_id = o.order_id JOIN products p on op.product_id = p.product_id WHERE op.order_id = {order_id}",
    )
    return summary


def ord_update(connection):

    cursor = connection.cursor()

    valid_order = False

    while not valid_order:
        update_ord = input("ID of the order that you would like to update?: ")
        new_stat = input("New Status: ")
        cursor.execute(f'SELECT * from orders WHERE order_id = "{update_ord}"')
        valid_order = check_id_in_db(cursor)

    cursor.execute(
        f'UPDATE orders status SET status = "{new_stat}" WHERE order_id = "{update_ord}"'
    )
    cursor.close()


def ord_delete(connection):

    cursor = connection.cursor()
    valid_order = False

    while not valid_order:
        del_ord = input("ID of the order that you would like to delete: ")
        cursor.execute(f'SELECT * from orders WHERE order_id = "{del_ord}"')
        valid_order = check_id_in_db(cursor)

    cursor.execute(f'DELETE FROM orders_products WHERE order_id = "{del_ord}"')
    cursor.execute(f'DELETE FROM orders WHERE order_id = "{del_ord}"')
    cursor.close()


def choose_prods_for_ord(connection):
    ids = [
        id[0]
        for id in execute_sql_select(connection, "SELECT product_id from products")
    ]
    products_ids = []
    print_table_drinks(connection)
    while True:
        id = input(
            "Please select a ID from the table. Select as many as you like. When done, eneter 0."
        )
        if int(id) == 0:
            break
        elif int(id) not in ids:
            print("Invalid Selection.")
            continue
        products_ids.append(id)
    return products_ids
