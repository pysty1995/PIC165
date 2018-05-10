#include <LiquidCrystal.h>
LiquidCrystal lcd(7, 8, 9, 10, 11, 12); // (rs, en, d4, d5, d6, d7);


#define voltage_in A0
#define resistor_in A1
#define vol_button 2
#define res_button 3
#define freq_button 4
#define current_button 5
void setup()
{

  /* add setup code here */
  lcd.begin(16, 2);
  Serial.begin(9600);
  pinMode(vol_button, INPUT_PULLUP);
  pinMode(res_button, INPUT_PULLUP);
  pinMode(feq_button, INPUT_PULLUP);
  pinMode(current_button, INPUT_PULLUP);
  
}

void loop()
{
  /* add main program code here */
  float vol, res;
  vol = analogRead(voltage_in);
  res = analogRead(resistor_in);
  
  vol = ( vol / 3 )*1000 ; // in mV
  Serial.println("Vol is: "); Serial.println()
  res = ( res * 10000) / (1024 - res); // in R
  
  
}
