import pandas as pd

def get_download_data_qty_for_session():
    path = '/data'
    log_file_name = path + 'access.log'
    df = pd.read_csv(log_file_name, sep = ' ', header = None)
    print(df)