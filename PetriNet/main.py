# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


    #Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
import pandas
import pm4py
import os
from pm4py.objects.conversion.log import converter as log_converter
## Import the alpha_miner algorithm
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
#from pm4py.visualization.petrinet import visualizer as pn_visualizer






def import_csv(file_path):
    event_log = pandas.read_csv(file_path, sep=';', header=1)
    event_log = pm4py.format_dataframe(event_log, case_id='caseID', activity_key='activity', timestamp_key='timestamp')
    event_log.rename(columns={'case ID': 'case:concept:name', 'activity': 'concept:name', 'timestamp': 'time:timestamp',
                              'on_off': 'org:resource'}, inplace=True)
    # Convert to log format
    log = log_converter.apply(event_log)
    #start_activities = pm4py.get_start_activities(event_log)
    #end_activities = pm4py.get_end_activities(event_log)
    #print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))
    return log




    # Restituisce la lista delle caratteristiche estratte



if __name__ == "__main__":
    cwd = os.getcwd()  # Get the current working directory (cwd)
    print(cwd)
    files=os.listdir(cwd)
    log = import_csv('dataset_prova.csv')

    # heuristics miner
    net, im, fm = heuristics_miner.apply(log)

    # viz
    #gviz = pn_visualizer.apply(net, im, fm)
    #pn_visualizer.view(gviz)


    pm4py.save_vis_petri_net(net, im, fm, 'petri_net.png')
