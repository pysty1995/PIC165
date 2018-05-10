#include <LiquidCrystal.h>
#include <FreqCount.h>
LiquidCrystal lcd(7, 8, 9, 10, 11, 12); // (rs, en, d4, d5, d6, d7);
#define voltage_in A0
#define resistor_in A1
#define current_in A2
#define vol_button 2
#define res_button 3
#define freq_button 4
#define current_button 5
void setup()
{
  /* add setup code here */
  lcd.begin(16, 2);
  Serial.begin(9600);
  FreqCount.begin(1000);
  pinMode(vol_button, INPUT_PULLUP);
  pinMode(res_button, INPUT_PULLUP);
  pinMode(feq_button, INPUT_PULLUP);
  pinMode(current_button, INPUT_PULLUP);
  
}

void loop()
{
  /* add main program code here */
  float vol = 0, res = 0, current = 0;
  vol = analogRead(voltage_in);
  res = analogRead(resistor_in);
  current = analogRead(current_in);
  vol = ( vol / 3 )*1000 ; // in mV
  Serial.println("Vol is: "); Serial.print(vol); Serial.print("mV");
  res = ( res * 10000) / (1024 - res); // in R
  Serial.println("Res is: "); Serial.print(res); Serial.print("R");
  if (FreqCount.available()) {
    unsigned long count = FreqCount.read();
    Serial.println("Freq: ");
    Serial.print(count); Serial.print("Hz");
  }
}
