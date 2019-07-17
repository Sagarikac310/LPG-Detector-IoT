import sys
import serial
import csv
#import keyboard
#import pynput.keyboard as kb

print("modules start")
#print(kb.__file__)
print(serial.__file__)
print("modules end")

try:
    # open the serial port; only do this once as most arduinos reset when the serial port is opened
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600)
    # e.g. remove remains of Arduino bootloader or old data while the application was not running
    # not sure yet if it's 100% reliable; robin's approach is probably safer
    ser.flushInput()
    l = list()
    while True:
        # check if bytes received
        numBytes = ser.inWaiting()
        if(numBytes > 0):
            serBytes = ser.readline()
            serBytes2 = ser.readline() 
            print(str(serBytes))
            print(int(serBytes2))
            print('---------------')
            l.append([str(serBytes),int(serBytes2)])
            # open file for binary (!) appending; not using binary results in
            # 1) error telling you 'must be str, not bytes'
            # 2) convering using str(ser_bytes) results in unwanted quotation marks in the file (as shown in the result of above print)
            # check if <esc> was pressed; stop if so
        #if kb.is_pressed('esc'):
         #   break;

    # close serial port
    ser.close
except:
    print("Unexpected error:", sys.exc_info()[0])
    print("Unexpected error:", sys.exc_info()[1])

    # maybe todo: close serial port; this might need a little rework of above code moving 'ser = serial.Serial('COM4', baudrate=57600)' to outside the try
print(l)
with open('project2.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(l)
