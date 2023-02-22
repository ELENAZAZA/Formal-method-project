# Smart Home Tracking Habits


Introduction

**1.1. Syntesis of the work done**

The Smart Home Tracking Habits project aims to create a system capable of modelling a user's habits at home using a Petri net.
The habits are collected by the sensors of the smart devices.
The system should be able to identify any anomalies in the user's behavior and report them to the user or a monitoring system. 
This will be done by an analysis which compute different parameters.
In order to do that we followed the steps above:
1. We created a dataset containing the set of habits of the user
2. A model (log event) has been generated from the dataset in the point 1
3. We created a dataset containing the set of wrong habits of the user
4. The wrong dataset has been used for creating another model in order to create a Petri Net 
5. The model of the right dataset and the wrong Petri Net have been compared
6. Anomalous activity detection


The analysis gave us good results because it shows that the system is able to recognize the irregular habits of the user. 

**1.2. Technology used**

In order to do this project we use the following technologies:

* Python: we used this programming language to implement the system and the anomalies identification algorithm. We thought to use it because of it provides
  a lot of libraries useful for terminate the project.
* Pm4py: is an open-source Python library that provides a wide range of tools for process mining, a field of computer science focused on the extraction of knowledge from event logs. It provides several tools, we used the following:
  - pm4py.objects.conversion.log
  - pm4py.visualization.petri_net import visualizer as pt_visualiser
  - pm4py.visualization.sna import visualizer as sna_visualiser
  - pm4py.algo.organizational_mining.sna import algorithm as sna_factory
  - pm4py.discover_petri_net_inductive
  - pm4py.conformance_diagnostics_token_based_replay
  - pm4py.save_vis_petri_net
  - pm4py.convert_to_event_log

* GitHub: to version and to increase the efficiency of the collaboration among the group project's members
* Colab: to write the code and to obtaining a more clear output
* Excel: to create the datasets


**2.2. Dataset**

The dataset is a set of information regarding the considered user's habits.
Each event log represents a sequence of actions performed by the user at home. The action available in the dataset are the following:
such as turning on lights, opening doors, or using appliances. 

A routine has been created for each day of a week. 

This is an example of a Monday routine: 

![alt tag](https://github.com/ELENAZAZA/Formal-method-project/blob/main/dataset.png)

The dataset has been created by using Excel. It is composed of many features:
* Day (scrivere cosa indica e formato) e dire quali valori può contenere
Tutte le features si trovano un'unica riga separata da ...
Le righe in totale sono...

Foto di tutto il dataset giusto

Foto di tutto il dataset sbagliato facendo notare almeno una differenza con quello giusto

Tecnica di importazione del dataset nel progetto.


So, in this project the event logs are useful because they allow to extract several insights about the user's behavior that include his daily routines, patterns of activities, duration of the activities and the order through which the activities are executed.


**2.3. Inductive miner**
In this project, Inductive Miner is used as the process discovery algorithm to generate a Petri net model from the event log data. One of the main advantages of using Inductive Miner is its ability to handle noisy and incomplete event logs.

The Inductive Miner algorithm is able to generate a simple, easy-to-understand process model that accurately reflects the user's behavior, making it ideal for our project. The resulting Petri net model can be used to analyze the user's habits, detect anomalies in their behavior, and provide personalized feedback and recommendations.


![alt tag](https://github.com/ELENAZAZA/Formal-method-project/blob/main/petrinet.png)



**3.1. Conformance checking**

Conformance checking is a process mining technique that compares a process model to an event log to determine how well the model fits the actual behavior captured in the log. One way to perform conformance checking is through token replay.


Token replay checks whether the sequence of activities in the log matches the sequence of activities in the model. If the log events follow the model exactly, the token will reach the end of the model without any errors. However, if the log events deviate from the model, the token will encounter an error and stop, indicating that the log and model do not conform.

 Token replay is a useful technique for conformance checking, as it allows analysts to identify discrepancies between a process model and an event log and diagnose the causes of those discrepancies.



**3.2. Results achieved.**
 Below we present the output obtained, in which the percentage of trace fitness is shown for each day, which indicates that measures how well the model fits the log.

- ![alt tag](https://github.com/ELENAZAZA/Formal-method-project/blob/main/screen_trace-fitness.png)

Overall, token replay is a useful technique for conformance checking, as it allows analysts to identify discrepancies between a process model and an event log and diagnose the causes of those discrepancies.

Non-compliant activities have been diagnosed in our project. Below is a screen of the output obtained after the diagnostics:

![alt tag](https://github.com/ELENAZAZA/Formal-method-project/blob/main/Result.png)
