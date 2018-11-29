import csv
import matplotlib.pyplot as plt
import numpy as np

# Creating arrays
categories = []
menGold_1924 = []
menGold_1948 = []
menGold_1972 = []
menGold_2002 = []
menGold_2014 = []
womenGold_1924 = []
womenGold_1948 = []
womenGold_1972 = []
womenGold_2002 = []
womenGold_2014 = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1

		if row[0] == '1924' and row[4] == 'CAN' and row[5] == 'Men' and row[7] == 'Gold':
			menGold_1924.append(row)
		elif row[0] == '1948' and row[4] == 'CAN' and row[5] == 'Men' and row[7] == 'Gold':
			menGold_1948.append(row)
		elif row[0] == '1972' and row[4] == 'CAN' and row[5] == 'Men' and row[7] == 'Gold':
			menGold_1972.append(row)
		elif row[0] == '2002' and row[4] == 'CAN' and row[5] == 'Men' and row[7] == 'Gold':
			menGold_2002.append(row)
		elif row[0] == '2014' and row[4] == 'CAN' and row[5] == 'Men' and row[7] == 'Gold':
			menGold_2014.append(row)
		if row[0] == '1924' and row[4] == 'CAN' and row[5] == 'Women' and row[7] == 'Gold':
			womenGold_1924.append(row)
		elif row[0] == '1948' and row[4] == 'CAN' and row[5] == 'Women' and row[7] == 'Gold':
			womenGold_1948.append(row)
		elif row[0] == '1972' and row[4] == 'CAN' and row[5] == 'Women' and row[7] == 'Gold':
			womenGold_1972.append(row)
		elif row[0] == '2002' and row[4] == 'CAN' and row[5] == 'Women' and row[7] == 'Gold':
			womenGold_2002.append(row)
		elif row[0] == '2014' and row[4] == 'CAN' and row[5] == 'Women' and row[7] == 'Gold':
			womenGold_2014.append(row)

print('Canadian men gold medals:', len(menGold_1924), 'in 1924,', len(menGold_1948), 'in 1948,', len(menGold_1972), 
	'in 1972,', len(menGold_2002), 'in 2002, and', len(menGold_2014), 'in 2014')

print('Canadian women gold medals:', len(womenGold_1924), 'in 1924,', len(womenGold_1948), 'in 1948,', len(womenGold_1972), 
	'in 1972,', len(womenGold_2002), 'in 2002, and', len(womenGold_2014), 'in 2014')




# Double bar graph visualization
plt.rcdefaults()

# Values of the bars
menMedals = (len(menGold_1924), len(menGold_1948), len(menGold_1972), len(menGold_2002), len(menGold_2014))

womenMedals = (len(womenGold_1924), len(womenGold_1948), len(womenGold_1972), len(womenGold_2002), len(womenGold_2014))

x_pos = np.arange(len(menMedals))  # The x locations for the groups
width = 0.35  # The width of the bars

# Creates the bars
fig, ax = plt.subplots()
menBar = ax.bar(x_pos - width/2, menMedals, width, color='royalblue', label='Men')
womenBar = ax.bar(x_pos + width/2, womenMedals, width, color='hotpink', label='Women')

# Sets labels and ticks
plt.ylabel('Number of Gold Medals', fontweight='bold')
plt.xlabel('Year', fontweight='bold')
plt.suptitle('Canadian Gold Medals: Men vs. Women', fontsize=16, fontweight='bold')
plt.title('(1924, 1948, 1972, 2002, 2014)')
ax.set_xticks(x_pos)
ax.set_xticklabels(('1924', '1948', '1972', '2002', '2014'))
plt.legend()

# Defines the bar height label and where it will be displayed
def autolabel(rects, xpos='center'):
    xpos = xpos.lower()
    ha = {'center': 'center'}
    offset = {'center': 0.5}

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.00*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')

# Labels the bars with their heights
autolabel(menBar, 'center')
autolabel(womenBar, 'center')

# Shows graph
plt.show()




# Line graph visualization
plt.rcdefaults()

x_pos = np.arange(len(menMedals))  # The x locations for the groups

# Draws Lines
fig, ax = plt.subplots()
plt.plot(menMedals, label='Men', color='royalblue', linewidth=2)
plt.plot(womenMedals, label='Women', color='hotpink', linewidth=2)

# Sets labels and ticks
plt.ylabel('Number of Gold Medals', fontweight='bold')
plt.xlabel('Year', fontweight='bold')
plt.suptitle('Canadian Gold Medals: Men vs. Women', fontsize=16, fontweight='bold')
plt.title('(1924, 1948, 1972, 2002, 2014)')
ax.set_xticks(x_pos)
ax.set_xticklabels(('1924', '1948', '1972', '2002', '2014'))
plt.legend()

# Shows graph
plt.show()
