# IoT-Project
A simple IoT project for Software Engineering course (SKEL413) on a Agriculture Monitoring System using NodeMCU ESP8266 with Soil Moisture and LDR Sensor Module for data acquisition.

Sensor      - ldr sensor module, soil moisture sensor, nodemcu esp8266

data ingest - Flask

storage     - heroku

Dashboard   - Grafana

problem statement - ammar

system architecture - afiq

sensor - ziyad

cloud plaform - ziyad

dashboard - ziyad
## Table of Contents

- [Stage 2: IoT Agriculture Monitoring System](#stage-2-iot-agriculture-monitoring-system)
  * [Problem Statement](#problem-statement)
  * [System Architecture](#system-architecture)
  * [Sensor](#sensor)
  * [Cloud Platform](#cloud-platform)
  * [Dashboard](#dashboard)
## Stage 2: IoT Agriculture Monitoring System

### Problem Statement

Food security has been listed in the 17 Sustainable Development Growth (17 SDGs) under 'Zero Hunger'. Agriculture is an important aspect of life as it could source an adequate foodstuff. It contributes to most of the world's food, one of the human's basic need of life. Hence, explains the importance of maintaining the quality of the crops. Cultivation of soil for the growth of crops has become the attention of all farmers. Frequent monitoring is required to ensure plants to grow healthily.

There are a few parameters that need to be monitored in growing a healthy crops which includes soil humidity and light intensity. A soil which is too humid could catalyst the growth of mold and bacteria that cause plants to wilt and become unhealthy whereas plants that does not receive enough lights will also become wilt and eventualy dies.

The intervention of Internet of Things (IoT) technology in agriculture could facilitate farmers in managing their crops by a proper schedule of plant monitoring. They need not to worry about the condition of their crops as the sensor will aid them to monitor the plants. The sensor senses the changes happen to the crops and immediately notify them for any changes occur and they can take action accordingly. This project will focus on the development of IoT-based agriculture monitoring system. 


![Use case diagram](https://user-images.githubusercontent.com/117179191/204078717-975225ce-d453-486c-a0b9-196c8b93746e.JPG)

#### Use Case Description - Report and Notify Plant Condition


|        | Description |
| ------- | ---------------|
| System | Farms or nursery |
| Use Case | Report and notify plant condition |
| Actors | Farms or nursery, Farmers |
| Data | Farms or nursery sends summary of collected data from the sensors such as soil humidity and acidity |
| Stimulus | Farms (Sensor location) establish communication link with the user to send and update requested data |
| Response | The summarized data are sent and displayed to the user for data analysis and user may take action accordingly based on the analyzed data |
| Comments | The plant's conditions need to be monitored every day. |

### System Architecture

Here are the general overview of the system architecture of our IoT weather monitoring system. For this project we will be using the M5STICKC for the device and it will be connected to DHT11 sensor to obtain temperature, humidity, and heat index data. The device will communicate using HTTP data protocol transmission for the data transmission and it will send the data to Heroku Cloud platform and finally update the data on our simple dashboard app which we will be using google web dashboard that we will create later.

![system architecture](https://i.ibb.co/RvBLGVK/Capture2.jpg)

### Sensor
Propose data transmission protocol is **Hyper-Text-Transfer-Protocol (HTTP)**. Propose device for this project are:
 - NodeMCU ESP8266
 - Soil Moisture Sensor Module
 - LDR Sensor Module

### Cloud Platform
Backend Framework: Flask

Cloud Hosting Platform: Heroku

URL of our Flask App: https://weather-m3.herokuapp.com/

This is the [video](https://www.youtube.com/watch?v=0j9s8jk-LtA&ab_channel=MOHDHAFEEZSHAHRIL) of how we deploy Flask app to Heroku

### Dashboard
This is the prototype dashboard that we will be creating later using Google Data Studio. It will display the temperature, humidity and heat index and also simple data like date and day.

![Dashboard](https://i.ibb.co/LSsG0yz/dashboard.jpg)
