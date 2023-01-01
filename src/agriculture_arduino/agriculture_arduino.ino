#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// setup -------------------------------------------------------
//#define ldr_sensor A0
//#define sm_sensor 5
#define serverName "https://agriculture-iot.onrender.com/"
#define api "rnd_YH6R9nJJMLeZKFDBSmiyScX36xAB"
#ifndef ssid
#define ssid "Mi 10T"
#define password "ziyadanas"
#endif
// global variable------------------------------------------
int sm = 0;       //moisture percentage
int ldr = 0;       //light intensity
unsigned long lastTime = 0;
unsigned long timerDelay = 5000; //set timer to 5s

void setup(){
  Serial.begin(115200);
  // Setup pinmode-----------------------------
  //pinMode(ldr_sensor, INPUT);
  //pinMode(sm_sensor, INPUT);
  // Connect to WiFi network--------------------
  Serial.println();
  Serial.println();
  Serial.println("[SETUP] Connecting to "+String(ssid));
  WiFi.begin(ssid, password);
  Serial.print("[SETUP] ");
  while (WiFi.status() != WL_CONNECTED) {delay(500);Serial.print(".");}
  Serial.println();
  Serial.println("[SETUP] WiFi connected");
  Serial.print("[SETUP] IP Address: ");
  Serial.println(WiFi.localIP());
  // -------------------------------------------
}

void loop(){
  // read input sensor-----------------------------------------------------------
  //sm = digitalRead(sm_sensor);
  sm = random(0,100);
  //ldr = (analogRead(ldr_sensor)/1023)*100;
  ldr = random(0,100);
  // check WiFi connection-------------------------------------------------------
  if((WiFi.status() == WL_CONNECTED)) httpclient();
  else Serial.println("[SETUP] WiFi Disconnected");
  delay(10000);
  //-----------------------------------------------------------------------------
}

void httpclient(){
  WiFiClient client;
  HTTPClient http;
 
  Serial.print("[HTTP] begin...\n");
  http.begin(client, serverName); //Specify the URL
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  
  String httpData = "api_key=rnd_YH6R9nJJMLeZKFDBSmiyScX36xAB&sm="+String(sm)+"&ldr="+String(ldr);
  Serial.print("[HTTP] POST...\n");
  int httpResponseCode = http.POST(httpData); //post http request
  if (httpResponseCode > 0) { //Check for the returning code
    String payload = http.getString();
    Serial.println("[HTTP] POST URL encode  : "+String(httpData));
    Serial.println("[HTTP] POST HTTP code   : "+String(httpResponseCode));
    Serial.println("[HTTP] Moisture         : "+String(sm)+"%");
    Serial.println("[HTTP] Light Intensity  : "+String(ldr)+"%");
    Serial.println("[HTTP]\n\n"+payload+"\n");
  }
  else {
    Serial.print("[HTTP] Error Code: "+String(httpResponseCode));
  }
  http.end(); //Free the resources
}