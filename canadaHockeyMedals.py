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
fig, ax = plt.subplots()

labels = ('Gold', 'Silver', 'Bronze')
sizes = (int(len(canadaHockeyGold)), int(len(canadaHockeySilver)), int(len(canadaHockeyBronze)))
colors = ('gold', 'silver', 'chocolate')

plt.pie(sizes, colors=colors, labels=sizes, labeldistance=0.7)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.xlabel("Number of Medals")
ax.set_title("How many Olympic medals has Canada won in Ice Hockey? (Since 1924)")

# Draws circle in middle
circle=plt.Circle( (0,0), 0.5, color='white')
p=plt.gcf()
p.gca().add_artist(circle)

plt.show()





# Horizontal bar graph visualization
plt.rcdefaults()
fig, ax = plt.subplots()

labels = ('Gold', 'Silver', 'Bronze')
y_pos = np.arange(len(labels))
sizes = (int(len(canadaHockeyGold)), int(len(canadaHockeySilver)), int(len(canadaHockeyBronze)))
error = np.random.rand(len(labels))

ax.barh(y_pos, sizes, xerr=error, align='center', color=['gold', 'silver', 'chocolate'])
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.invert_yaxis()  # Labels read top-to-bottom
ax.set_ylabel('Medal')
ax.set_xlabel('Number of Medals')
ax.set_title('How many Olympic medals has Canada won in Ice Hockey? (Since 1924)')

plt.show()
