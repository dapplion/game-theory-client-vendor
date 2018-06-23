# game-theory-client-vendor

This code is a small experiment to test a game theory problem described in this video https://youtu.be/jILgxeNBK_8

The main question to ask is, 
> why do competitor bussiness tend to be together in the same geographicall position?

### Methods

This code gives n vendors the chance to steal competitor's clients. On each step they attempt a finite number of random moves and only execute the one that results in getting more costumers. 

### Two vendors demo
This is the case discussed in the video referenced above. The simulation shows that equilibrium is reached when they are together back to back at the center of the area.

<p align="center">
  <img width="500" src="docs/demo-2vendors.gif">
</p>

The cited video above explains the concept perfectly. What you saw in the simulation is a Nash equilibrium, where vendors can't improve their positions without deviating from their current strategy

<p align="center">
  <img width="500" src="docs/video-intro.gif">
</p>

### Four vendors demo

With more vendors things get more interesting. With exactly 4 vendors, they tend to pair and split the area evenly.

<p align="center">
  <img width="500" src="docs/demo-4vendors.gif">
</p>
