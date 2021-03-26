import pandas as pd
import helper_methods as help
import matplotlib.pyplot as plt

    
def build_session_dataframe():
    valid_file_param = True
    log_file_name = input('Enter the name of the file:   ')

    if not help.file_exists(log_file_name):
        print(help.error_msg('File does not exist.'))
        valid_file_param = False
    
    if valid_file_param:
        with open(log_file_name, 'r') as reader:
            log_entries = []
            for log_entry in reader.readlines():
                log_entries.append(help.build_dataframe_row(log_entry))
            times = list(map(lambda x: x['timeOccurred'], log_entries))
            # Apply appropriate delimiter to separate the url from the rest of the standard format string within each line of the sample log file
            # Reference: https://httpd.apache.org/docs/1.3/logs.html
        #print(log_entries)
        df = pd.DataFrame(log_entries, index = times, columns = ['sessionId', 'noOfBytesDownloaded'])
        #df.sort_index(inplace = True, ascending = True)
        df = df.groupby(['sessionId'])['noOfBytesDownloaded'].sum().nlargest()
        df.plot(x = 'Session ID', y = 'No Of Bytes Downloaded', kind = 'bar', label = 'No Of Bytes Downloaded', rot = 5, fontsize = 6)

        plt.xlabel('Session ID')
        plt.ylabel('No of Bytes Downloaded')
        plt.title('G00398780 - Weekly Task 09')
        plt.legend()

        plt.show()
    if not help.do_not_replay():
        build_session_dataframe()