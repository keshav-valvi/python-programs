#ATTENDACE SHEET
# KESHAV VALVI 
# FY23N052

import numpy as np
import matplotlib.pyplot as plt
#creating the dataset
data = {'keshav':87, 'himanshu':68, 'pritesh':75, 'tushar':95, 'yadnesh':39}
courses = list(data.key())
value = list(data.value())
fig = plt.figure(figsize = (10,5))
#creating the bar plot
plt.bar(courses, values, color ='green', width = '0.4')
plt.xlabel("student name")
plt.ylabel("percentage attendence")
plt.title("attendance of student in 2 semister")
plt.show()