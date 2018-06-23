import random
import math
import numpy as np
import matplotlib.pyplot as plt
import copy
import time

# This code is a small experiment to test a game theory
# problem described in this video https://youtu.be/jILgxeNBK_8

# The main question to ask is, why do competitor bussiness 
# tend to be together in the same geographicall position?
# This code gives vendors the chance to steal competitor's
# clients and proves that with two vendors they only reach
# equilibrium when they are together at the center of the area

# With more vendors things get more interesting. With exactly
# 4 vendors, they tend to pair and split the area evenly

# =============================
# User defined parameters
# =============================

# Number of clients and vendors
vendorsNum = 4 
clientsNum = 100 * vendorsNum # Recommend for smoothness

# Define the size of the area to simulate
width = 2
height = 1

# At every move the vendor will attempt x move (int defined below) 
# and choose the most beneficial
attempts = 10

# Maximum distance to move, keep it low for a smooth simulation
dxMax = 0.1*(width+height)/2 # Recommend for smoothness

# =============================
# Helper functions
# =============================

# Create a postion array [x,y] within boundaries
def initPosition():
  return [random.uniform(0,width), random.uniform(0,height)]

# Generate a random direction and size vector
def generateVector():
	dx = dxMax*random.uniform(0, 1)
	return [dx*random.uniform(-1, 1), dx*random.uniform(-1, 1)]

# Compute the distance between two points [x,y]
def distance(p1,p2):
	return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

# Move a point with a vector
def move(p, v):
	p[0] += v[0]
	p[1] += v[1]

# Compute an array of length vendors.length with 
# how many clients belong to a vendor. 
# It assumes a client will always go to the closest vendor
def computeRes(vendors):
	res = []
	for i in range(vendorsNum):
		res.append(0)
	for client in clients:
		score = []
		for vendor in vendors:
			score.append(distance(vendor, client))
		res[np.argmin(score)] += 1
	return res

# Compute a step of the vendor i
# It will check the new score of n random moves and execute
# the one that results in the greter score. It will always move
def step(i):
	options = []
	vectors = []
	for j in range(attempts):
		newVendors = copy.deepcopy(vendors)
		vector = generateVector()
		move(newVendors[i], vector)
		# Store results
		options.append(computeRes(newVendors)[i])
		vectors.append(vector)
	bestVector = vectors[np.argmax(options)]
	move(vendors[i], bestVector)

# Plot a scatter adding tags for vendors
def singlePlot(ax, arr, color, tag):
	# Plot clients
	x = []
	y = []
	for e in arr:
		x.append(e[0])
		y.append(e[1])
	ax.scatter(x, y, color=color)
	if tag:
		for i, txt in enumerate(x):
			ax.annotate(str(i), (x[i],y[i]))

# Execute plots and add the vendors' score
def plot(res):
	fig, ax = plt.subplots()
	singlePlot(ax, clients, 'blue', False)
	singlePlot(ax, vendors, 'red', True)
	text = ''
	for i,e in enumerate(res):
		text += "{}: {}, ".format(i,e)
	ax.text(0.05, 1.08, text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
	
# =============================
# Simulation start
# =============================

# Initialize arrays
clients = []
vendors = []

# Initialize vendors
for i in range(vendorsNum):
	vendors.append(initPosition())

# Initialize clients
for i in range(clientsNum):
	clients.append(initPosition())

# Start simulation
for k in range(1000):
	for i in range(vendorsNum):
		step(i)
	res = computeRes(vendors)
	plot(res)
	plt.pause(0.01)
	plt.close()
plt.draw()


