#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Arduino.h>
#include <WiFiClientSecureBearSSL.h>

// setup -------------------------------------------------------
//#define ldr_sensor A0
//#define sm_sensor 5
#define serverName "https://agriculture-iot.onrender.com/sensor"
#define api "Token c217ccce9190ef8cb800aff0235fdaee7f8ebcda"
#ifndef ssid
#define ssid "Mi 10T"
#define password "ziyadanas"
#endif
// global variable------------------------------------------
int sm = 0;       //moisture percentage
int ldr = 0;       //light intensity
unsigned long lastTime = 0;
unsigned long timerDelay = 5000; //set timer to 5s
ESP8266WiFiMulti WiFiMulti;

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
  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);
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
  if((WiFiMulti.run() == WL_CONNECTED)) httpsclient();
  else Serial.println("[SETUP] WiFi Disconnected");
  delay(10000);
  //-----------------------------------------------------------------------------
}

void httpsclient(){
  std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);
  client->setInsecure();
  //WiFiClient client;
  HTTPClient http;
  Serial.print("[HTTPS] begin...\n");

  if(http.begin(*client, serverName)){
    Serial.print("[HTTPS] POST...\n");
    //http.addHeader("Authorization", String(api));
    //http.addHeader("Host", "http://mohdafiqazizi.pythonanywhere.com");
    //http.addHeader("Content-Type", "application/json");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    //String httpData = "{\"sm\":\"12\",\"ldr\":\"98\"}";
    String httpData = "sm="+String(sm)+"&ldr="+String(ldr);
    int httpResponseCode = http.POST(httpData);
    if (httpResponseCode > 0) { //Check for the returning code
      Serial.println("[HTTPS] POST HTTP code   : "+String(httpResponseCode));
      Serial.println("[HTTPS] Moisture         : "+String(sm)+"%");
      Serial.println("[HTTPS] Light Intensity  : "+String(ldr)+"%");
      String payload = http.getString();Serial.println("[HTTPS]\n\n"+payload+"\n");
    }
    else {
      Serial.println("[HTTPS] Error Code: "+String(httpResponseCode));
    }
  }
  http.end(); //Free the resources
}