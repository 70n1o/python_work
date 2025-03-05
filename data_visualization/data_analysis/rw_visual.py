"""Plotting the Random Walk."""

#import matplotlib.pyplot as plt
#
#from random_walk import RandomWalk
#
##Make a random walk.
#rw = RandomWalk()
#rw.fill_walk()
#
##Plot the points in walk.
#plt.style.use('classic')
#fig, ax = plt.subplots()
#ax.scatter(rw.x_values, rw.y_values, s=15)
#plt.show()


"""Generating Multiple Random Walks."""

#import matplotlib.pyplot as plt
#
#from random_walk import RandomWalk
#
##Keep making new walks, as long as the program is active.
#
#while True:
#    #Make a random walk.
#    rw = RandomWalk()
#    rw.fill_walk()
#
#    #Plot the points in walk.
#    plt.style.use('classic')
#    fig, ax = plt.subplots()
#
#    #Styling the Walk
#    point_numbers = range(rw.num_points)
#
#    #Coloring the Points
#    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#                edgecolors='none', s=15)
#    plt.show()
#
#    keep_running = input("Make another walk? (y/n): ")
#    if keep_running == 'n':
#        break


"""Plotting the Starting and Ending Points."""

#import matplotlib.pyplot as plt
#
#from random_walk import RandomWalk
#
##Keep making new walks, as long as the program is active.
#
#while True:
#    #Make a random walk.
#    rw = RandomWalk()
#    rw.fill_walk()
#
#    #Plot the points in walk.
#    plt.style.use('classic')
#    fig, ax = plt.subplots()
#    point_numbers = range(rw.num_points)
#    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#                edgecolors='none', s=15)
#
#    #Emphasize the first and last points.
#    ax.scatter(0, 0, c='green', edgecolors='none', s=100) #starting point
#    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) #ending point
#    plt.show()
#
#    keep_running = input("Make another walk? (y/n): ")
#    if keep_running == 'n':
#        break


"""Cleaning Up the Axes(x&y)."""


#import matplotlib.pyplot as plt
#
#from random_walk import RandomWalk
#
##Keep making new walks, as long as the program is active.
#
#while True:
#    #Make a random walk.
#    rw = RandomWalk()
#    rw.fill_walk()
#
#    #Plot the points in walk.
#    plt.style.use('classic')
#    fig, ax = plt.subplots()
#    point_numbers = range(rw.num_points)
#    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#                edgecolors='none', s=15)
#
#    #Emphasize the first and last points.
#    ax.scatter(0, 0, c='green', edgecolors='none', s=100) #starting point
#    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) #ending point
#    
#    #Removing the axes
#    ax.get_xaxis().set_visible(False)
#    ax.get_yaxis().set_visible(False)
#
#    plt.show()
#
#    keep_running = input("Make another walk? (y/n): ")
#    if keep_running == 'n':
#        break



"""Adding Plot Points."""


import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walks, as long as the program is active.

while True:
    #Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Plot the points in walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1)

    #Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100) #starting point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) #ending point
    
    #Removing the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break