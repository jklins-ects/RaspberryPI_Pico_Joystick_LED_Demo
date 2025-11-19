# Circuit Python/Raspberry Pi Pico Joystick Demo 
## Lights up different LEDs based on joystick direction. 
A basic joystick and wiring test.
### Materials:
- Rasberry Pi Pico
  - Flash the latest Circuit Python onto it.
- Joystick (5 pin)
- Breadboard/wires
- 220g resistors (for LEDs)
- 4 LEDs
### Joystick Connections:
- VCC → 3V3
- GND → GND
- VRx → GP26
- VRy → GP27
- SW → GP16
### LEDs (with 220g resistors!)
- UP LED anode → resistor → GP2
- DOWN LED anode → resistor → GP3
- LEFT LED anode → resistor → GP4
- RIGHT LED anode → resistor → GP5
- All LED cathodes → GND

Once Circuit Python is flashed onto the pico and all the wiring is complete, just save code.py to the Pico (CIRCUITPY drive)

<img width="365" height="406" alt="image" src="https://github.com/user-attachments/assets/acf49563-dc68-4dcc-93ce-7ae956364dd1" />

<img width="600" height="519" alt="image" src="https://github.com/user-attachments/assets/a75a9df0-ebe4-441e-82be-23cd6326813d" />

