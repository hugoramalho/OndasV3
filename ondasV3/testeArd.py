import serial.tools.list_ports
import sys
import atexit
import platform

print("=== Auto scan for Arduino Uno connected port===")
print("")
print(platform.system(), platform.release())
print(platform.dist())
print("Python version " + platform.python_version())
print("")

def findArduinoUnoPort():
    portList = list(serial.tools.list_ports.comports())
    for port in portList:
        print(port)
        if "VID:PID=2341:0043" in port[0]\
            or "VID:PID=2341:0043" in port[1]\
            or "VID:PID=2341:0043" in port[2]:
            print(port)
            print(port[0])
            print(port[1])
            print(port[2])
            #please note: it is not sure [0]
            #returned port[] is no particular order
            #so, may be [1], [2]
            return port[0]


def doAtExit():

    if serialUno.isOpen():
        serialUno.close()
        print("Close serial")
        print("serialUno.isOpen() = " + str(serialUno.isOpen()))


atexit.register(doAtExit)

unoPort = findArduinoUnoPort()
if not unoPort:
    print("No Arduino Uno found")
    sys.exit("No Arduino Uno found - Exit")

print("Arduino Uno found: " + unoPort)
print()

serialUno = serial.Serial(unoPort, 9600)
print("serialUno.isOpen() = " + str(serialUno.isOpen()))

while True:

    while (serialUno.inWaiting()==0):
        pass
    valueRead = serialUno.readline(500)
    print(valueRead)

    
