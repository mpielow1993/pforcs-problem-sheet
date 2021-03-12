import re, helper_methods as help

def extract_urls():
    valid_file_param = True
    log_file_name = input('Enter the name of the file:   ')

    if not help.file_exists(log_file_name):
        print(help.error_msg('File does not exist.'))
        valid_file_param = False
    
    if valid_file_param:
        with open(log_file_name, 'r') as reader:
            file_string = reader.read()
            file_array = file_string.replace(' ', '').split('"')
            extracted_urls = list(filter(lambda x: re.match(r'(http|https)://', x), file_array))
            processd_urls = list(map(lambda x: help.build_url_dict(x), extracted_urls))
            print(processd_urls)
    
    if not help.do_not_replay():
        extract_urls()