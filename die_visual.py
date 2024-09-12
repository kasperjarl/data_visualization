import plotly.express as px
from die import Die


die = Die()

# Makes some rolls, and store results in a list.
results = []
for roll_num in range(1_000):
    results.append(die.roll())
# print(results)

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequencies.append(results.count(value))
# print(frequencies)

# Visualize the results.
title = 'Results of Rolling One D6 1,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) 
fig.show()
