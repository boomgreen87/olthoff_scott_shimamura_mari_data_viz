import csv
import matplotlib.pyplot as plt
import numpy as np


# Line graph with the y axis CANADA VS USA - 2 lines. The x axis is gold, silver and bronze. 
# The y axis is the countries plus the amount of medals 

Canada_1924 = []
Canada_1960 = []
Canada_1976 = []
Canada_2002 = []
Canada_2014 = []
USA_1924 = []
USA_1960 = []
USA_1976 = []
USA_2002 = []
USA_2014 = []


categories = []


with open ('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader: 
		if line_count is 0: 
			categories.append(row)
			line_count += 1
	
		# this is our information about Canada
		if row[0] == "1924" and row[4] == "CAN":
			Canada_1924.append(row)
		elif row[0] == "1960" and row[4] == "CAN":
			Canada_1960.append(row)
		elif row [0] == "1976" and row [4] == "CAN":
			Canada_1976.append(row)
		elif row[0] == "2002" and row[4] == "CAN":
			Canada_2002.append(row)
		elif row[0] == "2014" and row[4] == "CAN":
			Canada_2014.append(row)
		# this is our information on USA
		elif row[0] == "1924" and row[4] == "USA":
			USA_1924.append(row)
		elif row[0] == "1960" and row[4] == "USA":
			USA_1960.append(row)
		elif row[0] == "1976" and row[4] == "USA":
			USA_1976.append(row)
		elif row[0] == "2002" and row[4] == "USA":
			USA_2002.append(row)
		elif row[0] == "2014" and row[4] == "USA":
			USA_2014.append(row)

# getting value 
CanMedals = (len(Canada_1924), len(Canada_1960), len(Canada_1976),len(Canada_2002), len(Canada_2014))

UsaMedals = (len(USA_1924), len(USA_1960), len(Canada_1976), len(USA_2002), len(USA_2014))


# line graph visualization
plt.rcdefaults()

x_pos = np.arange(len(CanMedals))

# lines
fig, ax = plt.subplots()
plt.plot(CanMedals, label='Canada', color='cyan', linewidth=4)
plt.plot(UsaMedals, label='USA', color='magenta', linewidth=4)

# labels and ticks
plt.ylabel('CANADA VS USA')
plt.xlabel('YEAR')
plt.suptitle('Total Medals Canada VS USA')
ax.set_xticks(x_pos)
ax.set_xticklabels(('1924','1960','1976','2002','2014'))
plt.legend()


# visual for the line graph
plt.show ()



# scatter plot visualization
plt.rcdefaults()

years = ['1924','1960','1976','2002','2014']

plt.scatter(years, CanMedals, label='Canada', color='cyan', marker="o")
plt.scatter(years, UsaMedals, label='USA', color='magenta', marker="o")

plt.xlabel('Years')
plt.ylabel('Countries')
plt.title('Canada VS USA \n Totals Medals')
plt.legend()
plt.show()
