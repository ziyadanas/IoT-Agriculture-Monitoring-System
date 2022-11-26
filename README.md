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
    + [Use Case Description - Report Weather](#use-case-description---report-weather)
  * [System Architecture](#system-architecture)
  * [Sensor](#sensor)
    + [NodeMCU ESP8266](#nodemcu-esp8266)
    + [LDR Sensor Module](#ldr-sensor-module)
    + [Soil Moisture Sensor Module](#soil-moisture-sensor-module)
    + [Hyper-Text-Transfer-Protocol (HTTP)](#hyper-text-transfer-protocol-http)
  * [Cloud Platform](#cloud-platform)
    + [Sub-sub-heading](#sub-sub-heading-2)
  * [Dashboard](#dashboard) 
## Stage 2: IoT Agriculture Monitoring System

### Problem Statement

Agriculture is one of the important aspect of life. It contributes to most of the world's food, one of the human's basic need of life. Hence, explains the importance of maintaining the quality of the crops. Cultivation of soil for the growth of crops has become the attention of all farmers. Frequent monitoring is required to ensure a healthy growth of plants.

There are a few parameters that need to be monitored which includes soil humidity and soil acidity. A soil which is too humid could catalyst the growth of mold and bacteria that cause plants to become wilt and unhealthy. 


![Case Diagram](https://i.ibb.co/mt1dCW2/image1.jpg)

#### Use Case Description - Report Weather


|        | Description |
| ------- | ---------------|
| System | Farms or nursery |
| Use Case | Notify plant condition |
| Actors | Farms or nursery, Farmers |
| Data | Farms or nursery sends summary of collected data from the sensors such as soil humidity and acidity |
| Stimulus | Farms (Sensor location) establish communication link with the user to send and update requested data |
| Response | The summarized data are sent and displayed to the user for data analysis and to take action accordingly |
| Comments | Weather station usually asked to report once per hour but the frequency may differ from one station to another and may be modified in the future |

### System Architecture

Here are the general overview of the system architecture of our IoT weather monitoring system. For this project we will be using the M5STICKC for the device and it will be connected to DHT11 sensor to obtain temperature, humidity, and heat index data. The device will communicate using HTTP data protocol transmission for the data transmission and it will send the data to Heroku Cloud platform and finally update the data on our simple dashboard app which we will be using google web dashboard that we will create later.

![system architecture](https://i.ibb.co/RvBLGVK/Capture2.jpg)

### Sensor

#### NodeMCU ESP8266

![M5](https://images-na.ssl-images-amazon.com/images/I/51ykxk9ZYoL.jpg)

#### LDR Sensor Module
#### Soil Moisture Sensor Module
#### Hyper-Text-Transfer-Protocol (HTTP)
### Cloud Platform

Backend Framework: Flask

Cloud Hosting Platform: Heroku

URL of our Flask App: https://weather-m3.herokuapp.com/

This is the [video](https://www.youtube.com/watch?v=0j9s8jk-LtA&ab_channel=MOHDHAFEEZSHAHRIL) of how we deploy Flask app to Heroku

### Dashboard

This is the prototype dashboard that we will be creating later using Google Data Studio. It will display the temperature, humidity and heat index and also simple data like date and day.

![Dashboard](https://i.ibb.co/LSsG0yz/dashboard.jpg)
