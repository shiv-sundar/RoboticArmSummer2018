# RoboticArmSummer2018
A robotic arm featuring a neural network

The primary purpose of this project is to demonstrate my understanding of graduate level concepts such as inverse kinematics and artificial intelligence. 

Secondly, this is to share with anyone interested my process for completing the task of creating an artificially intelligent robotic arm, which follows: 

  1. Generate training data sets that take various inputs and create the required outputs.
  2. Train multiple neural networks to model inverse kinematic functions.
  3. Implement the trained network in the microcontroller (Arduino Due).
  
Process 1 is written in Java because of my familiarity with it and so can spend more time understanding the theory behind the calculations.

Process 2 is written in Python because of its frequent use in these applications and for its efficiency in performing complex matrix calculations.

Process 3 is written in Arduino (a C/C++ based language) for the simple reason that Arduino is the language for controlling the Due. Also, the Due does not have enough processing power to train the network in a reasonable amount of time.
