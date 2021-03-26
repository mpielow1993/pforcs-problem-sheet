import helper_methods as help

def average_to(list, to_index):

    if type(list) is not list:
        print(help.error_msg('"list" parameter must be of type "list"'))
        return False
 
    if type(list) is not int:
        print(help.error_msg('"to_index" parameter must be of type "int"'))
        return False

    if not help.in_permitted_int_range(to_index, 0, len(list) - 1):
        print(help.error_msg('index out of range for list'))
        return False
    
    list = list[to_index]

    for element in list:
        if not help.parse_float(element):
            print(help.error_msg(f'"{element}" cannot be parsed to a float - thus a numerical average cannot be obtained'))
            return False
    
    return sum(list) / len(list)