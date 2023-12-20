/***********************************************************
 *                    TEMPERATURE DISPLAY
 *                    ===================
 * This program reads the analog temperature data from the
 * Raspberry Pi Pico over teh serial link and then displays
 * this data on the Arduino IDE monitor         
 * 
 * Author: Dogan Ibrahim
 * Date  : February, 2020
 * File  : Temp.c
 ***********************************************************/
#include <SoftwareSerial.h>
SoftwareSerial MySerial(2, 3);           // RX, TX

String Temp;
char ch;

void setup() 
{
  Serial.begin(9600);                    // Monitor speed 9600
  MySerial.begin(9600);                  // Soft serial speed 9600
}

void loop() 
{
  if(MySerial.available() > 0)           // Data available?
  {
    ch = MySerial.read();
    Temp.concat(ch);
    if(ch == '\n')
    {
        Serial.print("Temperature = ");
        Serial.print(Temp);               // Display data
        Temp="";
    }
  }
}
