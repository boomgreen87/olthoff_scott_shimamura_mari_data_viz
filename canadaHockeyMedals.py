import csv
import matplotlib.pyplot as plt
import numpy as np

# Creating arrays
categories = []
canadaMedals = []
canadaHockeyGold = []
canadaHockeySilver = []
canadaHockeyBronze = []

with open ('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "CAN":
			canadaMedals.append([row[2], row[7]])

	for medal in canadaMedals:
		if medal[0] == "Ice Hockey" and medal[1] == "Gold":
			canadaHockeyGold.append(medal)
		elif medal[0] == "Ice Hockey" and medal[1] == "Silver":
			canadaHockeySilver.append(medal)
		elif medal[0] == "Ice Hockey" and medal[1] == "Bronze":
			canadaHockeyBronze.append(medal)

print('Canada has won', len(canadaHockeyGold), 'gold medals', len(canadaHockeySilver), 
	'silver medals and', len(canadaHockeyBronze), 'bronze medals in Ice Hockey')





# Donut graph visualization
plt.rcdefaults()

labels = ('Gold', 'Silver', 'Bronze') # Sets labels
sizes = (int(len(canadaHockeyGold)), int(len(canadaHockeySilver)), int(len(canadaHockeyBronze))) # Sets sizes
colors = ('gold', 'silver', 'chocolate') # Sets colours

# Draws the chart
fig, ax = plt.subplots()
plt.pie(sizes, colors=colors, labels=sizes, labeldistance=0.7)

# Sets labels
plt.axis('equal')
plt.legend(labels, loc=1)
plt.xlabel("Number of Medals", fontweight='bold')
plt.suptitle('Canada Olympic Medals in Ice Hockey', fontsize=16, fontweight='bold')
plt.title('(Since 1924)')

# Draws circle in middle
circle=plt.Circle( (0,0), 0.5, color='white')
p=plt.gcf()
p.gca().add_artist(circle)

plt.show()





# Horizontal bar graph visualization
plt.rcdefaults()

labels = ('Gold', 'Silver', 'Bronze') # Creates y labels
y_pos = np.arange(len(labels)) # The y locations for the ticks
sizes = (int(len(canadaHockeyGold)), int(len(canadaHockeySilver)), int(len(canadaHockeyBronze))) # Sets bar sizes

# Plots the bars
fig, ax = plt.subplots()
plt.barh(y_pos, sizes, align='center', color=['gold', 'silver', 'chocolate'])

# Sets labels and ticks
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.invert_yaxis()  # Labels read top-to-bottom
plt.ylabel('Medal', fontweight='bold')
plt.xlabel('Number of Medals', fontweight='bold')
plt.suptitle('Canada Olympic Medals in Ice Hockey', fontsize=16, fontweight='bold')
plt.title('(Since 1924)')

# Shows the graph
plt.show()
