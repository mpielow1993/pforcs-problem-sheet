import re, helper_methods as help

# Method:   extract_urls()
# Description:  extracts the url from each line of a log file decided by the user.
#   Separates the resource and parameters from each extracted url and outputs them to a dictionary.
#   Outputs a list of all created dictionaries.
def extract_urls():
    valid_file_param = True
    log_file_name = input('Enter the name of the file:   ')
    if not help.file_exists(log_file_name):
        valid_file_param = False
    valid_file_extensions = ['log']
    if not help.is_valid_file(log_file_name, valid_file_extensions):
        valid_file_param = False
    if valid_file_param:
        processed_urls = []
        with open(log_file_name, 'r') as reader:
            for log_entry in reader.readlines():
                processed_urls.append(help.build_log_entry_section_dict(log_entry, help.LOG_ENTRY_URL))
        print(processed_urls)
    if not help.do_not_replay():
        extract_urls()