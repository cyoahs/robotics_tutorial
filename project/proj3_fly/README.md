# Experiment #3 - Fly! Fly! Fly!

## Introduction

In this experiment, you are requiered to control a UAV to cross a forest in a 2 dimensional plane. The UAV is subjected to random distributions. Thus you need automatic real time adjustment to make sure your UAV flies as you desired.

## General Information

### Integrity

You can only write your control algorithms and commands in the simulation code and only control the specific motors on your robot. The code should be submitted along with the report. Do not try any methods to get higher scores in a dishonest way.

### Scoring

Automatic scoring is used in this experiment. Functions for automatic scoring is embedded in the given script. You can run your code and the script locally on your own computer and see the score for your control algorithm, but the final score is the average score for the results from our server. 

If large difference appears between the score from the server and your local results, please contact the T.A. and we can recheck the results.

### Grading

The final grade of one experiment depend both on the absolute score and the relative rank.

## Details

### Environment

#### Dimension

This experiment is taken in a 2 dimensional plane. Thus the robot only have three degree of freedom: translation along x and z direction and rotation along y direction. The gravity is in -z direction.

#### Map

The map of the forest is given in a urdf file. The UAV starts from one side of the map and needs to reach the other side. A detailed illustration is given in the below figures.

#### Robot

The robot is given in a urdf file. Special treatments are taken to constraints the UAV into a 2 dimensional world. The base for the robot is a fixed base with zero mass. The real base of the robot is constraints to the fixed "world base" via two virtual links with three joints, that is, two prismatic joint for translation and one continuous joint for rotation. The mass and inertia of those virtual links can be ignored.

The exact size for the UAV with full collision is given in the figure below. The UAV has two sphere engines, one for each side. The engines can provide limited and noised force along the axes of symmetry.

The base of the UAV has a weight of 8 kg and a moment of inertia of 0.3 kg m^2 around the center of mass. Each engine has a weight of 1 kg and a moment of inertia of 0.1 kg m^2 around its own center of mass. Details can be found in the urdf file.

#### Control

The control is implemented by applying external force on the engines in their local frames. The signal contains a uniform distributed noise of 3%. The limitation of output force is 100 N for each engine. When the signal reaches over 100, the output will be 100 N with a uniform distributed noise of 6 N. (double noise for extreme conditions)

### Code

The `rsc` folder contains URDF files. The `src` folder contains python script and you should modify the files in this folder, but you can also write other files and import them. The `log` folder is used to contain score or other data from each experiment.

`Env.py` , `Helper.py` and `main.py` is used for basic setting for the task, do not modify them. `MapGenerator.py` is used to generate the urdf file for the map, it is no longer needed once you can find `forest.urdf` in `rsc` folder. `RobotControl.py` contains three functions that you can modify, but do not change the input and output for those function. The simulation is done with a timestep of 1/240 second.

`generateTraj()` function is called before actual control and returns a variable `plan`. This can be in any data sturcture you like. `realTimeControl()` takes the `robotId` and `plan` (just the one you get from `generateTraj()`) as input, and return a list of two float, representing the control singal for two engine. You can get the state for the robot and compare the current state to planned trajectory, and final calculate the control signal. Thus, you should make good use of the `plan` variable since it is prior information you can visit in real time control. `addDebugItems()` can be used for adding debug items. The input and output of this function can be modified as you need.

Eventually, you can run `main.py` to examine your control algorithm. In `main.py`, the control is performed in a loop. When the UAV finally contact with the final position, the loop breaks. Your have to create a `log` folder in the project folder (the folder in which you find this README) to ensure the logging functions.

### Score

The score depends on the total simulation time (number of time steps multiply timestep) and whether your UAV reaches the destination. Please submit at least one video and three text file recording your results along with your report.

