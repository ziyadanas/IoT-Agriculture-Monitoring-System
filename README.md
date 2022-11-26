# IoT-Project
A simple IoT project for Software Engineering course (SKEL413) on a Agriculture Monitoring System using NodeMCU ESP8266 with Soil Moistures and PH Sensors for data acquisition.

Sensor      - ph sensor, soil moisture sensor, nodemcu esp8266

data ingest - Flask

storage     - heroku

Dashboard   - Grafana

problem statement - ammar

system architecture - afiq

sensor - ziyad

cloud plaform - ziyad

dashboard - ziyad

## Table of Contents
- [Stage 2: IoT Agriculture Monitoring System](#stage-2:-iot-agriculture-monitoring-system)
  * [Problem Statement](#problem-statement)
    + [Use Case Description - Report Weather](#use-case-description---report-weather)
  * [System Architecture](#system-architecture)
    + [Sub-sub-heading](#sub-sub-heading-1)
  * [Sensor](#sensor)
    + [Proposed Device: M5STICKC](#proposed-device--m5stickc)
    + [Proposed Data Transmission Protocol : HTTP](#proposed-data-transmission-protocol---http)
    + [Code Sample](#code-sample)
  * [Cloud Platform](#cloud-platform)
  * [Dashboard](#dashboard)
- [IoTproject](#iotproject)
    + [Table of Contents](#table-of-contents)
  * [IoT Agriculture Monitoring System (Milestone2)](#iot-agriculture-monitoring-system--milestone2-)
    + [Problem Statement](#problem-statement)
      - [Use Case Description - Report Weather](#use-case-description---report-weather)
    + [System Architecture](#system-architecture)
    + [Sensor](#sensor)
      - [Proposed Device: M5STICKC](#proposed-device--m5stickc)
      - [Proposed Data Transmission Protocol : HTTP](#proposed-data-transmission-protocol---http)
      - [Code Sample](#code-sample)
    + [Cloud Platform](#cloud-platform)
    + [Dashboard](#dashboard)  
## Stage 2: IoT Agriculture Monitoring System
### Problem Statement

Weather conditions have an impact on human activity, and weather monitoring can aid in activity control. It is critical to keep an eye on and monitor the weather patterns in the area. Users have limited access to weather information such as temperature, humidity, and heat index. Users will not be notified about  heat waves, or any other weather-related emergency if they do not have access to a weather station.

Furthermore, producing weather forecasts without data is challenging. When a person uses a weather station, they can also view the information's history. The trends in the measurements can be determined by the user. The user will be able to examine patterns more effectively as a result of this.

![Case Diagram](https://i.ibb.co/mt1dCW2/image1.jpg)

#### Use Case Description - Report Weather


|        | Description |
| ------- | ---------------|
| System | Weather Station |
| Use Case | Report Weather |
| Actors | Weather Station, User that retrieve information |
| Data | The weather station sends summary of weather data that has been collected from the sensors. The data will be covering on the temperature, humidity and heat index |
| Stimulus | The weather station establish communication link with the user to send requested transmission of the data |
| Response | The summarized data are sent to the user |
| Comments | Weather station usually asked to report once per hour but the frequency may differ from one station to another and may be modified in the future |

### System Architecture

Here are the general overview of the system architecture of our IoT weather monitoring system. For this project we will be using the M5STICKC for the device and it will be connected to DHT11 sensor to obtain temperature, humidity, and heat index data. The device will communicate using HTTP data protocol transmission for the data transmission and it will send the data to Heroku Cloud platform and finally update the data on our simple dashboard app which we will be using google web dashboard that we will create later.

![system architecture](https://i.ibb.co/RvBLGVK/Capture2.jpg)

### Sensor
#### Proposed Data Transmission Protocol : HTTP
#### Proposed Device: NodeMCU ESP8266

![M5](https://hackster.imgix.net/uploads/attachments/944050/node-mcu_nRId0HmElJ.jpg?auto=compress%2Cformat&w=1280&h=960&fit=max)


  
### Cloud Platform

Backend Framework: Flask

Cloud Hosting Platform: Heroku

URL of our Flask App: https://weather-m3.herokuapp.com/

This is the [video](https://www.youtube.com/watch?v=0j9s8jk-LtA&ab_channel=MOHDHAFEEZSHAHRIL) of how we deploy Flask app to Heroku

### Dashboard

This is the prototype dashboard that we will be creating later using Google Data Studio. It will display the temperature, humidity and heat index and also simple data like date and day.

![Dashboard](https://i.ibb.co/LSsG0yz/dashboard.jpg)
