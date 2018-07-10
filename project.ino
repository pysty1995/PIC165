#include <LiquidCrystal.h>
#include <FreqCount.h>
LiquidCrystal lcd(7, 8, 9, 10, 11, 12); // (rs, en, d4, d5, d6, d7);
#define voltage_in A0
#define resistor_in A1
#define current_in A2
#define vol_button 2
#define res_button 3
#define freq_button 4
#define current_button 6
int menu_flag = 0;
byte ohm_icon[8] = {
  B00000,
  B01110,
  B10001,
  B10001,
  B10001,
  B01010,
  B11011,
  B00000
};
void setup()
{
  /* add setup code here */
  lcd.begin(16, 2);
  Serial.begin(9600);
  FreqCount.begin(1000);
  pinMode(vol_button, INPUT_PULLUP);
  pinMode(res_button, INPUT_PULLUP);
  pinMode(freq_button, INPUT_PULLUP);
  pinMode(current_button, INPUT_PULLUP);
  lcd.createChar(0, ohm_icon);
  lcd.print("Do An Tot Nghiep");
}

void loop()
{
  /* add main program code here */
  float vol = 0, res = 0, current = 0;
  unsigned long count;
  vol = analogRead(voltage_in);
  res = analogRead(resistor_in);
  current = analogRead(current_in);// w8 for investing
  Serial.println("Current is: "); Serial.print(current); Serial.print("mA");
  vol = ( vol / 3 )*1000 ; // in mV
  Serial.println("Vol is: "); Serial.print(vol); Serial.print("mV");
  res = ( res * 10000) / (1024 - res); // in R
  Serial.println("Res is: "); Serial.print(res); Serial.print("R");
  if (FreqCount.available()) {
    count = FreqCount.read();
    Serial.println("Freq: ");
    Serial.print(count); Serial.print("Hz");
  }
  int vol_button_status = digitalRead(vol_button);
  int res_button_status = digitalRead(res_button);
  int freq_button_status = digitalRead(freq_button);
  int current_button_status = digitalRead(current_button); 
  if( vol_button_status == LOW) menu_flag = 1;
  else if( res_button_status == LOW ) menu_flag = 2;
  else if( freq_button_status == LOW ) menu_flag = 3;
  else if( current_button_status == LOW ) menu_flag = 4;
  switch( menu_flag ){

    case 1:
    lcd.setCursor(0, 0);
    lcd.print("Dien ap la:");
    lcd.setCursor(0, 1);
    lcd.print(vol);///
    lcd.setCursor(6, 1);
    lcd.print("mV");
    break;
    case 2: 
    lcd.setCursor(0, 0);
    lcd.print("Dien tro la:");
    lcd.setCursor(0, 1);
    lcd.print(res);////
    lcd.setCursor(6, 1);
    lcd.write(byte(0));
    break;
    case 3:
    lcd.setCursor(0, 0);
    lcd.print("Tan so la:");
    lcd.setCursor(0, 1);
    lcd.print(count); ////
    lcd.setCursor(6, 1);
    lcd.print("Hz");
    break;
    case 4:
    lcd.setCursor(0, 0);
    lcd.print("Dong dien la:");
    lcd.setCursor(0, 1);
    lcd.print(current); ////
    lcd.setCursor(6, 1);
    lcd.print("mA");
    break;
    default:
    lcd.setCursor(0, 0);
    lcd.print("Moi chon....");
    break;
    }
}
