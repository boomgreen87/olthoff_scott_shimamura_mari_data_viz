
import csv 
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np


x = ([])
#y_labels = ['Canada', 'USA']
#y_label_usa = ()
#y_label_can = ()

#plt.plot(y_label_can, color='red')
#plt.plot(y_label_usa, color='blue')
 
#x =np.linespace(0,10,1000)
x.plot(x, np.sin(x));

x = plt.axes()
x.plot (x, np.sin(x))
x.set(xlim=(1924, 1928, 1932, 1948, 1952, 1960, 1964, 1968, 1976, 1984, 1992, 1994, 1998, 2002, 2006, 2010, 2014), ylim=('Canada', 'USA'),
title = 'Comparing Canda and USA Medals throughout the years');

plt.xlabel('Years')
plt.ylabel('Countries')

plt.show()

































#fig = plt.figure()
#ax = plt.axes()


#x = np.linspace(0,10,1000)
#ax.plot(x, np.sin(x));

#creating two lines
#plt.plot(x, npsin(x))
#plt.plot(x, np.cos(x));

# x axis is years 
# y axis is countries Canada and USA

# setting the x and y axis 
#plt.xlim ("1924", "1928", "1932", "1948", "1952", "1960", "1964", "1968", "1976", "1984", "1992", "1994", "1998", "2002", "2006", "2010", "2014")
#plt.ylim (Canada, USA)


#split the data into two lines
#xdatacan
#xdatausa

#sort data so it makes clean curves
#xdatacan.sort()
#xdatdausa.sort()

#create y data points
#ydatausa = ()

# plot data 
# 

# create the events marking the x data points


# create the events marking the y data points 
