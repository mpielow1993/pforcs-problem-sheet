import helper_methods as help

#   Method:   average_to()
#   Description:    Returns the average of a list of integers up to a valid positive index, None otherwise 
def average_to(list_param, to_index):
    if type(list_param) is not list:
        print(help.error_msg('"list_param" parameter must be of type "list"'))
        return None
    if len(list_param) == 0:
        return None
    if type(to_index) is not int:
        print(help.error_msg('"to_index" parameter must be of type "int"'))
        return None
    if not help.in_permitted_range(to_index, -1, len(list_param) - 1, int):
        print(help.error_msg('index out of range for list'))
        return None 
    list_param = list_param[:to_index]
    for element in list_param:
        if not help.try_parse(element, float):
            print(help.error_msg(f'"{element}" cannot be parsed to a float - thus a numerical average cannot be obtained'))
            return None    
    return sum(list_param) / len(list_param)