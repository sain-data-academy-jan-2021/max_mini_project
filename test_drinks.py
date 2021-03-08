import unittest
from drinks_funcs import *
from DB_funcs import *
from unittest.mock import Mock, patch


class DrinkFunctionsTests(unittest.TestCase):

    # HAPPY PATH TESTS.

    # ----------------------------------------------------------------------------------------------
    # ADDING TO DRINKS.

    @patch("builtins.input")
    @patch("drinks_funcs.db_do")
    def test_drinks_add(self, mock_execute, mock_input):
        mock_input.side_effect = ["Coffee", "Hot", "2.00", "Available"]
        connection = None
        drinks_add(connection)
        statement = 'insert into products (drink, type, price, status) VALUES ("Coffee", "Hot", 2.0, "Available")'
        mock_execute.assert_called_with(connection, statement)

    # ----------------------------------------------------------------------------------------------
    # DELETING FROM DRINKS.

    @patch("builtins.input")
    @patch("drinks_funcs.execute_sql_select")
    @patch("drinks_funcs.db_do")
    def test_drinks_delete(self, mock_db_do, mock_execute, mock_input):
        mock_input.side_effect = ["Coffee"]
        mock_execute.return_value = ((14, "Coffee", "Hot", "2.50", "Available"),)
        connection = None
        drinks_delete(connection)
        statement = 'DELETE FROM products WHERE drink = "Coffee"'
        mock_db_do.assert_called_with(connection, statement)

    # ----------------------------------------------------------------------------------------------
    # UPDATING DRINKS.

    @patch("builtins.input")
    @patch("drinks_funcs.execute_sql_select")
    @patch("drinks_funcs.db_do")
    def test_drinks_update(self, mock_db_do, mock_execute, mock_input):
        mock_input.side_effect = ["Water", "1.00"]
        mock_execute.return_value = ((9, "Water", "Cold", "0.50", "Available"),)
        connection = None
        drinks_update(connection)
        statement = 'UPDATE products price SET price = "1.0" WHERE drink = "Water"'
        mock_db_do.assert_called_with(connection, statement)