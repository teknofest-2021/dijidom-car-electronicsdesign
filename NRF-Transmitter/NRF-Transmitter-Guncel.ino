#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <OneWire.h>
#include <DallasTemperature.h>


#define ONE_WIRE_BUS1 3 // DS18B20 1
#define ONE_WIRE_BUS2 4 // DS18B20 2
#define ONE_WIRE_BUS3 5 // DS18B20 3
#define ONE_WIRE_BUS4 6 // DS18B20 4

OneWire oneWire1(ONE_WIRE_BUS1);
OneWire oneWire2(ONE_WIRE_BUS2);
OneWire oneWire3(ONE_WIRE_BUS3);
OneWire oneWire4(ONE_WIRE_BUS4);

DallasTemperature sensors1(&oneWire1);
DallasTemperature sensors2(&oneWire2);
DallasTemperature sensors3(&oneWire3);
DallasTemperature sensors4(&oneWire4);

const int AOUTpin=A1; // MQ135
int ppm;  // Ölçülen ppm değeri
int sensorPin = A0; // Toprak nem Data pin

RF24 radio(9, 10); // CE, CSN

const byte address[6] = "00001";

void setup() {
  pinMode(sensorPin, INPUT);
  
  //sensors1.begin();
  sensors2.begin();
  sensors3.begin();
  sensors4.begin();
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
  
  
}
void MQ135(){
  const char hava[10];
  int ppm;
  ppm= analogRead(AOUTpin);
  dtostrf(ppm,2,2,hava);
  strcat(hava, "PPM");
  radio.write(&hava,sizeof(hava));
}
void Temprature1(){
   const char senpaya[10];
   float Celcius=0;
   sensors1.requestTemperatures(); 
   Celcius=sensors1.getTempCByIndex(0);
   dtostrf(Celcius,2,2,senpaya);
   strcat(senpaya, "Ta");
   radio.write(&senpaya,sizeof(senpaya));
}
void Temprature2(){
   const char senpayb[10];
   float Celcius=0;
   sensors2.requestTemperatures(); 
   Celcius=sensors2.getTempCByIndex(0);
   dtostrf(Celcius,2,2,senpayb);
   strcat(senpayb, "Tb");
   radio.write(&senpayb,sizeof(senpayb));
}
void Temprature3(){
   const char senpayc[10];
   float Celcius=0;
   sensors3.requestTemperatures(); 
   Celcius=sensors3.getTempCByIndex(0);
   dtostrf(Celcius,2,2,senpayc);
   strcat(senpayc, "Tc");
   radio.write(&senpayc,sizeof(senpayc));
}
void Temprature4(){
   const char senpayd[10];
   float Celcius=0;
   sensors4.requestTemperatures(); 
   Celcius=sensors4.getTempCByIndex(0);
   dtostrf(Celcius,2,2,senpayd);
   strcat(senpayd, "Td");
   radio.write(&senpayd,sizeof(senpayd));
}
void Soil_Hum1(){
  const char yeni[10];
  float nemVal = analogRead(A0);
  dtostrf(nemVal,2,2,yeni);
  strcat(yeni, "Na");
  radio.write(&yeni,sizeof(yeni));
}
void Soil_Hum2(){
  const char yeni[10];
  float nemVal = analogRead(A2);
  dtostrf(nemVal,2,2,yeni);
  strcat(yeni, "Nb");
  radio.write(&yeni,sizeof(yeni));
}
void Soil_Hum3(){
  const char yeni[10];
  float nemVal = analogRead(A3);
  dtostrf(nemVal,2,2,yeni);
  strcat(yeni, "Nc");
  radio.write(&yeni,sizeof(yeni));
}
void Soil_Hum4(){
  const char yeni[10];
  float nemVal = analogRead(A4);
  dtostrf(nemVal,2,2,yeni);
  strcat(yeni, "Nd");
  radio.write(&yeni,sizeof(yeni));
}
void loop() {
  
  Soil_Hum1();
  Soil_Hum2();
  Soil_Hum3();
  Soil_Hum4();
  Temprature1();
  Temprature2();
  Temprature3();
  Temprature4();
  MQ135();
  delay(1000);
  
}
