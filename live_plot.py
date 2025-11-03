import serial
import time
import matplotlib.pyplot as plt

port = '/dev/tty.usbmodem101' #serial communication device name
baud_rate = 9600 #serial communication baud rate
update_interval = 0.01 #graph update interval (second)

try:
    ser = serial.Serial(port, baud_rate) #serial port definition and trying open
    time.sleep(2)

    x = list() #x-axis list definition
    y = list() #y-axis list definition
    x_count = 1 #data count
    plt.ion() #interactive plotting

    while True:
        if ser.in_waiting > 0: #if anything is waiting in port
            try:
                data = float(ser.readline().decode().strip()) #convert string data to float
            
                x.append(x_count) #appending data count to x list
                y.append(data) #appending data to y list

                x_count += 1

                plt.clf() #clear graph
                plt.plot(x,y, color = 'blue') #plot
                plt.pause(update_interval) #update

                print(f"Data: {data}") #print data to terminal
            
            except Exception as ex:
                print(ex)

except Exception as ex:
    print(ex)

finally:
    ser.close() #close port
    plt.close('all') #close graph
   
