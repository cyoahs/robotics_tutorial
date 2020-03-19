# Experiment #2 - Play Baseball

## Introduction

In this experiment, you are required to control the robot you built in Lab report #1. The robot is fixed on the table and you need to control the robot to grasp a baseball and throw it to a randomly given target position on the floor.

## General Information

### Robot

The robot must be realistic. You can not design a robot with changable link length or other unrealistic properties.

### Integrity

You can only write your control algorithms and commands in the simulation code and only control the specific motors on your robot. The code should be submitted along with the report. Do not try any methods to get higher scores in a dishonest way.

### Scoring

Automatic scoring is used in this experiment. Functions for automatic scoring is embedded in the given script. You can run your code and the script locally on your own computer and see the score for your control algorithm, but the final score is the average score for the results from our server. 
If large difference appears between the score from the server and your local results, please contact the T.A. and we can recheck the results.

### Grading

The final grade of one experiment depend both on the absolute score and the relative rank.

## Details

### Environment

#### Table and baseball

The detailed size of the table is shown in the fig below. The baseball is a sphere with a radius of 4 cm. The baseball is randomly placed in a limited square on the table. 

#### Robot

The base of robot should be fixed on the table at any position you like. The total length of your robot cannot be longer than 5 m.

#### Targets

4 targets will be given randomly in order of distance. The position will be $P(i) = [r_i \cos\theta_i, r_i \sin\theta_i, 0]$, where $r_i ~U(i, i+1), \theta_i ~U(-\pi/2, \pi/2), i=1,2,4,8$.

### Code

The `rsc` folder contains URDF files. The `src` folder contains python script and you should modify the `main.py` file, but you can also write other files and import them in the `main.py`. The `log` folder is used to contain score or other data from each experiment.

### Score

