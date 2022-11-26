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
Propose data transmission protocol is **Hyper-Text-Transfer-Protocol (HTTP)**. Propose device for this project are:
 - NodeMCU ESP8266
 - Soil Moisture Sensor Module
 - LDR Sensor Module
 - CD4051B Multiplexer
 
 ![image](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/IMG_0133.jpg)
 
 <details>
  <summary>Code for NodeMCU ESP8266

```

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

//setting I/O sensor nodemcu
#define moisturepin A0
#define ldrpin A0
#define modepin 10

//WiFi detail
const char* ssid = "insert SSID";
const char* password = "insert password";
String serverName =  "http://api.circuits.my/request.php";

//global variable
float mp = 0;       //moisture percentage
float li = 0;       //light intensity
int sensormode = 0; //swap sensor

//setup wifi port - http
WiFiServer server(80);

void wificlient(){
  WiFiClient client;
  HTTPClient http;
  String api_key = "Put your API key";
  String device_id = "Put your device ID";
  String httpData = serverName + "?api=" + api_key + "&id=" + device_id + "&mp=" + String(mp) + "&li=" + String(li);
  http.begin(client, httpData); //Specify the URL
  int httpResponseCode = http.GET(); //Make the request
  if (httpResponseCode > 0) { //Check for the returning code
    String payload = http.getString();
    Serial.println(httpResponseCode);
    Serial.println(payload);
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
  pinMode(moisturepin, INPUT);
  pinMode(ldrpin, INPUT);
  pinMode(modepin, OUTPUT);
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
  
  sensormode = 0;
  mp = ( 100.00 - ( (analogRead(moisturepin)/1023.00) * 100.00 ) );
  Serial.print("Soil Moisture (%) = "); Serial.print(mp); Serial.println("%");
  delay(200);
  
  sensormode = 1;
  li = (analogRead(ldrpin)/1023.00) * 100.00 ;
  Serial.print("Light Intensity (%) = "); Serial.print(li); Serial.println("%");
  delay(200);

  if(WiFi.status() == WL_CONNECTED) wificlient();
  else Serial.println("WiFi Disconnected");
  delay(600);
}

```
</details>

### Cloud Platform
Backend Framework: Flask

Cloud Hosting Platform: Heroku

URL of our Flask App: https://weather-m3.herokuapp.com/

This is the [video](https://www.youtube.com/watch?v=0j9s8jk-LtA&ab_channel=MOHDHAFEEZSHAHRIL) of how we deploy Flask app to Heroku

### Dashboard
This is the prototype dashboard that we will be creating later using Google Data Studio. It will display the temperature, humidity and heat index and also simple data like date and day.

![Dashboard](https://i.ibb.co/LSsG0yz/dashboard.jpg)
