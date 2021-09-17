
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <FastLED.h>
#define LED_PIN     5
#define NUM_LEDS    20
CRGB leds[NUM_LEDS];

RF24 radio(9, 10); // CE, CSN

const byte address[6] = "00001";

void setup() {
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    char text[32] = "";
    radio.read(&text, sizeof(text));
    Serial.println(text);
  }
  FastLED.clear();
  FastLED.show();
  //NeoLed();
}
void NeoLed()
{
  leds[0] = CRGB(208, 209, 2);
  leds[1] = CRGB(208, 209, 2);
  leds[2] = CRGB(208, 209, 2);
  leds[3] = CRGB(208, 209, 2);
  leds[4] = CRGB(208, 209, 2);
  leds[5] = CRGB(208, 209, 2);
  leds[6] = CRGB(208, 209, 2);
  leds[7] = CRGB(208, 209, 2);
  leds[8] = CRGB(208, 209, 2);
  leds[9] = CRGB(208, 209, 2);
  leds[10] = CRGB(208, 209, 2);
  leds[11] = CRGB(208, 209, 2);
  leds[12] = CRGB(208, 209, 2);
  leds[13] = CRGB(208, 209, 2);
  leds[14] = CRGB(208, 209, 2);
  leds[15] = CRGB(208, 209, 2);
  FastLED.show();
}
