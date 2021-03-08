import unittest
from couriers_funcs import *
from DB_funcs import *
from unittest.mock import Mock, patch


class CourierFunctionsTests(unittest.TestCase):

    # HAPPY PATH TESTS.

    # ----------------------------------------------------------------------------------------------
    # ADDING TO COURIERS.

    @patch("builtins.input")
    @patch("couriers_funcs.db_do")
    def test_cour_add(self, mock_execute, mock_input):
        mock_input.side_effect = ["Martin", "27", "Car", "Busy"]
        connection = None
        cour_add(connection)
        statement = 'INSERT INTO couriers (name, age, vehicle, status) VALUES ("Martin", "27", "Car", "Busy")'
        mock_execute.assert_called_with(connection, statement)

    # ----------------------------------------------------------------------------------------------
    # DELETING FROM COURIERS.

    @patch("builtins.input")
    @patch("couriers_funcs.execute_sql_select")
    @patch("couriers_funcs.db_do")
    def test_cour_delete(self, mock_db_do, mock_execute, mock_input):
        mock_input.side_effect = ["Lilly"]
        mock_execute.return_value = ((6, "Lilly", 18, "Bike", "Free"),)
        connection = None
        cour_delete(connection)
        statement = 'DELETE FROM couriers WHERE name = "Lilly"'
        mock_db_do.assert_called_with(connection, statement)

    # ----------------------------------------------------------------------------------------------
    # UPDATING COURIERS.

    @patch("builtins.input")
    @patch("couriers_funcs.execute_sql_select")
    @patch("couriers_funcs.db_do")
    def test_cour_update(self, mock_db_do, mock_execute, mock_input):
        mock_input.side_effect = ["Mac", "Busy"]
        mock_execute.return_value = ((5, "Mac", "26", "Car", "Busy"),)
        connection = None
        cour_update(connection)
        statement = 'UPDATE couriers status SET status = "Busy" WHERE name = "Mac"'
        mock_db_do.assert_called_with(connection, statement)


# ----------------------------------------------------------------------------------------------
