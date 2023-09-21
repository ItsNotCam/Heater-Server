
<div align="center">

# Raspberry Pi Room Temperature Control Application

[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/cameron-young-37b173129/)
&nbsp;
[![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/ItsNotCam)
</div>

<img src="docs/Demo.gif">

## Overview

The Raspberry Pi Room Temperature Control Application is a full-stack web application that allows users to remotely control and monitor the temperature in a room using a Raspberry Pi, while ensuring safety through the control of a heater via a Philips Hue Smart Plug. This application is built using Python, TypeScript, ReactJS, Node.js, asynchronous Websockets, and REST requests.


## Features

- **Temperature Sensing**: The Raspberry Pi collects real-time temperature data in the room to provide accurate information on the current temperature.

- **Remote Control**: Users can set a target temperature through a user-friendly web interface accessible from any device with a browser.

- **WebSocket Communication**: Real-time communication between the web UI and the Raspberry Pi is achieved through WebSockets, ensuring seamless updates and responsiveness.

## Tech Stack

- **Python**: The Raspberry Pi communicates with the temperature sensor, listens on the web socket, and controls the Philips Hue Smart Plug using Python.

- **ReactJS and TypeScript**: The frontend of the application is developed using ReactJS and Typescript to provide users and developers with the best experience possible

- **Asynchronous Websockets**: Asynchronous WebSockets ensure efficient real-time communication between the frontend and the Raspberry Pi.

## What I Learned
Through my project, I developed proficiency in ReactJS, Typescript, and WebSockets in order to create this responsive web application with real-time communication capabilities. Additionally, I gained hands-on experience in leveraging Raspberry Pi for IoT applications, enabling interactive real-world interactions with physical devices.

## Requirements


- A [Raspberry Pi](https://www.raspberrypi.com)

- A [Phillips Hue Smart Plug](https://www.philips-hue.com/en-us/p/hue-smart-plug/046677552343)

- Python 3.x installed on your Raspberry Pi.

- Node.js and npm (Node Package Manager) installed on your Raspberry Pi.

- A [DHT11 temperature sensor](https://www.amazon.com/Temperature-Humidity-Digital-3-3V-5V-Raspberry/dp/B07WT2HJ4F/ref=sr_1_5?keywords=dht11&qid=1695258164&sr=8-5)
