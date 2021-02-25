from DB_funcs import *


def cour_update(connection):

    cursor = connection.cursor()

    valid_courier = False

    while not valid_courier:
        update_cour = input("Name of courier you would like to update?: ")
        new_stat = input("New Status: ")
        cursor.execute(f'SELECT * from couriers WHERE name = "{update_cour}"')
        valid_courier = check_id_in_db(cursor)

    cursor.execute(
        f'UPDATE couriers status SET status = "{new_stat}" WHERE name = "{update_cour}"'
    )
    cursor.close()


def cour_delete(connection):

    cursor = connection.cursor()
    valid_courier = False

    while not valid_courier:
        del_cour = input("Name of courier you would like to delete: ")
        cursor.execute(f'SELECT * from couriers WHERE name = "{del_cour}"')
        valid_courier = check_id_in_db(cursor)

    cursor.execute(f'DELETE FROM couriers WHERE name = "{del_cour}"')
    cursor.close()


def cour_add(connection):

    name = input("Courier Name: ")
    age = input("Courier Age: ")
    vehic = input("Vehicle: ")
    status = input("Courier Status: ")
    db_do(
        connection,
        f'INSERT INTO couriers (name, age, vehicle, status) VALUES ("{name}", "{age}", "{vehic}", "{status}")',
    )