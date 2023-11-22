# Traffic Simulator

## Overview

This project is a traffic simulator that aims to simulate the flow of traffic at an intersection. The simulation involves multiple cars moving in different lanes towards the intersection. The goal is to coordinate the movement of cars through the intersection without collisions, implementing traffic rules and prioritizing certain lanes.

## Features

- Each car is represented as a separate entity, and their movement is simulated using multiprocessing.
- Rules of priority are implemented to control the passage of cars through the intersection.
- The intersection is managed to coordinate the movement of cars and avoid collisions.
- Time of arrival, waiting, and departure at the intersection are modeled.
- The status of cars, movements at the intersection, and any potential race conditions are logged and displayed.

## Project Components

- **Cars:**
  - Each car is a separate entity moving towards the intersection.
  - Threads or processes represent individual cars.
  
- **Intersection**
  - The main entity responsible for managing and coordinating the passage of cars.
  - Implements a semaphore algorithm to control the flow of traffic.

- **Semaphore Algorithm**
  - Controls the passage of cars through the intersection.
  - Adjusts the green light duration based on the number of cars in the queue.
  - Supports dynamic priority based on certain conditions.

- **Monitoring and Reports**
  - Displays the status of cars, movements at the intersection, and potential race conditions.

## How to Run

1. Clone the repository to your local machine.

2. Ensure you have Python installed.

3. Run the main program using the command: python traffic_simulator.py.

4. Follow the on-screen prompts to start the simulation, view credits, or exit the program.

## Credits
   - [@Rendrick27](https://github.com/Rendrick27)
   - [@joao-ribeirooo](https://github.com/joao-ribeirooo)


