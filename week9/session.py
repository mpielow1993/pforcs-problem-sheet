# Reference: https://httpd.apache.org/docs/1.3/logs.html

import pandas as pd
import helper_methods as help
import matplotlib.pyplot as plt

# Method:   plot_total_downloaded_data_per_session():
# Description:  Prompts the user for the name of a log file.
#   For a valid log file, collects the Datetime, Session ID and Number of Bytes downloaded within each line.
#   Builds a pandas dataframe containing the above attributes as columns, with Datetime as its index.
#   Outputs a plot showing the total amount of downloaded data in bytes for each Session ID in the entire log file.
def plot_total_downloaded_data_per_session():
    valid_file_param = True
    log_file_name = input('Enter the name of the file:   ')
    if not help.file_exists(log_file_name):
        valid_file_param = False
    valid_file_extensions = ['log']
    if not help.is_valid_file(log_file_name, valid_file_extensions):
        valid_file_param = False
    if valid_file_param:
        with open(log_file_name, 'r') as reader:
            log_entries = []
            for log_entry in reader.readlines():
                log_entries.append(help.build_dataframe_row(log_entry))
            times = list(map(lambda x: x['timeOccurred'], log_entries))
        df = pd.DataFrame(log_entries, index = times, columns = ['sessionId', 'noOfBytesDownloaded'])
        df = df.groupby(['sessionId'])['noOfBytesDownloaded'].sum().nlargest()
        df.plot(x = 'Session ID', y = 'No Of Bytes Downloaded', kind = 'bar', label = 'No Of Bytes Downloaded', rot = 5, fontsize = 6)
        plt.xlabel('Session ID')
        plt.ylabel('No of Bytes Downloaded')
        plt.title('G00398780 - Weekly Task 09')
        plt.legend()
        plt.show()
    if not help.do_not_replay():
        plot_total_downloaded_data_per_session()