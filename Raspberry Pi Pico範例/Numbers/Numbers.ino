/***********************************************************
 *              SEND NUMBERS TO RASPBERRY PICO
 *              ==============================
 * This program sends numbers to the Rspberry Pi Pico over
 * the serial link. These numbers are displayed by the Pico
 * 
 * Author: Dogan Ibrahim
 * Date  : February, 2020
 * File  : Numbers.c
 ***********************************************************/
#include <SoftwareSerial.h>
SoftwareSerial MySerial(2, 3);           // RX, TX

String Temp;
int cnt = 0;
char buffer[5];

void setup() 
{
  MySerial.begin(9600);                  // Soft serial speed 9600
}

void loop() 
{
  cnt = cnt + 1;                         // Increment cnt
  itoa(cnt, buffer, 10);                 // Convert to string
  MySerial.println(buffer);
  delay(10000);                          // 10 seconds delay
}
