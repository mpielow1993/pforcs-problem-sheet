# Reference: https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
# Reference: https://forum.learncodethehardway.com/t/testing-input-and-print/1757/3

import helper_methods as help
from unittest import mock
from datetime import datetime

# Test for method:   in_permitted_range()
def test_in_permitted_range():
    assert help.in_permitted_range(5.0, 1.0, 10.0, float) is True, 'input, min and max are of type float + input is between min and max should return True'
    assert help.in_permitted_range('BAD_INPUT', 1.0, 10.0, float) is False, 'value for input that cannot be parsed to a float should return False'
    assert help.in_permitted_range(5.0, 'BAD_MIN', 10.0, float) is False, 'value for minimum that cannot be parsed to a float should return False'
    assert help.in_permitted_range(5.0, 1.0, 'BAD_MAX', float) is False, 'value for maximum that cannot be parsed to a float should return False'
    assert help.in_permitted_range(1.0, 5.0, 10.0, float) is False, 'input, min and max are of type float + input between min and max should return True'
    assert help.in_permitted_range(5.0, 5.0, 10.0, float) is False, 'input, min and max are of type float + input equal to min should return False'
    assert help.in_permitted_range(10.0, 1.0, 5.0, float) is False, 'input, min and max are of type float + input greater than max should return False'
    assert help.in_permitted_range(10.0, 1.0, 10.0, float) is True, 'input, min and max are of type float + input equal to max should return True'


# Test for method:   positive_difference()
def test_positive_difference():
    assert help.positive_difference(2.0, 3.0, float) == 1.0, 'smaller number subtracted from larger number, with larger 2nd'
    assert help.positive_difference(3.0, 2.0, float) == 1.0, 'smaller number subtracted from larger number. Larger 1st.'
    assert help.positive_difference('BAD_ARGUMENT_1', 2.0, float) is False, 'value for argument1 that cannot be parsed to a float should return False'
    assert help.positive_difference(2.0, 'BAD_ARGUMENT_2', float) is False, 'value for argument2 that cannot be parsed to a float should return False'


# Test for method:   do_not_replay()
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


# Test for method:   http_request_successful()
def test_http_request_successful():
    assert help.http_request_successful(200) is True, 'Successful request should return True'
    assert help.http_request_successful(403) is False, 'Forbidden request should return False'
    assert help.http_request_successful(500) is False, 'Internal error should return False'


# Test for method:   internet_connection_present()
#def test_internet_connection_present():
    # TO-DO - Find a way to test method test_internet_connection_present()


# Test for method:   error_msg
def test_error_msg():
    valid_str = 'A Valid String'
    assert help.error_msg(valid_str) == '\nERROR: ' + valid_str, 'ERROR prepended correctly for valid string'


# Test for method:   try_parse()
def test_try_parse():
    # Test when input is of type bool, float, int or str
    valid_float_strings = [
        '3.56',
        '3',
        '3.141'
    ]
    invalid_float_strings = [
        ''
        'CANT_PARSE_TO_FLOAT',
        '3/4'
    ]
    for valid_float_string in valid_float_strings:
        assert help.try_parse(valid_float_string, float) is True, f'string that can be parsed to a float "{valid_float_string}" should return True'
    for invalid_float_string in invalid_float_strings:
        assert help.try_parse(invalid_float_string, float) is False, f'string that cannot be parsed to a float "{invalid_float_string}" should return False'
    # Tests above would be identical for str, int and bool
    # TO-DO - Find an example of an input that should not be able to be parsed to a string
    # Test when input is datetime
    valid_datetime_items = [
        {
            'value': '15/Feb/2021:18:24:31',
            'datetime_format': '%d/%b/%Y:%H:%M:%S'
        },
        {
            'value': '15-Feb-2021:18:24:31',
            'datetime_format': '%d-%b-%Y:%H:%M:%S'
        },    
                {
            'value': '15-February-2021:18:24:31',
            'datetime_format': '%d-%B-%Y:%H:%M:%S'
        }       
    ]
    invalid_datetime_items = [
        {
            'value': '15-Feb-2021:18:24:31',
            'datetime_format': '%d/%b/%Y:%H:%M:%S'
        },
        {
            'value': '15/Feb/2021:18:24:31',
            'datetime_format': '%d-%b-%Y:%H:%M:%S'
        },    
                {
            'value': '15-February-2021:18:24:31',
            'datetime_format': '%d-%B-%Y'
        }  
    ]
    for valid_datetime_item in valid_datetime_items:
        assert help.try_parse(valid_datetime_item['value'], datetime, valid_datetime_item['datetime_format']) is True, f'string that can be parsed to a datetime "{valid_datetime_item["value"]}" should return True'
    for invalid_datetime_item in invalid_datetime_items:
        assert help.try_parse(invalid_datetime_item['value'], datetime, invalid_datetime_item['datetime_format']) is False, f'string that cannot be parsed to a datetime "{invalid_datetime_item["value"]}" should return False'


# Test for method:   file_exists()
def test_file_exists():
    existing_files = [
        'week7/access.log',
        'helper_methods.py',
        'week2/bmi.py'
    ]
    non_existing_files = [
        'week6/access.log.txt',
        'helpers.py',
        'week2/bitcoin.py'
    ]
    for existing_file in existing_files:
        assert help.file_exists(existing_file) is True, f'Existing file "{existing_file}" should return True'
    for non_existing_file in non_existing_files:
        assert help.file_exists(non_existing_file) is False, f'Non-existing file "{non_existing_file}" should return False'


# Test for method:   is_valid_file()
def test_is_valid_file():
    valid_file_extensions = [
        'txt',
        'log'
    ]
    valid_files = [
        'week7/access.log',
        'dfjskj.sdfisd.txt',
        'a_test_file_123.log'
    ]
    invalid_files = [
        'week7/access.jpg',
        'log.jpg',
        'txt.txt.py'
    ]
    for valid_file in valid_files:
        assert help.is_valid_file(valid_file, valid_file_extensions) is True, f'File with valid extension "{valid_file}" should return True'
    for invalid_file in invalid_files:
        assert help.is_valid_file(invalid_file, valid_file_extensions) is False, f'File with invalid extension "{invalid_file}" should return False'


# Test for method:   is_valid_answer()
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


# Test for method:   parse_to_dict_item()
def test_parse_to_dict_item():
    delimiter = '='
    str_1 = 'KEY_VALUE'
    str_2 = f'KEY{delimiter}VALUE'
    str_3 = f'KEY{delimiter}VAL{delimiter}UE'
    assert help.parse_to_dict_item(str_1, delimiter) == {}, 'string eith no delimiter should return empty dict item' 
    assert help.parse_to_dict_item(str_2, delimiter) == { 'KEY': 'VALUE' }, 'string with exactly 1 delimiter should return non-empty dict item'
    assert help.parse_to_dict_item(str_3, delimiter) == {}, 'string with more than 1 delimiter should return empty dict item'       


# Test for method:   get_log_entry_section()
def test_get_log_entry_section():
    log_entry_1 = '91.205.189.27 - - [15/Feb/2021:18:46:24] "POST /cart.do?action=addtocart&itemId=EST-12&productId=CU-PG-G06&JSESSIONID=SD8SL8FF3ADFF5080 HTTP 1.1" 200 2931 "http://www.buttercupgames.com/product.screen?productId=CU-PG-G06" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5" 697'
    # Valid log entr(y/ies)
    assert help.get_log_entry_section(log_entry_1, help.LOG_ENTRY_DATETIME) == '15/Feb/2021:18:46:24', 'datetime in valid log entry is correctly returned'
    assert help.get_log_entry_section(log_entry_1, help.LOG_ENTRY_HTTP_REQUEST) == '/cart.do?action=addtocart&itemId=EST-12&productId=CU-PG-G06&JSESSIONID=SD8SL8FF3ADFF5080', 'HTTP request in valid log entry is correctly returned'
    assert help.get_log_entry_section(log_entry_1, help.LOG_ENTRY_URL) == 'http://www.buttercupgames.com/product.screen?productId=CU-PG-G06', 'URL in valid log entry is correctly returned'
    assert help.get_log_entry_section(log_entry_1, help.LOG_ENTRY_NO_OF_BYTES_DOWNLOADED) == '697', 'no of bytes downloaded in valid log entry is correctly returned'
    # Invalid log entr(y/ies)
    log_entry_2 = 'isfbiefbweufwpefnwuengpewrgerugnweifmre'
    # Valid log entr(y/ies)
    assert help.get_log_entry_section(log_entry_2, help.LOG_ENTRY_DATETIME) is None, 'datetime in invalid log entry returns None'
    assert help.get_log_entry_section(log_entry_2, help.LOG_ENTRY_HTTP_REQUEST) is None, 'HTTP request in invalid log entry returns None'
    assert help.get_log_entry_section(log_entry_2, help.LOG_ENTRY_URL) is None, 'URL in invalid log entry returns None'
    assert help.get_log_entry_section(log_entry_2, help.LOG_ENTRY_NO_OF_BYTES_DOWNLOADED) is None, 'no of bytes downloaded in invalid log entry returns None'


# Test for method:   build_log_entry_section_dict()
def test_build_log_entry_section_dict():
    log_entry_1 = '117.21.246.164 - - [15/Feb/2021:18:36:03] "POST /cart.do?action=addtocart&itemId=EST-27&productId=DC-SG-G02&JSESSIONID=SD9SL6FF8ADFF5015 HTTP 1.1" 200 1291 "http://www.buttercupgames.com/cart.do?action=addtocart&itemId=EST-27&productId=DC-SG-G02" "Googlebot/2.1 (http://www.googlebot.com/bot.html)" 795'
    invalid_log_entry_sections = (help.LOG_ENTRY_DATETIME, help.LOG_ENTRY_NO_OF_BYTES_DOWNLOADED)
    for invalid_log_entry_section in invalid_log_entry_sections:
        assert help.build_log_entry_section_dict(log_entry_1, invalid_log_entry_section) is None, 'build_log_entry_section_dict() for invalid log entry sections returns None'
    url_dict_1 = {
        'resource': 'http://www.buttercupgames.com/cart.do',
        'parameters': {
            'action': 'addtocart',
            'itemId': 'EST-27',
            'productId': 'DC-SG-G02'

        }
    }
    http_request_dict_1 = {
        'resource': '/cart.do',
        'parameters': {
            'action': 'addtocart',
            'itemId': 'EST-27',
            'productId': 'DC-SG-G02',
            'JSESSIONID': 'SD9SL6FF8ADFF5015'
        }
    }
    assert help.build_log_entry_section_dict(log_entry_1, help.LOG_ENTRY_URL) == url_dict_1, 'url dict correctly returned for valid log entry'
    assert help.build_log_entry_section_dict(log_entry_1, help.LOG_ENTRY_HTTP_REQUEST) == http_request_dict_1, 'http_request dict correctly returned for valid log_entry'


# Test for method:   build_date_frame_row()
def test_build_dataframe_row():
    log_entry_1 = '112.111.162.4 - - [15/Feb/2021:18:26:37] "GET /category.screen?categoryId=NULL&JSESSIONID=SD7SL8FF5ADFF4964 HTTP 1.1" 505 2445 "http://www.buttercupgames.com/category.screen?categoryId=NULL" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5" 393'
    dataframe_row_1_dict = {
        'timeOccurred': datetime(2021, 2, 15, 18, 26, 37),
        'sessionId': 'SD7SL8FF5ADFF4964',
        'noOfBytesDownloaded': 393
    }
    log_entry_2 = '112.111.162.4 - - [dvldjsnvjv] "GET /category.screen?categoryId=NULL&JSESSIONID=SD7SL8FF5ADFF4964 HTTP 1.1" 505 2445 "http://www.buttercupgames.com/category.screen?categoryId=NULL" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5" 393'
    dataframe_row_2_dict = {
        'sessionId': 'SD7SL8FF5ADFF4964',
        'noOfBytesDownloaded': 393
    }
    log_entry_3 = '112.111.162.4 - - [15/Feb/2021:18:26:37] "GET /category.screen?categoryId=NULL&dfdgrgdbfdfb HTTP 1.1" 505 2445 "http://www.buttercupgames.com/category.screen?categoryId=NULL" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5" 393'
    dataframe_row_3_dict = {
        'timeOccurred': datetime(2021, 2, 15, 18, 26, 37),
        'noOfBytesDownloaded': 393
    }
    log_entry_4 = '112.111.162.4 - - [15/Feb/2021:18:26:37] "GET /category.screen?categoryId=NULL&JSESSIONID=SD7SL8FF5ADFF4964 HTTP 1.1" 505 2445 "http://www.buttercupgames.com/category.screen?categoryId=NULL" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5" erfrergerg'
    dataframe_row_4_dict = {
        'timeOccurred': datetime(2021, 2, 15, 18, 26, 37),
        'sessionId': 'SD7SL8FF5ADFF4964'
    }
    print(help.get_log_entry_section(log_entry_4, help.LOG_ENTRY_NO_OF_BYTES_DOWNLOADED))
    assert help.build_dataframe_row(log_entry_1) == dataframe_row_1_dict, 'dataframe row correctly returned for log entry with valid time occurred + valid session_id + valid no of bytes downloaded'
    assert help.build_dataframe_row(log_entry_2) == dataframe_row_2_dict, 'dataframe row correctly returned for log entry with invalid time occurred + valid session_id + valid no of bytes downloaded'
    assert help.build_dataframe_row(log_entry_3) == dataframe_row_3_dict, 'dataframe row correctly returned for log entry with valid time occurred + invalid session_id + valid no of bytes downloaded'
    assert help.build_dataframe_row(log_entry_4) == dataframe_row_4_dict, 'dataframe row correctly returned for log entry with valid time occurred + valid session_id + invalid no of bytes downloaded'

        
if __name__ == "__main__":
    test_in_permitted_range()
    test_try_parse()
    test_do_not_replay()
    test_http_request_successful()
    test_error_msg()
    test_file_exists()
    test_is_valid_file()
    test_is_valid_answer()
    test_build_log_entry_section_dict()
    test_parse_to_dict_item()
    test_get_log_entry_section()
    test_build_dataframe_row()
    print("ALL TESTS PASSED")