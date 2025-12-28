# Remote-Control Line-Following Robot

## Overview
This project focused on the design and implementation of a mobile robot capable of both
**remote-controlled driving** and **autonomous line following**. The system was developed to
demonstrate fundamental robotics control concepts, including **proportional control** and
**finite state machines**, applied to real sensor data and motor actuation.

The robot was programmed in **Python** and designed to switch cleanly between operating modes
while maintaining stable, predictable behavior during autonomous motion.

> **Note:** Full source code and implementation details are available in the repository
> for deeper technical review.

---

## System Overview
The robot uses onboard sensors to detect a line on the ground and adjusts motor output in
real time to remain centered on the path. Control logic was structured around two core ideas:
continuous feedback control for steering and discrete state-based logic for mode selection.

The system supports:
- Manual remote control
- Autonomous line following
- Clean transitions between operating modes

---

## System Demonstration

The image below shows the robot operating during autonomous line-following mode, highlighting
real-time sensor feedback and proportional steering correction.

![Line-following robot in action](Image-LineFollowingRobot.png)

*Robot autonomously tracking a line using proportional control.*

> **Note:** Additional implementation details and source code can be found in the repository
> for those interested in a deeper technical breakdown.

---

## Control Strategy

### Proportional Control
Autonomous line following was implemented using **proportional control**. Sensor readings
were used to calculate an error value representing the robot’s deviation from the line center.
This error was multiplied by a proportional gain to dynamically adjust motor speeds and correct
the robot’s trajectory.

Key aspects of the proportional controller include:
- Continuous feedback from line sensors
- Real-time adjustment of motor output
- Reduced oscillation through gain tuning
- Smooth and responsive steering behavior

---

### Finite State Machine
A **finite state machine** was used to manage the robot’s operating modes and behavior.
Each state encapsulated a distinct control logic pathway, improving readability, reliability,
and expandability of the Python code.

Primary states included:
- **Remote Control Mode** – manual driving via user input
- **Line-Following Mode** – autonomous navigation using proportional control
- **Idle and Transition States** – safe switching between modes

Using a finite state machine ensured that only the appropriate control logic executed at any
given time and prevented conflicts between manual and autonomous behaviors.

---

## Design Highlights
- Dual-mode operation (manual and autonomous)
- Proportional control for smooth line tracking
- Finite state machine for structured control logic
- Real-time sensor feedback and motor adjustment
- Emphasis on stability, clarity, and modular Python code design

---

## My Role
- Designed and implemented the proportional control algorithm for line following in Python
- Tuned control gains to minimize oscillation and improve tracking accuracy
- Designed and implemented the finite state machine for mode management
- Mapped manual control inputs to **W, A, S, and D key bindings**, enabling grid-based movement
  and precise user-directed navigation during remote-controlled operation
- Integrated sensor feedback with motor control logic
- Tested and refined system performance through iterative trials

---

## Tools & Technologies
- Python
- Robotics control systems
- Proportional control
- Finite state machines
- Sensor-based feedback control
- Embedded programming
