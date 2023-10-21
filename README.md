# HeaterPi Server
***A Raspberry Pi powered climate control app***

![Demo](https://github.com/ItsNotCam/HeaterPi-Client/assets/46014191/17f970e3-a996-4818-9caa-183e60251834)

**See the react app source code [here](https://github.com/ItsNotCam/HeaterPi-Client).**

## Overview
HeaterPi is a full-stack web application that allows users to remotely **control and monitor the temperature in a room** using a Raspberry Pi, a Phillips Hue Smart Plug, and a standard space heater. This application is built using **Python**, **TypeScript**, **ReactJS**, **Websockets**, and **REST**.

## Why
I currently (2023) am **renting a single room** in the bottom floor of a home. The **windows here are very thin** and do not seal properly, so it can get *very* cold during the winter - especially in the night and when sleeping. 

**I own a space heater**, but **leaving it on unattended when sleeping can be dangerous**. To solve this **I created HeaterPi**.

## Features
- **Temperature Sensor**: The Raspberry Pi collects real-time temperature data in the room to provide accurate information on the current temperature using the [DHT 11](https://components101.com/sensors/dht11-temperature-sensor#:~:text=use%20DHT11%20Sensors-,The%20DHT11%20is%20a%20commonly%20used%20Temperature%20and%20humidity%20sensor,to%20interface%20with%20other%20microcontrollers.) sensor.
- **Automated Climate Control**: Users can set a target temperature through a user-friendly web interface accessible from any device with a browser, and the application will autonomously maintain that room temperature in the real world.
- **WebSocket Communication**: Real-time communication between the web UI and the Raspberry Pi is achieved through WebSockets, ensuring realtime temperature readouts.

## Tech Stack
- **Python**: The Raspberry Pi communicates with the temperature sensor, listens on the web socket, hosts the http server, and controls the Philips Hue Smart Plug using Python.
- **ReactJS and TypeScript**: The frontend of the application is developed using ReactJS and Typescript
- **Asynchronous Websockets**: WebSockets are used to ensure efficient real-time communication between the frontend and the Raspberry Pi.

## What I Learned
Throughout work on this project I broadened my understanding of ReactJS, Typescript, and WebSockets. Additionally, I gained hands-on experience in leveraging Raspberry Pi for IoT applications in a real-world scenario.