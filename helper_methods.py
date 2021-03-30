# Reference: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python 
# Reference: https://book.pythontips.com/en/latest/ternary_operators.html
# Reference: https://www.kite.com/python/answers/how-to-check-internet-connection-in-python
# Reference: https://www.w3schools.com/python/ref_requests_response.asp
# Reference

import requests, os.path, re
from os import path
from datetime import datetime

# Constants
LOG_ENTRY_HTTP_REQUEST = 0
LOG_ENTRY_URL = 1
LOG_ENTRY_NO_OF_BYTES_DOWNLOADED = 2
LOG_ENTRY_DATETIME = 3
LOG_ENTRY_HTTP_REQUEST_REGEX = 'GET|POST|PUT|PATCH|HTTP1.1'
LOG_ENTRY_URL_REGEX = 'http:\\/\\/|https:\\/\\/'
LOG_ENTRY_DATETIME_REGEX = '\\[|\\]'


# Method: try_parse()   
# Description:  
#   Returns true if a given input can be parse to a given data type, false otherwise
def try_parse(input, data_type, datetime_format = '%d/%b/%Y:%H:%M:%S'):    
    try:
        if data_type is None:
            return False
        if data_type in (bool, float, int, str):
            data_type(input)
            return True
        elif data_type is datetime:
            datetime.strptime(input, datetime_format)
            return True
    except(ValueError):
        return False


# Method: in_permitted_range()
# Description: 
#   Checks that a given input, minimum and maximum are all a given data type.
#   Returns true if input is in-between min & max, false otherwise
def in_permitted_range(input, min, max, data_type):
    valid_data_types = (bool, float, int, str)
    if data_type in valid_data_types:
        param_dict = {
            'Input': input,
            'Minimum': min,
            'Maximum': max
        }
        for key, value in param_dict.items():
            if not try_parse(value, data_type):
                print(error_msg(f'{key} cannot be converted to a decimal'))
                return False
        if data_type(input) <= min:
            print(error_msg(f'Input cannot be less than or equal to {min}'))
            return False
        if data_type(input) > max:
            print(error_msg(f'Input cannot be greater than {max}'))
            return False
        return True
    else:
        return False


# Method:  positive_difference()
# Description:   
#   Finds the greatest of two numbers of a given data type. 
#   Subtracts the smallest from the greatest to return the positive difference between the two.
def positive_difference(argument1, argument2, data_type):
    if not try_parse(argument1, data_type):
        print(error_msg(f'Argument 1 of "positive_difference()" cannot be parsed to {data_type}'))
        return False
    if not try_parse(argument2, data_type):
        print(error_msg(f'Argument 2 of "positive_difference()" cannot be parsed to {data_type}'))
        return False
    return (argument1 - argument2, argument2 - argument1)[argument1 <= argument2]


# Method:   do_not_replay()
# Description:   
#   Prompts the user to re-use the program to which it is appended 
def do_not_replay():
    choice = input('\nEnter any key to try again, or enter "exit" (case-insensitive) to quit:   ')
    if choice.upper() == 'EXIT':
        print('\nGoodbye')
        return True
    else:
        return False


# Method:   http_request_successful()  
# Description:   
#   Checks the reponse code for a given http request. 
#   Returns true if request successful, false otherwise. 
#   Prints appropriate message.
def http_request_successful(response_code):
    return response_code == 200


# Method:   internet_connection_present)()  
# Description:   
#   Returns true if the user is connected to the internet, false otherwise
def internet_connection_present(url):
    timeout = 5
    try:
        requests.get(url, timeout = timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        print(error_msg("No internet connection."))
        return False


# Method:   error_msg()
# Description:   
#   Prepends an error prefix onto a string to mark said string as an error message
def error_msg(output):
    if try_parse(output, str):
        return '\nERROR: ' + output
    return '\nERROR: parameter "output" in of method "errorMsg() cannot be parsed to a string"'


# Method:   file_exists()
# Description:   
#   Returns true if a file exists with name equal to the supplied input, false otherwise
def file_exists(file_name):
    if not path.isfile(file_name):
        print(error_msg(f'File "{file_name}" does not exist.'))
        return False
    else:
        return True


# Method:   is_valid_answer()
# Description:  
#   Returns true if the user_input is equal to a value in valid answers, false otherwise
def is_valid_answer(user_input, valid_answers):
    return user_input in valid_answers


# Method:   is_valid_file()
# Description:  
#   Returns true if the extension of a given file is in a list of permitted file extensions, false otherwise
def is_valid_file(file_name, valid_file_extensions):
    if len(valid_file_extensions) >= 1:
        if re.match(f'^.*(\\.{"|".join(valid_file_extensions)})$', file_name):
            return True
        print(error_msg(f'File extension must be one of the following:\n({", ".join(valid_file_extensions)})'))
        return False
    else:
        return False


# Method:   build_http_request_dict()
# Description:  
#   Separates the values for the resource and parameters of a given HTTP request
def build_log_entry_section_dict(log_entry, log_entry_section):
    valid_log_entry_sections = (LOG_ENTRY_HTTP_REQUEST, LOG_ENTRY_URL)
    if not log_entry_section in valid_log_entry_sections:
        return None
    log_entry = get_log_entry_section(log_entry, log_entry_section)
    log_entry_dict = {}
    param_dict = {}
    log_entry = re.split(r'\?|\/\?', log_entry)
    log_entry_dict['resource'] = (log_entry[0], log_entry[0][:-1])[log_entry[0][-1] == '/']
    if len(log_entry) > 1:
        param_list = list(map(lambda x: parse_to_dict_item(x, '='), log_entry[1].split('&')))
        if len(param_list) >= 1:
            for param in param_list:
                param_dict.update(param)
    log_entry_dict['parameters'] = param_dict
    return log_entry_dict


# Method: get_log_entry_section()     
# Description: 
#   Gets the string value for given section for a given line of a server log entry
def get_log_entry_section(log_entry, log_entry_section):
    if try_parse(log_entry, str):
        log_entry_list = str(log_entry).replace(' ', '').split('"')
        valid_log_entry_sections = (LOG_ENTRY_URL, LOG_ENTRY_HTTP_REQUEST, LOG_ENTRY_DATETIME, LOG_ENTRY_NO_OF_BYTES_DOWNLOADED)
        if log_entry_section in valid_log_entry_sections:
            if log_entry_section is LOG_ENTRY_URL:
                log_entry_list = list(filter(lambda x: re.search(f'{LOG_ENTRY_URL_REGEX}', x), log_entry_list))       
                if len(log_entry_list) > 0:
                    return log_entry_list[0]
                else:
                    return None
            elif log_entry_section is LOG_ENTRY_HTTP_REQUEST:
                log_entry_list = list(filter(lambda x: re.search(f'{LOG_ENTRY_HTTP_REQUEST_REGEX}', x), log_entry_list))
                if len(log_entry_list) > 0:
                    log_entry_list = log_entry_list[0]
                    log_entry_list = re.split(f'{LOG_ENTRY_HTTP_REQUEST_REGEX}', log_entry_list)        
                    return log_entry_list[1]
                else:
                    return None       
            elif log_entry_section is LOG_ENTRY_DATETIME:
                log_entry_list = list(filter(lambda x: re.search(f'{LOG_ENTRY_DATETIME_REGEX}', x), log_entry_list))
                if len(log_entry_list) > 0:
                    log_entry_list = log_entry_list[0]
                    log_entry_list = re.split(f'{LOG_ENTRY_DATETIME_REGEX}', log_entry_list)     
                    return log_entry_list[1]
                else:
                    return None   
            elif log_entry_section is LOG_ENTRY_NO_OF_BYTES_DOWNLOADED:
                if try_parse(log_entry_list[-1], float):
                    return log_entry_list[-1]
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None


# Method:   Build dataframe_row()   
# Description:  
#   Builds a given row of the pandas dataframe needed for the plot from week9
def build_dataframe_row(log_entry):    
    if log_entry and try_parse(log_entry, str):
        log_entry = str(log_entry)
        processed_log_entry = {}
        log_entry_section = get_log_entry_section(log_entry, LOG_ENTRY_DATETIME)
        if log_entry_section is not None:
            if try_parse(log_entry_section, datetime, '%d/%b/%Y:%H:%M:%S'):
                processed_log_entry['timeOccurred'] = datetime.strptime(log_entry_section, '%d/%b/%Y:%H:%M:%S')
        log_entry_section = get_log_entry_section(log_entry, LOG_ENTRY_HTTP_REQUEST)
        if log_entry_section is not None:
            http_request_param_dict = build_log_entry_section_dict(log_entry, LOG_ENTRY_HTTP_REQUEST)['parameters']
            if 'JSESSIONID' in http_request_param_dict:
                processed_log_entry['sessionId'] = http_request_param_dict['JSESSIONID']
        log_entry_section = get_log_entry_section(log_entry, LOG_ENTRY_NO_OF_BYTES_DOWNLOADED)
        if log_entry_section is not None:
            if try_parse(log_entry_section, float):
                processed_log_entry['noOfBytesDownloaded'] = float(log_entry_section)
        return processed_log_entry
    else:
        return None


# Method Signature:   parse_string_to_dict_item()
# Description:  
#   Checks if the given string contains one and only one occurrence of the given delimiter. 
#   If so, splits the string by the given delimiter, then generates a key-value pair for the first and second parts, respectively.
def parse_to_dict_item(string, delimiter):
    string = str(string)
    delimiter = str(delimiter)
    dict_item = {}
    if string.count(delimiter) == 1:
        split_string = string.split(delimiter)
        dict_item = {split_string[0]: split_string[1]}
    return dict_item
