# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


    #Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
import pandas
import pm4py
import os
from pm4py.objects.petri_net.utils.decomposition import decompose


def import_csv(file_path):
    event_log = pandas.read_csv(file_path, sep=';',header=1)
    event_log = pm4py.format_dataframe(event_log, case_id='caseID', activity_key='activity', timestamp_key='timestamp')
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))
    return event_log

if __name__ == "__main__":
    cwd = os.getcwd()  # Get the current working directory (cwd)
    print(cwd)
    files=os.listdir(cwd)
    log = import_csv('dataset.CSV')
    net, im, fm = pm4py.discover_petri_net_alpha(log)
    list_nets = decompose(net, im, fm)
    
for index, model in enumerate(list_nets):
        subnet, s_im, s_fm = model

        pm4py.save_vis_petri_net(subnet, s_im, s_fm, str(index)+".png")