import re, helper_methods as help

def extract_url():
    str = '127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"'
    split_arr = str.replace(' ', '').split('"')
    url = list(filter(lambda x: re.match(r'(http|https)://', x), split_arr))[0]
    print(url)


def extract_urls():
    valid_file_param = True
    log_file_name = input('Enter the name of the file:   ')

    if not help.file_exists(log_file_name):
        print(help.error_msg('File does not exist.'))
        valid_file_param = False
    
    if valid_file_param:
        with open(log_file_name, 'r') as reader:
            arr = reader.replace(' ', '').split('"')
            urls = list(filter(lambda x: re.match(r'(http|https)://', x), arr))
            print(urls)
    
    if not help.do_not_replay():
        extract_urls()