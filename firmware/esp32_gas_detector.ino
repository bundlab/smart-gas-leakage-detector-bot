#include <WiFi.h>
#include <HTTPClient.h>

#define MQ_SENSOR 34
#define BUZZER 26

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
const char* server = "http://YOUR_SERVER_IP:8000/api/gas";

void setup() {
  Serial.begin(115200);
  pinMode(BUZZER, OUTPUT);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }
}

void loop() {
  int gasLevel = analogRead(MQ_SENSOR);

  if (gasLevel > 2000) {
    digitalWrite(BUZZER, HIGH);
  } else {
    digitalWrite(BUZZER, LOW);
  }

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(server);
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"gas_level\":" + String(gasLevel) + "}";
    http.POST(payload);
    http.end();
  }
  delay(5000);
}