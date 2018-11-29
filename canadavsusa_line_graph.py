import csv
import matplotlib.pyplot as plt
import numpy as np


# Line graph with the y axis CANADA VS USA - 2 lines. The x axis is gold, silver and bronze. 
# The y axis is the countries plus the amount of medals 
# 
Canada_1924 = []
Canada_1928 = []
Canada_1932 = []
Canada_1948 = []
Canada_1952 = []
Canada_1960 = []
Canada_1964 = []
Canada_1968 = []
Canada_1976 = []
Canada_1984 = []
Canada_1992 = []
Canada_1994 = []
Canada_1998 = []
Canada_2002 = []
Canada_2004 = []
Canada_2010 = []
Canada_2014 = []
USA_1924 = []
USA_1928 = []
USA_1932 = []
USA_1936 = []
USA_1948 = []
USA_1952 = []
USA_1956 = []
USA_1960 = []
USA_1964 = []
USA_1968 = []
USA_1972 = []
USA_1976 = []
USA_1980 = []
USA_1984 = []
USA_1988 = []
USA_1992 = []
USA_1994 = []
USA_1998 = []
USA_2002 = []
USA_2006 = []
USA_2010 = []
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
		if row[0] == "1924" and row[4] == "CAN"
		Canada_1924.append(row)
		elif row[0] == "1928" and row[4] == "CAN"
		Canada_1928.append(row)
		elif row [0] == "1932" and row[4] == "CAN"
		Canada_1932.append(row)
		elif row[0] == "1948" and row[4] == "CAN"
		Canada_1948.append(row)
		elif row[0] == "1952" and row[4] == "CAN"
		Canada_1952.append(row)
		elif row[0] == "1960" and row[4] == "CAN"
		Canada_1960.append(row)
		elif row[0] == "1964" and row[4] == "CAN"
		Canada_1962.append(row)
		elif row[0] == "1976" and row[4] == "CAN"
		Canada_1976.append(row)
		elif row[0] == "1984" and row[4] == "CAN"
		Canada_1986.append(row)
		elif row[0] == "1992" and row[4] == "CAN"
		Canada_2002.append(row)
		elif row[0] == "2006" and row[4] == "CAN"
		Canada_2006.append(row)
		elif row[0] == "2010" and row[4] == "CAN"
		Canada_2010.append(row)
		elif row[0] == "2014" and row[4] == "CAN"
		Canada_2014.append(row)
		# this is our information on USA
		elif row[0] == "1924" and row[4] == "USA"
		USA_1924.append(row)
		elif row[0] == "1928" and row[4] == "USA"
		USA_1928.append(row)
		elif row[0] == "1932" and row[4] == "USA"
		USA_1932.append(row)
		elif row[0] == "1948" and row[4] == "USA"
		USA_1948.append(row)
		elif row[0] == "1952" and row[4] == "USA"
		USA_1952.append(row)
		elif row[0] == "1956" and row[4] == "USA"
		USA_1956.append(row)
		elif row[0] == "1960" and row[4] == "USA"
		USA_1960.append(row)
		elif row[0] == "1964" and row[4] == "USA"
		USA_1964.append(row)
		elif row[0] == "1968" and row[4] == "USA"
		USA_1968.append(row)
		elif row[0] == "1972" and row[4] == "USA"
		USA_1972.append(row)
		elif row[0] == "1976" and row[4] == "USA"
		USA_1976.append(row)
		elif row[0] == "1984" and row[4] == "USA"
		USA_1984.append(row)
		elif row[0] == "1988" and row[4] == "USA"
		USA_1988.append(row)
		elif row[0] == "1992" and row[4] == "USA"
		USA_1992.append(row)
		elif row[0] == "1998" and row[4] == "USA"
		USA_1998.append(row)
		elif row[0] == "2002" and row[4] == "USA"
		USA_2002.append(row)
		elif row[0] == "2006" and row[4] == "USA"
		USA_2006.append(row)
		elif row[0] == "2010" and row[4] == "USA"
		USA_2010.append(row)
		elif row[0] == "2014" and row[4] == "USA"
		USA_2014.append(row)






# putting everything into a line graph 
# setting up x and y axis 

ind = np.arange(len())
plt.xlabel('Years')
plt.ylabel('Countries - CANADA VS USA')


		





















plt.ylabel('Countries: Canada VS U.S.A')
plt.xlabel('Medals')

plt.show()