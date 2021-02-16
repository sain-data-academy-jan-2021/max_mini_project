from utils import main_functions
from unittest.mock import Mock, patch
menu_select = ""
acceptable_values = [0, 1, 2, 3]

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
#                                            HAPPY PATH.          
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

def test_main_menu():

    expected = 3

    result = main_menu()

    assert result == expected
    print("Works 1.")


test_main_menu()

# # ------------------------------------------------------------------------------------------------------------

def test_read_from_csv():

    # Assemble
    filename = "test/test_courier_list.csv"
    my_list = []

    # Act
    read_from_csv(filename, my_list)

    # Assert
    assert len(my_list) == 2
    assert my_list[0]["Name"] == "Martin"
    assert my_list[1]["Age"] == "41"
    print("Works 2.")


test_read_from_csv()

# # ------------------------------------------------------------------------------------------------------------

def test_write_to_csv():

    # Assemble
    filename = "test/test_write_to_csv.csv"
    a_list = [{"Name": "Martin", "Age": 25}, {"Name": "Sheila", "Age": 30}]
    fieldnames = ["Name", "Age"]

    # Act
    write_to_csv(filename, a_list, fieldnames)

    # Assert
    b_list = []
    read_from_csv(filename, b_list)

    assert len(b_list) == 2
    assert b_list[0]["Name"] == "Martin"
    assert b_list[1]["Age"] == "30"
    print("Works 3.")


test_write_to_csv()

# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------
# #                                          UNHAPPY PATH.          
# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------


def test_main_menu():

    expected = "hello"  # Not a Acceptable Value.

    result = main_menu()

    assert result == expected
    print("Works 1.")


test_main_menu()

#------------------------------------------------------------------------------------------------------------

def test_read_from_csv():

    # Assemble
    filename = "test/test_people_list.csv"    # Wrong file.
    my_list = []

    # Act
    read_from_csv(filename, my_list)

    # Assert
    assert len(my_list) == 2
    assert my_list[0]["Name"] == "Martin"
    assert my_list[1]["Age"] == "41"
    print("Works 2.")


test_read_from_csv()

# ------------------------------------------------------------------------------------------------------------

def test_write_to_csv():

    # Assemble
    filename = "test/test_write_to_csv.csv"
    a_list = [{"Name": "Martin", "Age": 25}, {"Name": "Sheila", "Age": 30}]
    fieldnames = ["Name", "Age"]

    # Act
    write_to_csv(filename, a_list, fieldnames)

    # Assert
    b_list = []
    read_from_csv(filename, b_list)

    assert len(b_list) == 2
    assert b_list[0]["Name"] == "Marcus"    # Wrong Name Input
    assert b_list[1]["Age"] == "30"
    print("Works 3.")


test_write_to_csv()







def main_menu():

    try:
        selection = int(
            input(
                """1.) Product Menu    \n2.) Courier List    \n3.) Order Screen    \n0.) Exit. """
            )
        )
        if selection not in acceptable_values:
            print("Invalid number. Please try again. ")
        return selection
    except ValueError as err:
         print(err)




@patch("builtins.print")
@patch("builtins.input")
def test_mock_main_menu(mock_input, mock_print):

    mock_input.return_value = "4"
    main_menu()
    mock_print.assert_called_with("Invalid number. Please try again. ")
    print("Works.")

test_mock_main_menu()
