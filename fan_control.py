import os
import time

FAN_CONTROL_PATH = "/sys/class/thermal/cooling_device0/cur_state"

# Temperaturen zum Ein- und Ausschalten des Lüfters
ON_TEMP = 60  # Temperatur in °C zum Einschalten des Lüfters
OFF_TEMP = 50  # Temperatur in °C zum Ausschalten des Lüfters

def get_cpu_temp():
    """Liest die CPU-Temperatur."""
    temp = os.popen("vcgencmd measure_temp").readline()
    return float(temp.replace("temp=", "").replace("'C\n", ""))

def set_fan_state(state):
    """Setzt den Zustand des Lüfters."""
    with open(FAN_CONTROL_PATH, 'w') as f:
        f.write(str(state))

while True:
    temp = get_cpu_temp()
    if temp > ON_TEMP:
        set_fan_state(1)  # Lüfter einschalten
    elif temp < OFF_TEMP:
        set_fan_state(0)  # Lüfter ausschalten
    time.sleep(10)
