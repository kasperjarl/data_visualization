import plotly.express as px
from die import Die

# Create an instance of the class Die()
die = Die()

# Makes some rolls, and store results in a list.
results = []
for roll_num in range(1_000):
    results.append(die.roll() + die.roll())
# print(results)

frequencies = []
poss_results = range(1, die.num_sides * 2 +1)
poss_res_list = []

for i in poss_results:
    poss_res_list.append(i)
print(poss_res_list)

for value in poss_results:
    frequencies.append(results.count(value))
print(frequencies)

# Visualize the results.
title = 'Results of Rolling Two D6 1,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) 
fig.show()
