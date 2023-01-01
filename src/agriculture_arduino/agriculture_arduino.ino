#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <WiFiClientSecureBearSSL.h>

// setup -------------------------------------------------------
//#define ldr_sensor A0
//#define sm_sensor 5
#define serverName "https://api.render.com/v1/services?limit=20"
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
  if((WiFiMulti.run() == WL_CONNECTED)) httpclient();
  else Serial.println("[SETUP] WiFi Disconnected");
  delay(10000);
  //-----------------------------------------------------------------------------
}

void httpclient(){
  std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);
  client->setInsecure();
  HTTPClient https;
  Serial.print("[HTTP] begin...\n");

  if(https.begin(*client, serverName)){
    http.addHeader("Accept", "application/application/json");
    //https.addHeader("Accept", "application/x-www-form-urlencoded");
    https.addHeader("Authorization", "Bearer " + String(api));
    Serial.print("[HTTP] POST...\n");
    int httpResponseCode = https.POST("{\"sm\":\"12\",\"ldr\":\"98\"}");
    //String httpData = "sm="+String(sm)+"&ldr="+String(ldr);
    int httpResponseCode = https.POST(httpData);
    if (httpResponseCode > 0) { //Check for the returning code
      String payload = https.getString();
      Serial.println("[HTTP] POST HTTP code   : "+String(httpResponseCode));
      Serial.println("[HTTP] Moisture         : "+String(sm)+"%");
      Serial.println("[HTTP] Light Intensity  : "+String(ldr)+"%");
      Serial.println("[HTTP]\n\n"+payload+"\n");
    }
    else {
      Serial.print("[HTTP] Error Code: "+String(httpResponseCode));
    }
  }
  https.end(); //Free the resources
}