import plotly.express as px
from die import Die

# Create an instance of the class Die()
die_1 = Die()
die_2 = Die()
die_3 = Die()
# Makes some rolls, and store results in a list.
results = []
for roll_num in range(100_000):
    results.append(die_1.roll() + die_2.roll())
# print(results)

frequencies = []
poss_results = range(1, die_1.num_sides + die_2.num_sides + 1)
poss_res_list = []

for i in poss_results:
    poss_res_list.append(i)
# print(poss_res_list)

for value in poss_results:
    frequencies.append(results.count(value))
# print(frequencies)

# Visualize the results.
title = 'Results of Rolling a D6 and a D10 50,000 Times"'
labels = {'x': 'Result', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) 

# Customize axis on chart.
fig.update_layout(xaxis_dtick=1)
fig.show()
