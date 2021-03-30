import re, helper_methods as help

# Method:   get_number_of_pattern_occurrences
# Description:  Outputs the number of occurrences of a character sequence decided by the user
def get_number_of_pattern_occurrences():
    file_name = input('Enter the name of the file:   ')
    valid_file_extensions = ['txt']
    if not help.file_exists(file_name):
        valid_file_param = False
    elif not help.is_valid_file(file_name, valid_file_extensions):
        valid_file_param = False
    else:
        valid_file_param = True
    if valid_file_param:
        pattern_to_match = input('Enter the pattern to match by:   ')
        with open(file_name, 'r') as reader:
            # The length of the split array will always be one greater than the pattern delimiter that it is split
            print(f'Number of occurrences of "{pattern_to_match}":   {len(re.split(pattern_to_match, reader.read())) - 1}')
    if not help.do_not_replay():
        get_number_of_pattern_occurrences()


