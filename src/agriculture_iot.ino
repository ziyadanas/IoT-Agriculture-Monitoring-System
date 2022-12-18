#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// setup I/O sensor nodemcu---------------------------------
#define ldr_sensor A0
#define sm_sensor 5
// global variable------------------------------------------
int sm = 0;       //moisture percentage
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
  String httpData = "&sm=" + String(sm) + "&ldr=" + String(ldr);
  
  int httpResponseCode = http.POST(httpData); //post http request
  if (httpResponseCode > 0) { //Check for the returning code
    String payload = http.getString();
    Serial.println(httpResponseCode);
    Serial.println(payload);
    Serial.print("Moisture: ");
    Serial.println(sm);
    Serial.print("Light Intensity: ");
    Serial.print(ldr);
    Serial.println("%");
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
  sm = digitalRead(sm_sensor);
  ldr = (analogRead(ldr_sensor)/1023)*100;
  // check WiFi connection-------------------------------------------------------
  if((millis() - lastTime) > timerDelay){
    if(WiFi.status() == WL_CONNECTED) wificlient();
    else Serial.println("WiFi Disconnected");
  }
  lastTime = millis();
  //-----------------------------------------------------------------------------
}