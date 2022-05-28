import serial
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from time import sleep
import karelPupper
import numpy as np

def main():
    ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
    ser.reset_input_buffer()
    is_first_reading = True
    baseline = 0

    myPup = karelPupper.Pupper()
    #myPup.wakeup()
    sleep(2)

    pupper_displacement = 0
    
    while True:
        if ser.in_waiting > 0:
            if is_first_reading:
                baseline = float(ser.readline().decode('utf-8').rstrip())
                is_first_reading = False
            line = float(ser.readline().decode('utf-8').rstrip())
            displacement = line - baseline
            print(displacement)
            if np.abs(displacement - pupper_displacement) > 0.25:
                myPup.turn_for_time(1, np.sign(displacement - pupper_displacement)*0.4)
                sleep(1)
                pupper_displacement = displacement
            #else:
            #    myPup.forward(0.1, 0.1)
            #    sleep(1)


            
if __name__ == '__main__':
    main()
