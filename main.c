  #define CRYS_20M //Use this for crystal 20MHz. If It use crystal 10MHz, please comment this
#include <main.h>
#define XBEE_ADDRESS_BYTE1   0x21
#define XBEE_ADDRESS_BYTE2   0x22
#define XBEE_ADDRESS_BYTE3   0x23
#define XBEE_ADDRESS_BYTE4   0x24
#define XBEE_ADDRESS_BYTE5   0x25
#define XBEE_ADDRESS_BYTE6   0x26
#define XBEE_ADDRESS_BYTE7   0x27
#define XBEE_ADDRESS_BYTE8   0x28

#define TIME_ADDRESS   0x29
#define ENABLE_ADDRESS 0x30

#define SaveData write_eeprom
#define LoadData read_eeprom

#define pload_165 PIN_A3
#define dataPin_165 PIN_A1
#define clockPin_165 PIN_A2

#define dataPin_595 PIN_B0
#define clockPin_595 PIN_B1
#define latchPin_595 PIN_B3

int8 chipCount = 1;
int8 dataWidth = chipCount * 8;
int8 pulseWidth = 5 ;// microsecond

unsigned int8 data_165 = 0;
int1 test=0;
int8 ReceiveStep = 0;                                   // dem tung byte trong goi tin
int8 DataReceive = 0;                                    // noi dung cua byte nhan dc
int8 DataLenByte[2] = 
{ 0 };                                                  // chieu dai du lieu
int16 DataLenTotal = 0; 
int8 data_led[8] = {0}; // mang luu gia tri nhan dc tu he thong
int DataReceiveBuffer[30] =
{ 0 };                                                  
int16 DataReceiveCount = 0;
int8 DataCheckByte = 0;
int8 dataTransmit[30] =
   {
   0x7E, 0x00, 0x11, 0x10, 0x01,                     //0x7e: delimeter byte, 0x00, 0x11: do dai du lieu
   0x00, 0x13, 0xA2, 0x00, 0x40, 0xB2, 0x75, 0xBF,         // dia chi 64-bit cua xbee
   0xFF, 0xFE, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,         // data transmit[17]-[24]
   0x00, 0x00, 0x00, 0x00, 0x00 };                     // 1 byte used to checksum [25]-> [30]
int data_button;  
int8 TimeCounter = 0;
int8 TIME = 1;
int1 Enable = TRUE;
int1 isUpdate = TRUE;
int8 TransmitStatus = 0xFF; //0xFF mean not receive respond
int8 TryTime = 0;                                                                                                                           
int8 checkSum();
int8 checkSumRespond();

int1 respondCheck = 1;
int1 offLamp = 1;
int1 res_button = 1;
int1 res_button_status = 1;
int1 res_led = 1;
int1 res_led_status = 1;
void setupTimer();
int8 checkSum();
void ReceiveData();
void ExecuteXBee();
void ReadAddress();
void ReadTime();
void ReadEnable();
void adj_165();
void write_595();
#INT_TIMER0
void interrupt_TIMER0()
{
   TimeCounter++;
   if (TimeCounter >= (TIME*100))
   {
      isUpdate = TRUE;
      TimeCounter = 0;
   }
   set_timer0(60);
}
#INT_RDA
void interrupt_RDA()
{
   ReceiveData();
}

void adj_165(){
  unsigned char data_165;
  unsigned char result;
  read_165(result);
  {
    int1 value1 = ((read_165(result); >> 1) & 0x01);
    int1 value2 = ((result >> 2)) & 0x01);
    int1 value3 = ((result >> 3)) & 0x01);
    int1 value4 = ((result >> 4)) & 0x01);
    int1 value5 = ((result >> 5)) & 0x01);
    int1 value6 = ((result >> 6)) & 0x01);
    int1 value7 = ((result >> 7)) & 0x01);
    int1 value8 = ((result >> 8)) & 0x01);
    if(value1 == 1) data_165 = 0x01;
    else if(value2 == 1) data_165 = 0x02;
    else if(value3 == 1) data_165 = 0x04;
    else if(value4 == 1) data_165 = 0x08;
    else if(value5 == 1) data_165 = 0x10;
    else if(value6 == 1) data_165 = 0x20;
    else if(value7 == 1) data_165 = 0x40;
    else if(value8 == 1) data_165 = 0x80;  
  }
  return data_165;
}
void write_595(unsigned char value){
  int state; 
  for(int i = 0; i < dataWidth; i++)
  {
    output_bit(dataPin_595, !!(value && (1 << i)));
    output_bit(clockPin_595, 1);
    delay_us(pulseWidth);
    output_bit(clockPin_595, 0);
  }
  return state;
}
void main()
{
   int8 i,j;
   setupTimer();
   set_tris_a(0b11111111);
   set_tris_b(0b11011111);
   output_bit(pload_165, 0);
   output_bit(clockPin_165, 0);
   output_bit(dataPin_595, 0);
   output_bit(clockPin_595, 0);
   output_bit(latchPin_595, 0);
   dataTransmit[25] = checkSum();
   enable_interrupts(GLOBAL);         // bat khoa' ngat tong? : GLOBAL
   enable_interrupts(INT_RDA);         // bat khoa' ngat (INT_RDA) = nhay? vao ngat khi nhan data RS232
   //ReadAddress();
   ReadTime();
   ReadEnable();

   while (TRUE)   
   {
      ExecuteXBee();
      unsigned char data = adj_165();

         if((DataReceiveBuffer[12] == 0x4C) && (DataReceiveBuffer[14] == 0x01))         // receive command to turn on led
         {
            res_led = 0;
         }
         if( res_led == 0)
         {  
            data_led[1] = DataReceiveBuffer[13];
            write_595(data_led[1]);
            output_bit( PIN_B4, 1);   
            for (j = 0; j < 5; j++)
               {
               output_toggle(PIN_B4);
               delay_ms( 200 );
               }   
            output_bit( PIN_B4, 0);
            res_led = 1;
            DataReceiveBuffer[12] = 0xFF;
            DataReceiveBuffer[14] = 0xFF;
   
            // ON lamp() ...
         }
///////////////////////////////////////////////////////////////////////////////////
         else if((DataReceiveBuffer[12] == 0x01) && (DataReceiveBuffer[14] == 0x01))         // send led status
         {
            res_led_status = 0;
         }
         if(res_led_status == 0)
         {   
            dataTransmit[17] = 0x01;
            dataTransmit[18] = data_led;
            dataTransmit[19] = 0x01;
            dataTransmit[25] = checkSumRespond();
   
             for ( i = 0; i <= 4; i++) // send maximum 5 times
               {
               while(!TRMT);
               fputc(dataTransmit[i], PORT1);
               }
            output_bit( PIN_B0, 1);
            for (j = 0; j < 5; j++)
               {
               output_toggle(PIN_B4);
               delay_ms( 500 );
               }
            output_bit( PIN_B0, 1);   
            res_led_status = 1;
            DataReceiveBuffer[12] = 0xFF;
            DataReceiveBuffer[14] = 0xFF;
   
            // OFF lamp() ...
         }
         else if((DataReceiveBuffer[12] == 0x00) && (DataReceiveBuffer[14] == 0x00)) // send button status

         {
            res_button_status = 0;
          } 
          if(res_button_status == 0){
          
            dataTransmit[17] = 0x00;
            dataTransmit[18] = adj_165();
            dataTransmit[19] = 0x00;
            dataTransmit[25] = checkSumRespond();
              
             for (i = 0; i <= 4; i++)
               {
               while(!TRMT);
               fputc(dataTransmit[17], PORT1);
               }
            output_bit( PIN_B0, 1);
            for (j = 0; j < 5; j++)
               {
               output_toggle(PIN_B4);
               delay_ms( 500 );
               }
            output_bit( PIN_B0, 1);   
            res_button_status = 1;
            DataReceiveBuffer[12] = 0xFF;
            DataReceiveBuffer[14] = 0xFF;
          
          
          }
         else if((DataReceiveBuffer[12] == 0x00) && (DataReceiveBuffer[14] == 0x00)) //receive command to open/close button
           res_button = 1;
         }
         if(res_button == 1){
          data_button = dataReceiveBuffer[13];
          switch (data_button)
          {
            case 0x01: putc("Den 1 bat"); break;
            case 0x02: putc("Den 2 bat"); break;
            case 0x04: putc("Den 3 bat"); break;
            case 0x08: putc("Den 4 bat"); break;
            case 0x10: putc("Den 5 bat"); break;
            case 0x20: putc("Den 6 bat"); break;
            case 0x40: putc("Den 7 bat"); break;
            case 0x80: putc("Den 8 bat"); break;
            default: break;
          }
          // w8 for investing
         }
   }
}
int8 checkSumRespond()
{
   int temp;
   int sum = 0;
   for (temp = 3; temp < 20; temp++)
   {
      sum = sum + dataTransmit[temp];
   }
   return (0xFF - sum);
}

int8 checkSum()
{
   int temp;
   int sum = 0;
   for (temp = 3; temp < 25; temp++)
   {
      sum = sum + dataTransmit[temp];
   }
   return (0xFF - sum);
}
void setupTimer()
{
   setup_timer_0(RTCC_INTERNAL|RTCC_DIV_256|RTCC_8_bit);      //13.1 ms overflow   
   set_timer0(60); // 10ms interrupt
   enable_interrupts(INT_TIMER0);
   enable_interrupts(GLOBAL);
}
void ReceiveData()            // DataReceiveBuffer[] = mang save data nhan duoc. DataReceiveBuffer[12] toi' DataReceiveBuffer[last] =  chua' data 
{
   if (kbhit())
   {
      DataReceive = getc();
      if ((DataReceive == 0x7E) && ((ReceiveStep > 4) || (ReceiveStep == 0)))
      {
         ReceiveStep = 1; // Co bao da nhan duoc header byte
         return;
      }
      switch (ReceiveStep)
      {
      case 1: // Already receive Start Delimiter byte
         DataLenByte[0] = DataReceive;
         ReceiveStep++;
         break;
      case 2: // Already receive Fist length byte
         DataLenByte[1] = DataReceive;
         DataLenTotal = make16(DataLenByte[0], DataLenByte[1]);
         DataReceiveCount = 0;
         ReceiveStep++;
         break;
      case 3: // Already receive all length byte
         DataReceiveBuffer[DataReceiveCount] = DataReceive;  //DataReceiveBuffer(i)
         DataReceiveCount++;
         if (DataReceiveCount >= DataLenTotal)
            ReceiveStep++;
         break;
      case 4: // Already receive all data byte
         DataCheckByte = DataReceive;
         ReceiveStep++;
         break;
      default:
         break;
      }
   }
}

void ExecuteXBee()         // xbee endDevice save address Host Xbee, host xbee sent data: frame type = 0x01 | RF data = 'S'
{
   int i,j;
   if (ReceiveStep < 5)
      return;
   else
   {
      switch (DataReceiveBuffer[0])
      // Frame type
      {
      case 0x90: // Receive data from control system
         // From byte 1 to 11 of DataReceiveBuffer is address of sender and other status - don't care
         switch (DataReceiveBuffer[12])
         // Command
         
         
         {
         case 'S': //Set host
            for (i = 0; i < 8; ++i)
            {
               dataTransmit[5 + i] = DataReceiveBuffer[1 + i];
            }
            dataTransmit[25] = checkSum();

            SaveData(XBEE_ADDRESS_BYTE1, DataReceiveBuffer[1]);
            SaveData(XBEE_ADDRESS_BYTE2, DataReceiveBuffer[2]);
            SaveData(XBEE_ADDRESS_BYTE3, DataReceiveBuffer[3]);
            SaveData(XBEE_ADDRESS_BYTE4, DataReceiveBuffer[4]);
            SaveData(XBEE_ADDRESS_BYTE5, DataReceiveBuffer[5]);
            SaveData(XBEE_ADDRESS_BYTE6, DataReceiveBuffer[6]);
            SaveData(XBEE_ADDRESS_BYTE7, DataReceiveBuffer[7]);
            SaveData(XBEE_ADDRESS_BYTE8, DataReceiveBuffer[8]);
            Enable = TRUE;
            SaveData(ENABLE_ADDRESS, True);

            for (j = 0; j < 10; j++)
               {
               output_toggle(PIN_B4);
               delay_ms( 500 );
               }

            break;
         case 'T': //Set cycle time
            SaveData(TIME_ADDRESS, DataReceiveBuffer[13]);
            TIME = DataReceiveBuffer[13];
            break;
         case 'X': //Stop
            Enable = FALSE;
            SaveData(ENABLE_ADDRESS, False);
            break;
         default:
            break;
         }
         break;
      case 0x8B: //Transmit status
         TransmitStatus = DataReceiveBuffer[5];
         break;
      default: // Transmit status - don't care
         break;
      }
      ReceiveStep = 0;
   }
}

void ReadAddress()
{
   dataTransmit[5] = LoadData(XBEE_ADDRESS_BYTE1);
   dataTransmit[6] = LoadData(XBEE_ADDRESS_BYTE2);
   dataTransmit[7] = LoadData(XBEE_ADDRESS_BYTE3);
   dataTransmit[8] = LoadData(XBEE_ADDRESS_BYTE4);
   dataTransmit[9] = LoadData(XBEE_ADDRESS_BYTE5);
   dataTransmit[10] = LoadData(XBEE_ADDRESS_BYTE6);
   dataTransmit[11] = LoadData(XBEE_ADDRESS_BYTE7);
   dataTransmit[12] = LoadData(XBEE_ADDRESS_BYTE8);
   dataTransmit[25] = checkSum();
}

void ReadTime()
{
   TIME = LoadData(TIME_ADDRESS);
   if (TIME == 0xFF)
   {
      TIME = 1;
   }
}
void ReadEnable()
{
   Enable = LoadData(ENABLE_ADDRESS);
   if (Enable == 0xFF)
   {
      Enable = True;
   }
}
