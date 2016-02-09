# UART-data-over-air
Transmit the UART data acquired by SYNAPSE module over air

components used:
  - 2 RF200 modules
  - 1 SN171 board
  - USB to UART FTDI chip 
  - 3mm LED
  - 1 USB stick
  
Description:

NodeA:
used as portal.

NodeB :
USB to UART converrter(FTDI chip and cool term software) -> RF200 -> data Over the air to other node, data to be printed in event view window and an LED toggle whenever data is received.  

Test :
- primary test for getting the data from UART is carried out, the code for it is in the reposit.
