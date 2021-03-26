import average


def test_average_to():

    valid_list = [1, 2, 3, 4, 5]
    invalid_value_ist = [1, 'Fish', 3, 4, 5]
    empty_list = []

    valid_index = 3
    invalid_numeric_index = 6
    non_numeric_index = 'Dog'

    # First, test vaid param values for list and index_to
    assert average.average_to(valid_list, valid_index) == 2, 'Test average_to works as expected for valid values of list and average_to'

    # Test type checking by switching the values of the list and index_to params in the method call
    assert average.average_to(valid_index, valid_index) is False, 'Test index_to can only be of type int'
    assert average.average_to(valid_list, valid_list) is False, 'Test list can only be of type list'

if __name__ == "__main__":
    test_average_to()
    print("ALL TESTS PASSED")