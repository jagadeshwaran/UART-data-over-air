# UART-data-over-air
Transmit the UART data acquired by SYNAPSE module over air

components used:
  - 2 RF200 modules
  - 1 SN171 board
  - USB to UART FTDI chip 
  - 3mm LED
  - 1 USB stick
  
Description:

NodeA is used as portal.

Nodeb B -> connected with USB to UART converter( FTDI chip) -> tries to transmit the data to node A and print in event view window and an LED toggle when a data is received
