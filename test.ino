int cambien1 = 3;   // moi lan cam bien lai tang bo dem len 1, sau khi cam bien xong thi dong role theo so tg da cai dat truoc
int out1 = 4;   //output ra relay
/*
bình thường cambien1 chưa bị che thì mạch ko chạy, sau khi bị che bộ đếm sẽ tăng 1, sau đó cambien1 ko bị che nữa thì đóng relay theo số time
đã cài đặt tính bằng giây.
nút nhấn: nút 1 _ giữ 3s reset bộ đếm
nút 2 _ cài đặt thời gian đóng relay tính bằng s
nút 3 _ tăng time
nút 4 _ giảm time
*/
#define BAT HIGH
#define TAT LOW

int latchPin = 6;//ST_CP
int clockPin = 7;//SH_CP 
int dataPin = 5; //DS 
int reset_button = 12;
int down_button = 13;
int up_button = 0;
int setup_button = 1; 
bool last_setup_status = false;
bool isProduct = false;
int setup_flag = 0;
unsigned long previousMillis = 0;
// int reset_button_status, down, up, setup_button_status, value;
long timer = 1;
int counter = 0;
int state = LOW;
void setup ()
{
pinMode(latchPin,OUTPUT);
pinMode(clockPin,OUTPUT);
pinMode(dataPin,OUTPUT);
pinMode(out1, OUTPUT); 
pinMode(reset_button, INPUT_PULLUP);
pinMode(down_button, INPUT_PULLUP);
pinMode(up_button, INPUT_PULLUP);
pinMode(setup_button, INPUT_PULLUP);
pinMode(cambien1, INPUT_PULLUP);

}
 
void displayNum(int Num_Dis, int Num_Pos)
{
int Num_Dis_B = 0;
int Num_Pos_B = 0;
switch (Num_Dis) 
{
case 0:Num_Dis_B = 0b11000000;break;
case 1:Num_Dis_B = 0b11111001;break;
case 2:Num_Dis_B = 0b10100100;break;
case 3:Num_Dis_B = 0b10110000;break;
case 4:Num_Dis_B = 0b10011001;break;
case 5:Num_Dis_B = 0b10010010;break;
case 6:Num_Dis_B = 0b10000010;break;
case 7:Num_Dis_B = 0b11111000;break;
case 8:Num_Dis_B = 0b10000000;break;
case 9:Num_Dis_B = 0b10010000;break;
case 'e': Num_Dis_B = 0b00000110; break;
case '-': Num_Dis_B = 0b11111110 ; break;
case 'o': Num_Dis_B = 0b11111111; break;
default:break;
};

switch (Num_Pos)
{
case 1:Num_Pos_B = 0b10000000;break;
case 2:Num_Pos_B = 0b01000000;break;
case 3:Num_Pos_B = 0b00100000;break;
case 4:Num_Pos_B = 0b00010000;break;
case 5:Num_Pos_B = 0b00001000;break;
case 6:Num_Pos_B = 0b00000100;break;
case 7:Num_Pos_B = 0b00000010;break;
case 8:Num_Pos_B = 0b00000001;break;
default:break;
};

//========================================
digitalWrite(latchPin,LOW); 

int L = Num_Dis_B; int R = Num_Pos_B;
shiftOut(dataPin,clockPin,MSBFIRST,R);
shiftOut(dataPin,clockPin,MSBFIRST,L);
digitalWrite(latchPin,HIGH); 
//========================================
delayMicroseconds(5);
}
void showNum(int number)

{

int ShowNumber[4];
ShowNumber[4] = (number/1000)%10;
ShowNumber[3] = (number/100)%10;
ShowNumber[2] = (number/10)%10;
ShowNumber[1]= (number/1)%10;
 
displayNum(ShowNumber[1],1);
displayNum(ShowNumber[2],2);
displayNum(ShowNumber[3],3);
displayNum(ShowNumber[4],4);

}
void delay_timer(int numb){
    int number[3];
    number[1] = (numb/1)%10;
    number[2] = (numb/10)%10;
    number[3] = (numb/100)%100;
    displayNum(number[1], 5);
    displayNum(number[2], 6);
    displayNum(number[3], 7);
}
//============================================================
void loop()
{
unsigned long currentMillis = millis();
setup_flag = 0;

if(setup_flag == 0)
{
displayNum('o', 8);
} 
int up_button_status=digitalRead(up_button);
int down_button_status = digitalRead(down_button);
int reset_button_status = digitalRead(reset_button);
int cambien_status = digitalRead(cambien1);
int setup_button_status = digitalRead(setup_button);
//======================================
if(reset_button_status == LOW) {
delay(3000);
if(reset_button_status == LOW)
{
counter = 0;
}
}
   showNum(counter);
//======================================
if(setup_button_status == LOW) last_setup_status = true;
if((setup_button_status == LOW) && (last_setup_status == true)){
   setup_flag = setup_flag + 1;
   last_setup_status = false;
}
if(setup_flag == 1)
{
displayNum('e', 8);
if(up_button_status == LOW){
  timer++;
  delay(100);
  if(timer > 999)
  timer = 0;
  }
if(down_button_status == LOW)
{
  timer--;
  delay(100);
  if(timer < 0)
  timer = 999;
  }
}
else if(setup_flag == 2){
displayNum('-', 8);
delay_timer(timer);
setup_flag = 0;
}
delay_timer(timer);

//======================================

if(cambien_status == LOW)
{
   
   counter++;
   delay(100);
   isProduct = true;
   if(counter > 9999)
   counter = 0;
   if(isProduct)
   {
   if((currentMillis - previousMillis) >= (unsigned long)(timer*1000))
   {
   previousMillis = currentMillis;
   if(state == HIGH)
   {
   state = LOW;
   } 
   else 
   {
   state = HIGH;
   }
   digitalWrite(out1, state);

   }
   isProduct = false;
   }
}
 
   //======================================

   showNum(counter);
   }
   

