# RoboticArmSummer2018
A robotic arm featuring a neural network

This project is focused on 3 processes in the following order:
  1. Generating data points that calculate angles of a robotic arm's joint (servo position) from a target point
  2. Using those data points to train a neural network that models the given functions
  3. Making predictions from this network and moving the servos to that position
  
Each process is completed in a different language for the following reasons:
  1. To learn the syntax of each language
  2. Processing power of certain components that use each language (this reason will be explained later)
  3. Certain libraries are developed for each language.
  
The first process is written in Java. This is because of my familiarity with Java. Also, I can dive right into the calculations and learn more of the theory.

Process 2 is written in Python. Python is considered to be a language that can perform complex matrix operations efficiently.

Process 3 will be completed in C. This is for the Arduino Due controlling the arm's servos. Because of the limitations of computing power, training of the network is in Python.
