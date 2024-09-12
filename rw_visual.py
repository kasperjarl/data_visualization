import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active

while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=2)
    ax.set_aspect('equal')

    # Emphasize the first and last points
    ax.plot(rw.x_values[0], rw.y_values[0], 'go', markersize=5, markeredgewidth=5, markeredgecolor= 'g')
    ax.plot(rw.x_values[-1], rw.y_values[-1], 'ro',markersize=5, markeredgewidth=5, markeredgecolor='r')

    # Remove the axes. 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Show the visual
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break