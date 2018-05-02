/******************************************************************************                                                   
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
