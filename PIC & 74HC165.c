/******************************************************************************                                                   
Chip type           : PIC16F877A         
Program type        : Application
Clock frequency     : 20 MHz
Project             : Mo rong dau vao Input
Version             : V1.0
Date                : 03/06/2013
Author              : DAO XUAN TRUONG 
Gmail               : daotruongpro@gmail.com   
Mobile              : 0979.20.90.10
Company             : JVN Technology., JSC 

Comments : Chuong trinh viet mo rong dau vao Input dung 74HC165
*******************************************************************************/
#include <PIC & 74HC165.h>
#include <74165.c>
unsigned int8 data=0;

void main()
{

   while(TRUE)
   {
      //doc du lieu dau vao
      read_expanded_inputs(&data);
      OUTPUT_D(data);
   }

}
