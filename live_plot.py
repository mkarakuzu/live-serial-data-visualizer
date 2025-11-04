import serial
import serial.tools.list_ports
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

class SerialVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Serial Data Visualizer")
        self.root.geometry("500x500")

        self.x = list() #x-axis list definition
        self.y = list() #y-axis list definition
        self.x_count = 1 #data count
        self.is_running = False #program is running or not

        #top frame (port name and baud rate comboboxes)
        top = ttk.Frame(self.root)
        top.pack(fill='x')
        ttk.Label(top, text="Live Serial Data Visualizer", font=("Arial", 20)).pack(side='top')
        ttk.Label(top, text = "Serial Port:").pack(side='left')
        self.port_combobox = ttk.Combobox(top, values = [port.device for port in serial.tools.list_ports.comports()])
        self.port_combobox.pack(side = 'left')

        ttk.Label(top, text = "Baud Rate:").pack(side='left')
        self.baudrate_combobox = ttk.Combobox(top, values= ["9600", "19200", "115200"])
        self.baudrate_combobox.pack(side='left')

        #button frame (start and stop buttons)
        button_frame = ttk.Frame(self.root)
        button_frame.pack()
        self.start_btn = ttk.Button(button_frame, text="Start", command= self.start)
        self.start_btn.pack(side='left')
        self.stop_btn = ttk.Button(button_frame, text="Stop", command=self.stop)
        self.stop_btn.pack(side='left')

        #graph frame (data label and graph)
        graph_frame = ttk.Frame(self.root)
        graph_frame.pack(fill='both')
        self.value_label = ttk.Label(graph_frame, text="Data: --")
        self.value_label.pack()

        self.fig = Figure(figsize=(6, 5))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Live Data Graph")
        self.ax.set_xlabel("Data Number")
        self.ax.set_ylabel("Data Value")

        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill='both')

    #read port function
    def read_port(self):
        while self.is_running:
            if self.ser.in_waiting > 0: #if anything is waiting in port
                try:
                    data = float(self.ser.readline().decode().strip()) #convert string data to float
                
                    self.x.append(self.x_count) #appending data count to x list
                    self.y.append(data) #appending data to y list

                    self.x_count += 1
                    self.value_label.config(text = f"Data: {data}") #update value label

                    #draw graph
                    self.ax.cla()
                    self.ax.plot(self.x, self.y, color = 'blue')
                    self.canvas.draw()
            
                except Exception as ex:
                    self.value_label.config(text = f"Error: {ex}")

            time.sleep(0.05)

    def start(self):
        port = self.port_combobox.get() #get selected port name
        baud_rate = int(self.baudrate_combobox.get()) #get selected baud rate
        try:
            self.ser = serial.Serial(port, baud_rate) #initialize port
            time.sleep(2)
            self.is_running = True
            threading.Thread(target=self.read_port, daemon=True).start() #to listen port, we use threading
        except Exception as ex:
            self.value_label.config(text = f"Error: {ex}")

    def stop(self):
        try:
            if self.ser.is_open:
                self.ser.close() #close port
                self.is_running = False
        except Exception as ex:
            self.value_label.config(text = f"Error: {ex}")
 
if __name__ == "__main__":
    root = tk.Tk()
    app = SerialVisualizer(root)
    root.mainloop()