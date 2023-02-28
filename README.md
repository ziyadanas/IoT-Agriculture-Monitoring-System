<p align="center">
	<img src="https://chancellery.utm.my/wp-content/uploads/sites/21/2016/08/LOGO-UTM.png" height="120px"/>
	<h1 align="center">IoT Agriculture Monitoring System</h1>
</p>
A simple IoT project for Software Engineering course (SKEL413) on a Agriculture Monitoring System using NodeMCU ESP8266 with LDR Sensor Module for data acquisition.

## Table of Contents

- [Stage 2: Overview IoT Agriculture Monitoring System](#stage-2-overview-iot-agriculture-monitoring-system)
  * [Problem Statement](#problem-statement)
  * [System Architecture](#system-architecture)
  * [Sensor/Devices](#sensordevices)
  * [Cloud Platform](#cloud-platform)
  * [Dashboard](#dashboard)
- [Stage 3: RDBMS Design](#stage-3-rdbms-design)
  * [Database Configuration](#database-configuration)
  * [RDBMS Implementation](#rdbms-implementation)
- [Stage 4: Dashboard Implementation](#stage-4-dashboard-implementation)

## Stage 2: Overview IoT Agriculture Monitoring System

### Problem Statement

<div align="justify">
<p>Light intensity is a critical factor that affects plant growth, development, and yield in agriculture. The amount and quality of light that plants receive directly affect their photosynthesis and growth rates. Therefore, monitoring and controlling light intensity is crucial for optimizing crop production and ensuring high-quality yields.</p>

<p>However, traditional methods of monitoring light intensity in agriculture, such as manual observations, are time-consuming, labor-intensive, and prone to errors. In addition, farmers often lack the necessary expertise to interpret the data accurately, making it difficult to make informed decisions about crop management.</p>

<p>To address this issue, an IoT agriculture monitoring system is proposed that will monitor the light intensity of crops in real-time. The system will consist of farmers who will use the data to adjust crop management, an administrator who will manage system configuration, sensors that will collect and send data to a cloud server, and the cloud server itself, which will receive, process, and send data to a dashboard for visualization. The following use case diagram illustrates the different actors and their interactions with the IoT agriculture monitoring system</p>

</div>

![case diagram](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/case-diagram-v3.png)

<!--
### Use Case Description

| Elements | Description |
| ------- | ---------------|
| System | Farms or nursery |
| Use Case | Report and notify plant condition |
| Actors | Farmers, Sensor, Administrator, Cloud Server |
| Data | Farms or nursery sends summary of collected data from the sensors such as soil humidity and light intensity |
| Stimulus | Farms (Sensor location) establish communication link with the user to send and update requested data |
| Response | The summarized data are sent and displayed to the user for data analysis and user may take action accordingly based on the analyzed data |
| Comments | The plant's conditions need to be monitored every day. |
-->


### System Architecture

<div align="justify">
<p>The proposed IoT agriculture monitoring system architecture comprises three main components: sensor/devices, cloud platform, and dashboard. The sensor/devices component consists of a Nodemcu ESP8266 microcontroller and an LDR sensor module. The Nodemcu ESP8266 will be used to read the data from the LDR sensor module, which will measure the light intensity of the crops.</p>

<p>The data collected by the sensor/devices will be sent to the cloud platform, which will be hosted on the web using the render.com. The cloud platform will be responsible for receiving, processing, and storing the data collected by the sensor/devices. To facilitate this, the web framework Flask will be used to develop the backend of the system. The Flask backend will interact with a PostgreSQL database to store the data collected by the sensor/devices.</p>

<p>The dashboard will be used to visualize the data collected by the sensor/devices. Grafana will be used to develop the dashboard, which will be connected to the PostgreSQL database used by the cloud platform. The dashboard will enable farmers and administrators to view the light intensity data collected by the sensor/devices in real-time</p>
</div>

![system architecture](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/system-architecture.png)

### Sensor/Devices

+ The Nodemcu ESP8266 is used to collect data from sensors and transmit it wirelessly to a cloud server.
+ The LDR sensor module can be used to monitor the amount of light received by crops in real-time. 
+ The HTTPS protocol is used to provide secure data transfer between the Nodemcu ESP8266 and the cloud server.
+ Arduino source code can be obtained [here](https://github.com/SolaireAstora125/IoT-Project/blob/main/src/agriculture_(HTTPS)/agriculture_(HTTPS).ino)

<div align="center">
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/hardware-diagram-v5.png" alt="hardware diagram">
 </figure>
 <p></p>
</div>

### Cloud Platform

This [video](https://youtu.be/_i5_W27mgAI) shows the result of  web deployment on render.com using the flask backend where the web-app link can be found [here](https://agriculture-iot.onrender.com/).


### Dashboard
The following diagram illustrate the dashboard's wireframe as low-fidelity representation of the actual dashboard:

![Dashboard](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard.png)


## Stage 3: RDBMS Design

### Database configuration
+ Utilize PostgreSQL since render.com does not support SQL except PostgreSQL
+ The configuration of database can be found at [line 11-30](https://github.com/SolaireAstora125/IoT-Project/blob/main/app.py#:~:text=%23PostgreSQL%20DB%20config,%5D%20%3D%20False)
+ render.com does not support console access for free version. Thus, need to drop and create database manually through python source code at [line 47-56](https://github.com/SolaireAstora125/IoT-Project/blob/main/app.py#:~:text=%23%20Initialize%20DB%20manually,users%20table.%27)


### RDBMS implementation
- Data table is used to record reading of respective sensor in 1NF:
  * id - primary key for data table
  * sid - foreign key that connects to sensor table
  * tsp - record timestamp value
  * val - record sensor reading
- Sensor table is used to register a sensor into the system:
  * id - primary key for sensor table
  * nm - store name of the sensor
- Relationship between data and sensor table is one-to-one relationship
- The source code of RDBMS can be found at [line 34-46](https://github.com/SolaireAstora125/IoT-Project/blob/main/app.py#:~:text=%23%20Create%20DB%20with%201%2Dto%2D1,data%27%2C%20uselist%3DFalse)

<div align="center">
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/erd-diagram-v2.png" alt="ERD diagram">
 </figure>
</div>

## Stage 4: Dashboard Implementation

<div align="center">
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard-reading-graph.png" alt="dashboard 1">
 </figure>
 <p></p>
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard-table.png" alt="dashboard 2">
 </figure>
</div>
