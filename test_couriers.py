import unittest
from couriers_funcs import *
from DB_funcs import *
from unittest.mock import Mock, patch


#class CourierFunctionsTests(unittest.TestCase):
    # @patch("builtins.input")
    # @patch("couriers_funcs.db_do")
    # def test_courier_add(self, mock_execute, mock_input):
    #     connection = None
    #     mock_input.side_effect = ["Munir", "27", "Car", "Free"]
    #     expected = (
    #         None,
    #         'INSERT INTO couriers (name, age, vehicle, status) VALUES ("Munir", "27", "Car", "Free")',
    #     )

    #     cour_add(connection)

    #     mock_execute.assert_called_with(expected)

    
    