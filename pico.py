from machine import Pin, ADC
import time

# Initialize ADC for the microphone (replace '28' with your ADC pin)
adc = ADC(27)

# GPIO pin for sending signal (replace '15' with your chosen GPIO pin)
signal_pin = Pin(18, Pin.OUT)

def is_sound_detected(threshold=55000):
    # Read the microphone value
    value = adc.read_u16()
    return value > threshold

while True:
    if is_sound_detected():
        signal_pin.value(1)  # Send signal (set pin HIGH)
        time.sleep(0.1)

         # Keep the signal for a duration
    else:
        signal_pin.value(0)
        # No sound detected (set pin LOW)
    time.sleep(0.1)
    # Sampling interval

