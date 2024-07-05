#include <Wire.h>
#include "hsc_ssc_i2c.h"

#define DEBUG_LEVEL 1

#define HSCDDRN060MD2A5
//#define

#define RESULT_DECIMALS 4

// example differential sensor
#ifdef HSCDDRN060MD2A5
const uint8_t HSC_SENSOR_ADDR = 0x28;
const int16_t HSC_OUTPUT_MIN = 0x0666;
const int16_t HSC_OUTPUT_MAX = 0x399A;
const float HSC_PRESSURE_MIN = -60;
const float HSC_PRESSURE_MAX = 60;
#endif

uint32_t previousPost = 0;
//const uint32_t postInterval = 1000;
const uint32_t postInterval = 500; // tempo (ms) entre medidas

void setup()
{
  Serial.begin(9600);
  Wire.begin();
}

void loop()
{
  struct cs_raw raw_sensor_data;
  uint8_t el;
  float pressure, temperature;
  if ((millis() - previousPost > postInterval) && (Serial.available() <= 0)) {
    previousPost = millis();
    el = ps_get_raw(HSC_SENSOR_ADDR, &raw_sensor_data);
#if DEBUG_LEVEL > 0
    if ( el == 4 ) {
      Serial.println(F("ERROR: no sensor "));
    } else {
      if ( el == 3 ) {
          Serial.print(F("ERROR: diagnostics fail "));
          Serial.println(raw_sensor_data.status, BIN);
      }
      if ( el == 2 ) {
          // if data has already been feched since the last
          // measurement cycle
          Serial.print(F("WARNING: stale data "));
          Serial.println(raw_sensor_data.status, BIN);
      }
      if ( el == 1 ) {
          // chip in command mode
          Serial.print(F("WARNING: command mode "));
          Serial.println(raw_sensor_data.status, BIN);
      }
#endif
#if DEBUG_LEVEL > 4
      Serial.print("Status: ");
      Serial.println(raw_sensor_data.status, BIN);
      Serial.print("Bridge data: ");
      Serial.println(raw_sensor_data.bridge_data, DEC);
      //Serial.print("Temperature data: ");
      //Serial.println(raw_sensor_data.temperature_data, DEC);
#endif
      ps_convert(raw_sensor_data, &pressure, &temperature, HSC_OUTPUT_MIN, HSC_OUTPUT_MAX, HSC_PRESSURE_MIN, HSC_PRESSURE_MAX);
      //Serial.print(F("Pressure (mbar): "));
      Serial.println(String(pressure, RESULT_DECIMALS));
      //Serial.print("Temperature (C): ");
      //Serial.println(String(temperature, RESULT_DECIMALS));
    }
  }
}