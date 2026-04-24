# Mini-Project 3: PID Speed Controller Simulation

## Overview
This project implements a Proportional-Integral-Derivative (PID) controller to regulate the speed of a simulated DC motor.

## Objectives
* Implementation of a closed-loop control system.
* Dynamic parameter adjustment within a ROS 2 timer callback.
* Usage of `Float32` message types for real-time control commands.

## Formula
The control law implemented is:
$$u(t) = K_p e(t) + K_i \int e(t) dt + K_d \frac{de(t)}{dt}$$

## Usage
The node calculates the necessary command to reach a target speed of 100 units and publishes the simulated feedback to the `motor_command` topic.
