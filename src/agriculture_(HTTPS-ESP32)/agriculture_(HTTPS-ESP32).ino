#include <WiFiClientSecure.h>
#include <ssl_client.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>

WiFiMulti wifiMulti;
// setup -------------------------------------------------------
#define ldr_sensor A0
//#define sm_sensor 5
#define serverName "https://agriculture-iot.onrender.com/read"
#ifndef ssid
#define ssid "Mi 10T"
#define password "ziyadanas"
#endif
WiFiMulti WiFiMulti;
// global variable------------------------------------------
int s1 = 0;       //light intensity
int id  = 2;
unsigned long lastTime = 0;
unsigned long timerDelay = 5000; //set timer to 5s

void setup() {
  // Setup pinmode-----------------------------
  pinMode(ldr_sensor, INPUT);
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
  wifiMulti.addAP(ssid, password);
  Serial.println("[SETUP] WiFi connected");
}

void loop() {
    // read input sensor-----------------------------------------------------------
  s1 = random(100);
  // check WiFi connection-------------------------------------------------------
  if ((millis() - lastTime) > timerDelay) {
    if((WiFiMulti.run() == WL_CONNECTED)) httpsclient();
    else Serial.println("[SETUP] WiFi Disconnected");
    lastTime = millis();
  }
}

void httpsclient(){
  WiFiClientSecure *client = new WiFiClientSecure;
  client->setInsecure();
  //WiFiClient client;
  HTTPClient http;
  Serial.print("[HTTPS] begin...\n");

  if(http.begin(*client, serverName)){
    Serial.print("[HTTPS] POST...\n");
    //http.addHeader("Content-Type", "application/json");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    String httpData = "id="+String(id)+"&s1="+String(s1);
    int httpResponseCode = http.POST(httpData);
    if (httpResponseCode > 0) { //Check for the returning code
      Serial.println("[HTTPS] POST HTTP code    : "+String(httpResponseCode));
      Serial.println("[HTTPS] ID                : "+String(id));
      Serial.println("[HTTPS] Sensor1           : "+String(s1)+"%");
      String payload = http.getString();Serial.println("[HTTPS]\n\n"+payload+"\n");
    }
    else {
      Serial.println("[HTTPS] Error Code: "+String(httpResponseCode));
    }
  }
  http.end(); //Free the resources
}
