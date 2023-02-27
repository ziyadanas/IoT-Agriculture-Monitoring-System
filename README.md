<p align="center">
	<img src="https://chancellery.utm.my/wp-content/uploads/sites/21/2016/08/LOGO-UTM.png" height="120px"/>
	<h1 align="center">IoT Agriculture Monitoring System</h1>
</p>
A simple IoT project for Software Engineering course (SKEL413) on a Agriculture Monitoring System using NodeMCU ESP8266 with LDR Sensor Module for data acquisition.

<!--
## Table of Contents

- [Stage 2: Overview IoT Agriculture Monitoring System](#stage-2-overview-iot-agriculture-monitoring-system)
  * [Problem Statement](#problem-statement)
  * [Use Case Diagram](#use-case-diagram)
  * [System Architecture](#system-architecture)
  * [Sensor](#sensor)
  * [Cloud Platform](#cloud-platform)
  * [Dashboard](#dashboard)
- [Stage 3: RDBMS Design](#stage-3-rdbms-design)
- [Stage 4: Dashboard Design](#stage-4-dashboard-design)
-->

## Stage 2: Overview IoT Agriculture Monitoring System

### Problem Statement

<div align="justify">
<p>Food security has been listed in the 17 Sustainable Development Growth (17 SDGs) under 'Zero Hunger'. Agriculture is an important aspect of life as it could source an adequate foodstuff. It contributes to most of the world's food, one of the human's basic need of life. Hence, explains the importance of maintaining the quality of the crops. Cultivation of soil for the growth of crops has become the attention of all farmers. Frequent monitoring is required to ensure plants to grow healthily.</p>

<p>There are a few parameters that need to be monitored in growing a healthy crops which includes soil humidity and light intensity. A soil which is too humid could catalyst the growth of mold and bacteria that cause plants to wilt and become unhealthy whereas plants that does not receive enough lights will also become wilt and eventualy dies.</p>

<p>The intervention of Internet of Things (IoT) technology in agriculture could facilitate farmers in managing their crops by a proper schedule of plant monitoring. They need not to worry about the condition of their crops as the sensor will aid them to monitor the plants. The sensor senses the changes happen to the crops and immediately notify them for any changes occur and they can take action accordingly. This project will focus on the development of IoT-based agriculture monitoring system.</p>
</div>

### Use Case Diagram
The following use case diagram illustrates the different actors and their interactions with the IoT agriculture monitoring system:
![case diagram](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/case-diagram-v4.png)

### Use Case Requirement

<!--
| Elements | Description |
| ------- | ---------------|
| System | Farms or nursery |
| Use Case | Report and notify plant condition |
| Actors | Farms or nursery, Farmers |
| Data | Farms or nursery sends summary of collected data from the sensors such as soil humidity and light intensity |
| Stimulus | Farms (Sensor location) establish communication link with the user to send and update requested data |
| Response | The summarized data are sent and displayed to the user for data analysis and user may take action accordingly based on the analyzed data |
| Comments | The plant's conditions need to be monitored every day. |
-->

### System Architecture

<div align="justify">
<p>This section present an overview of the system architecture of IoT Agriculture Monitoring System. This project use NodeMCU ESP8266 to control, process and transmit moisture and light intensity data received from soil moisture and ldr sensor. NodeMCU will communicate using HTTP data protocol transmission to Flask Web Framework for data ingestion. Then, Flask will store the data to PythonAnywhere Web Hoisting platform and finally update to simple dashboard using Grafana Web Application.</p>
</div>

![system architecture](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/software-architecture.png)

### Sensor

+ The Nodemcu ESP8266 is used to collect data from sensors and transmit it wirelessly to a cloud server.
+ The LDR sensor module can be used to monitor the amount of light received by crops in real-time. 
+ The HTTPS protocol is used to provide secure data transfer between the Nodemcu ESP8266 and the cloud server.
+ Arduino source code can be obtained [here](https://github.com/SolaireAstora125/IoT-Project/blob/main/src/agriculture_(HTTPS)/agriculture_(HTTPS).ino)

<div align="center">
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/hardware-diagram-v2.png" alt="hardware diagram">
  <figcaption>Figure 3 - Hardware Diagram for Sensor</figcaption>
 </figure>
 <p></p>
<!--
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/nodemcu-pinout.png" alt="nodemcu pinout">
  <figcaption>Figure 4 - Pinout for Nodemcu ESP8266</figcaption>
 </figure>
-->
</div>

### Cloud Platform

This [video](https://youtu.be/_i5_W27mgAI) shows the result of integrated [PythonAnywhere Web Hosting](https://www.pythonanywhere.com/) with the [Flask Web Framework](https://flask.palletsprojects.com/en/2.2.x/) where the web-app link can be found [here](http://mohdafiqazizi.pythonanywhere.com/).


### Dashboard
The prototype dashboard will developed using Grafana Web Application. The dashboard mainly focus on **Graphical-User-Interface (GUI)** approach consist element of:
- icon - small picture represent sub-application
- cursor - as interactive between GUI element
- menu - information or data group together and placed at visible place

<!-- 
![Dashboard](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard.png)
-->

## Stage 3: RDBMS Design

### Database configuration
+ Utilize PostgreSQL since render.com does not support other SQL other than PostgreSQL
+ The configuration of database can be found at [line 11-30](https://github.com/SolaireAstora125/IoT-Project/blob/main/app.py#:~:text=%23PostgreSQL%20DB%20config,%5D%20%3D%20False)
+ the details of database configuration can be obtained in info section of PostgreSQL in Render.com
+ render.com does not support console access for free version. Thus, need to drop and create database manually through python source code at [line 47-56](https://github.com/SolaireAstora125/IoT-Project/blob/main/app.py#:~:text=%23%20Initialize%20DB%20manually,users%20table.%27)


### RDBMS implementation
+ describe what is the purpose of each table
+ describe what variable in each table represent
+ describe relationship between table
+ The source code of RDBMS can be found at [line 34-46](https://github.com/SolaireAstora125/IoT-Project/blob/main/app.py#:~:text=%23%20Create%20DB%20with%201%2Dto%2D1,data%27%2C%20uselist%3DFalse)

<div align="center">
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/erd-diagram.png" alt="ERD diagram">
  <figcaption>Figure 7 - ERD Diagram for IoT Agriculture Monitoring System</figcaption>
 </figure>
</div>

## Stage 4: Dashboard Design

<div align="center">
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard-reading-graph.png" alt="dashboard 1">
  <figcaption>Figure 8 - Dashboard displaying sensor reading in meter and graph form</figcaption>
 </figure>
 <p></p>
 <figure>
  <img src="https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard-table.png" alt="dashboard 2">
  <figcaption>Figure 9 - Dashboard displaying sensor reading in table form</figcaption>
 </figure>
</div>
