# IoT-Project
A simple IoT project for Software Engineering course (SKEL413) on a Agriculture Monitoring System using NodeMCU ESP8266 with Soil Moisture and LDR Sensor Module for data acquisition.
## Table of Contents

- [Stage 2: IoT Agriculture Monitoring System](#stage-2-iot-agriculture-monitoring-system)
  * [Problem Statement](#problem-statement)
    + [Use Case Description - Report and Notify Plant Condition](#use-case-description---report-and-notify-plant-condition)
  * [System Architecture](#system-architecture)
  * [Sensor](#sensor)
  * [Cloud Platform](#cloud-platform)
  * [Dashboard](#dashboard)
## Stage 2: IoT Agriculture Monitoring System

### Problem Statement

Food security has been listed in the 17 Sustainable Development Growth (17 SDGs) under 'Zero Hunger'. Agriculture is an important aspect of life as it could source an adequate foodstuff. It contributes to most of the world's food, one of the human's basic need of life. Hence, explains the importance of maintaining the quality of the crops. Cultivation of soil for the growth of crops has become the attention of all farmers. Frequent monitoring is required to ensure plants to grow healthily.

There are a few parameters that need to be monitored in growing a healthy crops which includes soil humidity and light intensity. A soil which is too humid could catalyst the growth of mold and bacteria that cause plants to wilt and become unhealthy whereas plants that does not receive enough lights will also become wilt and eventualy dies.

The intervention of Internet of Things (IoT) technology in agriculture could facilitate farmers in managing their crops by a proper schedule of plant monitoring. They need not to worry about the condition of their crops as the sensor will aid them to monitor the plants. The sensor senses the changes happen to the crops and immediately notify them for any changes occur and they can take action accordingly. This project will focus on the development of IoT-based agriculture monitoring system. 

[click here to return to the table of contents](#table-of-contents)

![Use Case Agriculture (3)](https://user-images.githubusercontent.com/117179191/211964029-1f989870-7ccc-443e-8366-bd63ddc81803.jpeg)

#### Use Case Description - Report and Notify Plant Condition

[click here to return to the table of contents](#table-of-contents)

| Elements | Description |
| ------- | ---------------|
| System | Farms or nursery |
| Use Case | Report and notify plant condition |
| Actors | Farms or nursery, Farmers |
| Data | Farms or nursery sends summary of collected data from the sensors such as soil humidity and light intensity |
| Stimulus | Farms (Sensor location) establish communication link with the user to send and update requested data |
| Response | The summarized data are sent and displayed to the user for data analysis and user may take action accordingly based on the analyzed data |
| Comments | The plant's conditions need to be monitored every day. |

### System Architecture

This section present an overview of the system architecture of IoT Agriculture Monitoring System. This project use NodeMCU ESP8266 to control, process and transmit moisture and light intensity data received from soil moisture and ldr sensor. NodeMCU will communicate using HTTP data protocol transmission to Flask Web Framework for data ingestion. Then, Flask will store the data to PythonAnywhere Web Hoisting platform and finally update to simple dashboard using Grafana Web Application.

[click here to return to the table of contents](#table-of-contents)
![system architecture](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/architechture-stage2-v5.png)

### Sensor
Propose data transmission protocol is **Hyper-Text-Transfer-Protocol (HTTP)**. Propose device for this project are:

| Devices | Function |
| ------- | ---------------|
| NodeMCU ESP8266 | Control, process and transmit data to web framework using HTTP data transmission |
| Soil Moisture Sensor | To check moisture level of soil |
| LDR Sensor Module | To detect change of light intensity with light dependent resistor |
| CD4051B Multiplexer  | Soil moisture and LDR sensor need to share ADC pin via multiplexer since NodeMCU 8266 has only one ADC pinout|
 
Code for NodeMCU ESP8266 using Arduino IDE
 
```

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// setup I/O sensor nodemcu---------------------------------
#define ldr_sensor A0
#define sm_sensor 5
// global variable------------------------------------------
int ms = 0;       //moisture percentage
int ldr = 0;       //light intensity
unsigned long lastTime = 0;
unsigned long timerDelay = 5000; //set timer to 5s
// WiFi detail----------------------------------------------
WiFiServer server(80);
const char* ssid = "insert SSID";
const char* password = "insert password";
String serverName = "http://mohdafiqazizi.pythonanywhere.com/sensor";
//----------------------------------------------------------

void wificlient(){
  WiFiClient client;
  HTTPClient http;
 
  http.begin(client, serverName); //Specify the URL
  String httpData = "&ms=" + String(ms) + "&ldr=" + String(ldr);
  
  int httpResponseCode = http.POST(); //post http request
  if (httpResponseCode > 0) { //Check for the returning code
    String payload = http.getString();
    Serial.println(httpResponseCode);
    Serial.println(payload);
    Serial.print("Moisture: ");Serial.println(ms);
    Serial.print("Light Intensity: ");Serial.print(ldr);Serial.println("%");
  }
  else {
    Serial.print("Error Code: ");
    Serial.println(httpResponseCode);
  }
  http.end(); //Free the resources
}

void setup(){
  Serial.begin(115200);
  // Setup pinmode-----------------------------
  pinMode(ldr_sensor, INPUT);
  pinMode(sm_sensor, INPUT);
  // Connect to WiFi network-------------------
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  // Start the server-------------------------
  server.begin();
  Serial.println("Server started");
  // Print the IP address---------------------
  Serial.print("Network IP Address: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
  //------------------------------------------
}

void loop(){
  // read input sensor-----------------------------------------------------------
  ms = digitalRead(ms_sensor);
  ldr = (analogRead(ldr_sensor)/1023)*100;
  // check WiFi connection-------------------------------------------------------
  if((millis() - lastTime) > timerDelay){
    if(WiFi.status() == WL_CONNECTED) wificlient();
    else Serial.println("WiFi Disconnected");
  }
  lastTime = millis();
  //-----------------------------------------------------------------------------
}

```
</details>

 [click here to return to the table of contents](#table-of-contents)
 
 ![image](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/hardware-diagram.png)
 ![image](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/nodemcu-pinout.png)

### Cloud Platform

This [video](https://youtu.be/_i5_W27mgAI) shows the result of integrated [PythonAnywhere Web Hosting](https://www.pythonanywhere.com/) with the [Flask Web Framework](https://flask.palletsprojects.com/en/2.2.x/) where the web-app link can be found [here](http://mohdafiqazizi.pythonanywhere.com/).

[click here to return to the table of contents](#table-of-contents)

### Dashboard
The prototype dashboard will developed using Grafana Web Application. The dashboard mainly focus on **Graphical-User-Interface (GUI)** approach consist element of:
- icon - small picture represent sub-application
- cursor - as interactive between GUI element
- menu - information or data group together and placed at visible place

[click here to return to the table of contents](#table-of-contents)
 
![Dashboard](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard.png)
