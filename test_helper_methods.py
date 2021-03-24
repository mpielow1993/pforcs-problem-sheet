import helper_methods as help
from unittest import mock


def test_in_permitted_float_range():
    assert help.in_permitted_float_range(5.0, 1.0, 10.0) is True, 'Input, min and max are of tye float. Input is between min and max'
    assert help.in_permitted_float_range('BAD_INPUT', 1.0, 10.0) is False, 'Input cannot be parsed to a float'
    assert help.in_permitted_float_range(5.0, 'BAD_MIN', 10.0) is False, 'Minimum cannot be parsed to a float'
    assert help.in_permitted_float_range(5.0, 1.0, 'BAD_MAX') is False, 'Maximum cannot be parsed to a float'
    assert help.in_permitted_float_range(5.0, 1.0, 'BAD_MAX') is False, 'Maximum cannot be parsed to a float'
    assert help.in_permitted_float_range(1.0, 5.0, 10.0) is False, 'Input cannot be less than min'
    assert help.in_permitted_float_range(5.0, 5.0, 10.0) is False, 'Input cannot be equal to min'
    assert help.in_permitted_float_range(10.0, 1.0, 5.0) is False, 'Input cannot be greater than max'
    assert help.in_permitted_float_range(10.0, 1.0, 10.0) is True, 'Input can be equal to max'


# in_permitted_int_range works in a very similar fashion, so is omitted from testing here


def test_positive_float_difference():
    assert help.positive_float_difference(2.0, 3.0) == 1.0, 'Smaller number subtracted from larger number. Larger 2nd.'
    assert help.positive_float_difference(3.0, 2.0) == 1.0, 'Smaller number subtracted from larger number. Larger 1st.'
    assert help.positive_float_difference('BAD_PARAM_1', 2.0) is False, 'Param 1 cannot be parsed to a float.'
    assert help.positive_float_difference(2.0, 'BAD_PARAM_2') is False, 'Param 2 cannot be parsed to a float.'


# Reference: https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
# Reference: https://forum.learncodethehardway.com/t/testing-input-and-print/1757/3
def test_do_not_replay():
    exit_list = [ 
        'exit',
        'Exit', 
        'eXit',
        'exIt',
        'exiT' 
    ]

    repeat_list = [
        'Exits',
        'Quit',
        'Any other random input string'
    ]

    for exit_string in exit_list:
        with mock.patch('builtins.input', return_value = f'{exit_string}'):
            assert help.do_not_replay() is True, f'Typing "{exit_string}" quits the method'
    
    for repeat_string in repeat_list:
        with mock.patch('builtins.input', return_value = f'{repeat_string}'):
            assert help.do_not_replay() is False, f'Typing "{repeat_string}" repeats the method'


def test_http_request_successful():
    assert help.http_request_successful(200) is True, 'Should be True'
    assert help.http_request_successful(403) is False, 'Should be False'
    assert help.http_request_successful(500) is False, 'Should be False'


# TO-DO - Find a way to test method test_internet_connection_present()


def test_error_msg():
    valid_str = 'A Valid String'
    assert help.error_msg(valid_str) == '\nERROR: ' + valid_str, 'ERROR prepended correctly for valid string'
    # TO-DO - Find an example of a class that cannot be parsed to a string


def test_parse_float():
    assert help.parse_float('3.56') is True, 'Input string that should be able to be parsed to a float'
    assert help.parse_float('3') is True, 'Input string that should be able to be parsed to a float'
    assert help.parse_float('CANT_PARSE_TO_FLOAT') is False, 'Input string that should be able to be parsed to a float'


def test_parse_string():
    assert help.parse_str('rgardeghye45tdf534534') is True, 'Input string should be able to be parsed to string'
    assert help.parse_str('') is True, 'Empty input should be able to be parsed to string'
    # TO-DO - Find an example of an input that should not be able to be parsed to a string


# Ignore testing parse_int() - functions similarly to parse_float()


def test_file_exists():

    existing_files = [
        'week7/access.log.txt',
        'helper_methods.py',
        'week2/bmi.py'
    ]

    non_existing_files = [
        'week6/access.log.txt',
        'helpers.py',
        'week2/bitcoin.py'
    ]

    for existing_file in existing_files:
        assert help.file_exists(existing_file) is True, f'Existing file "{existing_file}" is indicated to exist'

    for non_existing_file in non_existing_files:
        assert help.file_exists(non_existing_file) is False, f'Non-existing file "{non_existing_file}" is indicated to not exist'


def test_is_valid_answer():

    all_valid_answers = [
        'John',
        'Paul',
        'George',
        'Ringo'
    ]

    answer_list_1 = all_valid_answers

    answer_list_2 = [
        'jOhn',
        'paUl',
        'geoRge',
        'riNGo',
        'Mick',
        'Ronnie'
    ]

    for answer in answer_list_1:
        assert help.is_valid_answer(answer, all_valid_answers) is True, f'"{answer}" should be a valid answer'

    for answer in answer_list_2:
        assert help.is_valid_answer(answer, all_valid_answers) is False, f'"{answer}" should not be a valid answer'


def test_parse_string_to_dict_item():

    delimiter = '='

    str_with_no_delimiter = 'PARAM_VALUE'
    assert help.parse_string_to_dict_item(str_with_no_delimiter, delimiter) == {}, 'Test string eith no delimiter returns empty dict item' 

    str_with_one_delimiter = f'PARAM{delimiter}VALUE'
    assert help.parse_string_to_dict_item(str_with_one_delimiter, delimiter) == { 'PARAM': 'VALUE' }, 'Test string with exactly 1 delimiter returns non-empty dict item'

    str_with_more_than_one_delimiter = f'PARAM{delimiter}VAL{delimiter}UE'
    assert help.parse_string_to_dict_item(str_with_more_than_one_delimiter, delimiter) == {}, 'Test string with more than 1 delimiter returns empty dict item'       


def test_build_url_dict():
    
    url_1 = ''
    assert help.build_url_dict(url_1) is False, 'Empty url should return False'

    url_2 = 'https://www.youtube.com/'
    url_2_dict = {
        'resource': 'www.youtube.com',
        'parameters': {}
    }

    assert help.build_url_dict(url_2) == url_2_dict, 'Test build_url_dict() for url with no params'

    url_3 = "http://www.buttercupgames.com/category.screen?categoryId=SHOOTER"
    url_3_dict = {
        'resource': 'www.buttercupgames.com/category.screen',
        'parameters': {
            'categoryId': 'SHOOTER'
        }
    }

    print(help.build_url_dict(url_3))

    assert help.build_url_dict(url_3) == url_3_dict, 'Test build_url_dict() for url with params'

    url_4 = 'https://www.youtube.com/?DSDOFNSFDKL9ERW9'
    url_4_dict = {
        'resource': 'www.youtube.com',
        'parameters': {}
    }

    assert help.build_url_dict(url_4) == url_4_dict, 'Test build_url_dict() for url with improperly formatted query string'

    url_5 = 'https://www.youtube.com/?param1=PAR=1&param2=PARAM_2'
    url_5_dict = {
        'resource': 'www.youtube.com',
        'parameters': {
            'param2': 'PARAM_2'
        }
    }

    assert help.build_url_dict(url_5) == url_5_dict, 'Test build_url_dict() for url with query param containing more than one equals'



def test_build_http_request_dict():

    http_request_1 = ''
    assert help.build_http_request_dict(http_request_1) is False, 'Empty http request should return False'

    http_request_2 = '199.15.234.66 - - [15/Feb/2021:18:24:31] "GET /cart.do?action=view&itemId=EST-6&productId=SC-MG-G10&JSESSIONID=SD5SL9FF2ADFF4958 HTTP 1.1" 200 3033 "http://www.google.com" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.28) Gecko/20120306 YFF3 Firefox/3.6.28 ( .NET CLR 3.5.30729; .NET4.0C)" 177'
    http_request_2_dict = {
        'resource': '/cart.do',
        'parameters': {
            'action': 'view',
            'itemId': 'EST-6',
            'productId': 'SC-MG-G10',
            'JSESSIONID': 'SD5SL9FF2ADFF4958'
        },
        'noOfBytesDownloaded': '177'
    }

    print(help.build_http_request_dict(http_request_2))

    assert help.build_http_request_dict(http_request_2) == http_request_2_dict, 'Test build_http_request_dict() for url with params'


if __name__ == "__main__":
    test_in_permitted_float_range()
    test_positive_float_difference()
    test_do_not_replay()
    test_http_request_successful()
    test_error_msg()
    test_parse_float()
    test_parse_string()
    test_file_exists()
    test_is_valid_answer()
    test_build_url_dict()
    test_parse_string_to_dict_item()
    test_build_http_request_dict()
    print("ALL TESTS PASSED")