from DB_funcs import *

# COURIER FUNCTIONS.

# ----------------------------------------------------------------------------------------------


def cour_delete(connection):

    valid_courier = False

    while not valid_courier:
        del_cour = input("Name of courier you would like to delete: ")
        courier_list = execute_sql_select(
            connection, f'SELECT * from couriers WHERE name = "{del_cour}"'
        )
        if len(courier_list) != 0:
            db_do(connection, f'DELETE FROM couriers WHERE name = "{del_cour}"')
            break
        else:
            print("Invalid Selection. Try Again. ")
            continue


# ----------------------------------------------------------------------------------------------


def cour_add(connection):

    name = input("Courier Name: ")
    age = input("Courier Age: ")
    vehic = input("Vehicle: ")
    status = input("Courier Status: ")
    db_do(
        connection,
        f'INSERT INTO couriers (name, age, vehicle, status) VALUES ("{name}", "{age}", "{vehic}", "{status}")',
    )


# ----------------------------------------------------------------------------------------------


def cour_update(connection):

    valid_courier = False

    while not valid_courier:
        update_cour = input("Name of courier you would like to update?: ")
        new_stat = input("New Status: ")
        courier_list = execute_sql_select(
            connection, f'SELECT * from couriers WHERE name = "{update_cour}"'
        )
        if len(courier_list) != 0:
            db_do(
                connection,
                f'UPDATE couriers status SET status = "{new_stat}" WHERE name = "{update_cour}"',
            )
            break
        else:
            print("Invalid Selection. Please Try Again.")
            continue