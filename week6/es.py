import re, helper_methods as help

def get_number_of_pattern_occurrences():
    valid_file_param = True
    file_name = input('Enter the name of the file:   ')

    if not help.file_exists(file_name):
        print(help.error_msg('File does not exist.'))
        valid_file_param = False
    
    if valid_file_param:
        pattern_to_match = input('Enter the pattern to match by:   ')
        with open(file_name, 'r') as reader:
            # The length of the split array will always be one greater than the pattern delimiter that it is split
            print(f'Number of occurrences of "{pattern_to_match}":   {len(re.split(pattern_to_match, reader.read())) - 1}')
    
    if not help.do_not_replay():
        get_number_of_pattern_occurrences()


