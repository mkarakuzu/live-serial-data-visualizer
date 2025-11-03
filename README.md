# Live Serial Data Visualizer

This project is a Python application designed to **visualize real-time data received through a serial port**. It can display numerical data dynamically on a live graph, whether the source is a sensor, a microcontroller (e.g., Arduino, ESP32), or any other serial communication device.

---

## 🖼️ Demo

![Demo](demo.gif)

---

## 🔍 Features

* **Real-time data tracking:** Incoming serial data is plotted instantly.
* **Interactive live graph:** Uses `matplotlib` to continuously update the plot as new data arrives.
* **Customizable setup:** Easily modify the port name, baud rate, and graph update interval.
* **Device-agnostic:** Works with any system that outputs serial data — Arduino boards, sensor modules, lab devices, and more.

---

## ⚙️ Requirements

Install the following Python libraries before running the program:

```bash
pip install pyserial matplotlib
```

---

## 🧩 Usage

1. Connect your serial data source to the computer.
   *(For example, an Arduino board, a sensor module, or another serial device.)*

2. Configure the serial settings in the code according to your device:

   ```python
    port = '/dev/tty.usbmodem101' #serial communication device name
    baud_rate = 9600 #serial communication baud rate
    update_interval = 0.01 #graph update interval (second)
   ```

3. Run the script:

   ```bash
   python live_plot.py
   ```

4. The application will display incoming data both in the terminal and on a live graph.

5. When the data stream ends or the window is closed, the serial connection and graph are automatically closed safely.

---

## 🖼️ How It Works

1. The program listens for incoming serial data on the specified port.
2. Each new line of data is decoded, stripped, and converted to a numerical (`float`) value.
3. The values are stored in lists and plotted in real time using `matplotlib`.
4. The graph is continuously refreshed, creating a smooth live visualization.

---

## 🧠 Use Cases

* Real-time visualization of temperature, humidity, or acceleration data from an Arduino or ESP32
* Monitoring live sensor output from lab or industrial equipment
* Observing experimental data streams for analysis
* Visual debugging of prototype systems

---

## 🧰 Notes

* Port names differ depending on the operating system:

  * **Windows:** `COM3`, `COM4`, etc.
  * **macOS / Linux:** `/dev/tty.usbmodem101`, `/dev/ttyACM0`, etc.
* The incoming data should be numeric (e.g., `"23.7"`).
* Any errors encountered during execution will be shown in the terminal, and resources will be closed safely afterward.
