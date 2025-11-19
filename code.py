import time
import board
import analogio
import digitalio

# -----------------------
# Joystick analog pins
# -----------------------
x = analogio.AnalogIn(board.GP26)  # VRx
y = analogio.AnalogIn(board.GP27)  # VRy

# Joystick button (active LOW)
sw = digitalio.DigitalInOut(board.GP16)
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

# -----------------------
# Direction LEDs
# -----------------------
led_up = digitalio.DigitalInOut(board.GP2)
led_up.direction = digitalio.Direction.OUTPUT

led_down = digitalio.DigitalInOut(board.GP3)
led_down.direction = digitalio.Direction.OUTPUT

led_left = digitalio.DigitalInOut(board.GP4)
led_left.direction = digitalio.Direction.OUTPUT

led_right = digitalio.DigitalInOut(board.GP5)
led_right.direction = digitalio.Direction.OUTPUT


def direction_from_value(value, center=32768, threshold=8000):
    """
    Converts ADC value into:
    -1 = negative direction (LEFT or DOWN)
     0 = centered
     1 = positive direction (RIGHT or UP)
    """
    if value < center - threshold:
        return -1
    elif value > center + threshold:
        return 1
    else:
        return 0


while True:
    x_val = x.value      # 0–65535
    y_val = y.value      # 0–65535
    pressed = not sw.value   # True when pressed (active LOW)

    x_dir = direction_from_value(x_val)  # -1 left, +1 right
    y_dir = direction_from_value(y_val)  # -1 down, +1 up

    # Update LEDs
    led_left.value = (x_dir == -1)
    led_right.value = (x_dir == 1)
    led_up.value = (y_dir == 1)
    led_down.value = (y_dir == -1)

    # Debug print over serial
    print("X:", x_val, "Y:", y_val,
          "x_dir:", x_dir, "y_dir:", y_dir,
          "Pressed:", pressed)

    time.sleep(0.05)
