# IoT-Project
IoT project for course skel4213

Sensor      - ph sensor, soil moisture sensor, nodemcu esp8266

data ingest - Flask

storage     - heroku

Dashboard   - Grafana

problem statement - ammar

system architecture - afiq

sensor - ziyad

cloud plaform - ziyad

dashboard - ziyad


# IoTproject
A simple IoT project for Software Engineering course (SKEL413) on a weather monitoring system using M5stickC with soil moisture sensor and Ph sensor to obtain the related data

### Table of Contents

- [IoTproject](#iotproject)
    + [Table of Contents](#table-of-contents)
  * [IoT Weather Monitoring System (Milestone2)](#iot-weather-monitoring-system--milestone2-)
    + [Problem Statement](#problem-statement)
      - [Use Case Description - Notify crops condition](#use-case-description---report-weather)
    + [System Architecture](#system-architecture)
    + [Sensor](#sensor)
      - [Proposed Device: M5STICKC](#proposed-device--m5stickc)
      - [Proposed Data Transmission Protocol : HTTP](#proposed-data-transmission-protocol---http)
      - [Code Sample](#code-sample)
    + [Cloud Platform](#cloud-platform)
    + [Dashboard](#dashboard)
   
## IoT Agriculture Monitoring System (Stage 2)

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

#### Proposed Device: M5STICKC

![M5](https://images-na.ssl-images-amazon.com/images/I/51ykxk9ZYoL.jpg)

#### Proposed Data Transmission Protocol : HTTP

#### Code Sample

<details>
  <summary>Click to expand!</summary>

```

#include <WiFi.h>
#include "DHT.h"
#include <HTTPClient.h>
#define DHTPIN 26     // DHT sensor pin
float h = 0;
float t = 0;
// Replace with your network credentials
const char* ssid     = "YOUR SSID NAME";
const char* password = "YOUR NETWORK PASSWORD";

#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

// Set web server port number to 80
WiFiServer server(80);

// Variable to store the HTTP request
String header;

void setup() {
  Serial.begin(115200);
  pinMode(4,OUTPUT);
  pinMode(2,OUTPUT);
  dht.begin();
  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (isnan(h) || isnan(t)) {
    h = random(60,78);
    t = random(28,31);
  } else {
    h = dht.readHumidity();
    t = dht.readTemperature();
  }

  HTTPClient http;
  //send channel data with data reference name and data for example: temp=32
  //You can send multiple data separated by & for example: temp=32$hum=67
  //dont forget to include api(api key) and id (device id)
  
  //Example url for channel data and controllers data both can be requested at the same http request url
  //replace API_KEY and DEVICE_ID with your own at io.circuits.my 
  //any api request will be using api.circuits.my

  String api_key = "Put your API key";
  String device_id = "Put your device ID";

  //For display data only without control.

  HTTPClient http;
  String httpData = "http://api.circuits.my/request.php?api=" + api_key + "&id=" + device_id + "&temp=" + String(t) + "&hum=" + String(h);
  http.begin(httpData); //Specify the URL
  int httpResponsCode = http.GET(); //Make the request
  if (httpResponsCode > 0) { //Check for the returning code
    String payload = http.getString();
    Serial.println(httpResponsCode);
    Serial.println(payload);
  }

  else {
    Serial.println("Error on HTTP request");
  }
  http.end(); //Free the resources
  delay(3000);
}

```
</details>
  
<img src="https://i.ibb.co/1m4fcFt/Whats-App-Image-2021-12-15-at-20-33-40.jpg" alt="sample" width="400"/> 
  
### Cloud Platform

Backend Framework: Flask

Cloud Hosting Platform: Heroku

URL of our Flask App: https://weather-m3.herokuapp.com/

This is the [video](https://www.youtube.com/watch?v=0j9s8jk-LtA&ab_channel=MOHDHAFEEZSHAHRIL) of how we deploy Flask app to Heroku

### Dashboard

This is the prototype dashboard that we will be creating later using Google Data Studio. It will display the temperature, humidity and heat index and also simple data like date and day.

![Dashboard](https://i.ibb.co/LSsG0yz/dashboard.jpg)
