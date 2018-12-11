#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  0.1.0
@author: gy18qz (Zhao Qianchen)
This model is run from a GUI in which there is a run menu.
When you run this code it is expected that a window will appear on your 
computer screen. To run the model, find this window and select run from the
menu bar.
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import matplotlib.backends.backend_tkagg
import agentframework
import csv 
import tkinter
import requests
import bs4
"""
Step 1: Initialise parameters.
"""
print("Step 1: Initialise parameters.")
# Make the parameters

num_of_agents = 20
num_of_iterations = 1000
agents = []
neighbourhood = 10
"""
Step 2: Plot environment.
"""
print("Step 2: Plot environment.")
# Setup plot

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Create environment from file
environment = []
f = open('in.txt')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()
"""
Step 3: Initialise agents.
"""
print("Step 3: Initialise agents.")
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
 
"""
Step 4: Animate acting agents.
"""
print("Step 4: Animate acting agents.")    
def update(frame_number):
    
    fig.clear()   
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    # Move the agents, eat, and share
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    # Plot the environment
    matplotlib.pyplot.imshow(environment)

# Animate acting agents

    for i in range(num_of_agents):
       matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat=False, frames=num_of_iterations)
    canvas.show()
"""
Step 5: Initialise GUI main window.
"""
print("Step 5: Initialise GUI main window.")
root = tkinter.Tk()   		# Main window.
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()		# Wait for interactions.