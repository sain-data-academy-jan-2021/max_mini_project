import unittest
from orders_funcs import *
from DB_funcs import *
from unittest.mock import Mock, patch


class OrderFunctionsTests(unittest.TestCase):

    # HAPPY PATH TESTS.

    # ----------------------------------------------------------------------------------------------
    # ADDING TO ORDERS.

    @patch("builtins.input")
    @patch("orders_funcs.choose_prods_for_ord")
    @patch("orders_funcs.db_do")
    @patch("orders_funcs.execute_sql_select")
    @patch("orders_funcs.print_order_summary")
    def test_ord_add(
        self, mock_summary, mock_execute, mock_db_do, mock_c_p_f_o, mock_input
    ):
        mock_input.side_effect = ["Harry", "123 London Street", "012345", "1"]
        connection = None
        mock_c_p_f_o.return_value = ["2"]
        mock_summary.return_value = (
            (26, "Harry", "123 London Street", "012345", "Pending", "Coffee", "1.8"),
        )
        mock_execute.return_value = ((26,),)
        statement = (
            "insert into orders_products (order_id, product_id) values ('26', '2')"
        )
        ord_add(connection)
        mock_db_do.assert_called_with(connection, statement)
        self.assertEqual(mock_db_do.call_count, 2)

    # ----------------------------------------------------------------------------------------------
    # DELETING FROM ORDERS.

    @patch("builtins.input")
    @patch("orders_funcs.execute_sql_select")
    @patch("orders_funcs.db_do")
    def test_ord_delete(self, mock_db_do, mock_execute, mock_input):
        mock_input.side_effect = ["4"]
        mock_execute.return_value = (
            (4, "Shaquille", "43 Green Close", "7567845398", "3", "Pending."),
        )
        connection = None
        ord_delete(connection)
        statement = 'DELETE FROM orders WHERE order_id = "4"'
        mock_db_do.assert_called_with(connection, statement)
        self.assertEqual(mock_db_do.call_count, 2)

    # ----------------------------------------------------------------------------------------------
    # UPDATING ORDERS.

    @patch("builtins.input")
    @patch("orders_funcs.execute_sql_select")
    @patch("orders_funcs.db_do")
    def test_ord_delete(self, mock_db_do, mock_execute, mock_input):
        mock_input.side_effect = ["2", "Ready."]
        mock_execute.return_value = (
            (2, "Jack", "4 Sunnyside Road", "79276541884", "1", "Pending."),
        )
        connection = None
        ord_update(connection)
        statement = 'UPDATE orders status SET status = "Ready." WHERE order_id = "2"'
        mock_db_do.assert_called_with(connection, statement)
        # self.assertEqual(mock_db_do.call_count, 2)
