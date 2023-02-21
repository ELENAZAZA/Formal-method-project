# Tracking Habit System


Introduction

**1.1. Aim of the Project**

The Tracking Habit System project aims to create a system capable of tracking a user's habits at home using a Petri net. The system should be able to identify any anomalies in the user's behavior and report them to the user or a monitoring system.

**1.2. Technology used**

The project uses the following technologies:
Python: to implement the system and the anomaly identification algorithm.
pm4py: to perform the modeling and analysis of the Petri net.
GitHub: to version and share the source code.

**PetriNet**


**2.1. Pm4py**
Pm4py is an open-source Python library that provides a wide range of tools for process mining, a field of computer science focused on the extraction of knowledge from event logs. 

**2.2. Dataset**

The dataset contains information about a user's habits.
Each event log represents a sequence of actions performed by the user at home, such as turning on lights, opening doors, or using appliances. The event logs can be used to extract useful insights about the user's behavior, such as their daily routines or patterns of activity.

A routine is described by 12 activities for each day of the week.

**2.3. Inductive miner**
In this project, Inductive Miner is used as the process discovery algorithm to generate a Petri net model from the event log data. One of the main advantages of using Inductive Miner is its ability to handle noisy and incomplete event logs.

The Inductive Miner algorithm is able to generate a simple, easy-to-understand process model that accurately reflects the user's behavior, making it ideal for our project. The resulting Petri net model can be used to analyze the user's habits, detect anomalies in their behavior, and provide personalized feedback and recommendations.

![alt tag](https://github.com/ELENAZAZA/Formal-method-project/blob/main/petrinet.png)

**3. Conclusions**

**3.1. Conformance checking**

**3.2. Results achieved.**


![alt tag](https://github.com/ELENAZAZA/Formal-method-project/blob/main/Result.png)
