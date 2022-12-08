/*
  Abhishek Kairamkonda
  Project Title : Realtime Garbage Monitor 
  Contact EMAIL: abk1382000@gmail.com
*/
#include <WiFi.h>
#include <FirebaseESP32.h>
#include <addons/TokenHelper.h>
#include "soc/rtc.h"
#include "HX711.h"
#include <addons/RTDBHelper.h>

#define WIFI_SSID "YOUR_SSID" //REPLACE IT WITH YOUR SSID
#define WIFI_PASSWORD "YOUR_PASSWORD" //REPLACE IT WITH YOUR WIFI_PASSWORD
#define API_KEY "YOUR_API_KEY" //Replace it with your Realtime Database API key
#define DATABASE_URL "https://yourURL.firebaseio.com/" //replace it with your RTDB URL

//CONSTANT Value declaration
#define SOUND_SPEED 0.034
#define VOLUME_CONST 1809.57 //Radius of container = 24 so volume const pi*r^2 = 1809.57
#define VOLUME_THRESHOLD 45000.0 //Container Threshold

//OBJECT CREATION
FirebaseData fbdo;
HX711 scale;
FirebaseAuth auth;
FirebaseConfig config;

//PIN DECLARATION

String main="";
const int trigPin = 5;
const int echoPin = 18;
const int alertPin = 23;
const int LOADCELL_DOUT_PIN = 21;
const int LOADCELL_SCK_PIN = 22;

/* 
Pin connection :-
  FOR ULTRASONIC SENSOR:
    echo pin to pin 18 of esp32
    trigger pin to pin 5 of esp32
    vcc - 5V or 3.3V
    gnd to gnd

  FOR WEIGHT SENSOR (LOAD CELL with HX711 Amplifier):
    VCC to 5V or 3.3V
    GND to GND
    SDA to GPIO 21 of esp32
    SCL to GPIO 22 of esp32
  FOR ALERT LED :
  ANODE to GPIO 23 of esp32
  cathode to GND of esp32
  
*/

long duration;
float distanceCm;
float Volume;
float reading;

////

void setup()
{
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(alertPin, OUTPUT);
  rtc_clk_cpu_freq_set(RTC_CPU_FREQ_80M);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  Serial.begin(115200);
  delay(2000);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
  Serial.printf("Firebase Client v%s\n\n", FIREBASE_CLIENT_VERSION);
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  Firebase.begin(DATABASE_URL, API_KEY);
  Firebase.setDoubleDigits(5);

}

void loop(){
  
  //ULTRASONIC SENSOR READ
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * SOUND_SPEED/2;
  Volume = VOLUME_CONST*distanceCm;
  if (Volume > VOLUME_THRESHOLD){
    digitalWrite(alertPin,HIGH);
    }
  //WEIGHT SENSOR READ
  if (scale.is_ready()){
    scale.set_scale(-480.134); //CALIBRATION FACTOR -480.134
    delay(1000);
    long reading = scale.get_value(10);
    delay(3000);
    scale.power_down();
    }
 if (Firebase.ready()) 
  { 
    //SYNTAX For Firebase Set Command
    // Firebase.setInt(fbdo, "/HouseX/GarbageWeight/",reading);
    // Firebase.setInt(fbdo, "/HouseX/GarbageVolume/",Volume);
    
    Firebase.setInt(fbdo, "/House1/GarbageWeight/", reading);//Unit in gms
    Firebase.setInt(fbdo, "/House1/GarbageVolume/", Volume); //Unit in cm3
    delay(2500);
    scale.power_up();
    delay(1000);
    }
}
