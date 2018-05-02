#IFNDEF EXP_IN_ENABLE

#define EXP_IN_ENABLE   PIN_B3
#define EXP_IN_CLOCK    PIN_B4
#define EXP_IN_DI       PIN_B5
#define NUMBER_OF_74165 1

#ENDIF


void read_expanded_inputs(BYTE *ei) {
  BYTE i;

  output_high(EXP_IN_CLOCK);
  output_low(EXP_IN_ENABLE);      // Latch all inputs
  output_high(EXP_IN_ENABLE);

  for(i=1;i<=NUMBER_OF_74165*8;++i) {      // Clock in bits to the ei structure
    shift_left(ei,NUMBER_OF_74165,input(EXP_IN_DI));
    output_low(EXP_IN_CLOCK);
    output_high(EXP_IN_CLOCK);
  }
  output_low(EXP_IN_ENABLE);
}
