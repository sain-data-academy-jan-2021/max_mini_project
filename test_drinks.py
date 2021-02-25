import unittest
from drinks_funcs import *
from DB_funcs import *
from unittest.mock import Mock, patch


class DrinkFunctionsTests(unittest.TestCase):
    @patch("builtins.input")
    @patch("drinks_funcs.db_do")
    def test_drinks_add(self, mock_execute, mock_input):
        mock_input.side_effect = ["Coffee", "Hot", "2.00", "Available"]
        connection = None
        drinks_add(connection)
        statement = 'insert into products (drink, type, price, status) VALUES ("Coffee", "Hot", 2.0, "Available")'
        mock_execute.assert_called_with(connection, statement)
        

    @patch("builtins.input")
    @patch("drinks_funcs.check_id_in_db")
    def test_drinks_delete(self, mock_valid_drink, mock_input):
        
                
