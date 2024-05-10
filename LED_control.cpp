// C++ code
//
#include <Arduino.h> //type: ignore
void setup()
{
  for (int i = 8; i<=10; i++){
    pinMode(i, OUTPUT);  
  }
 
 
}
void on_led(int port){

  digitalWrite(port, HIGH);
  delay(1000);
  digitalWrite(port, LOW);
  //delay(1000);
}

void loop()
{
  on_led(8);
  on_led(9);
  on_led(10);
  //delay(1000);
  
}