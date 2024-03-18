import serial.tools.list_ports
from datetime import datetime, timezone, timedelta
import time
import os
import sqlite3
from pyfirmata import Arduino, util
#from multiprocessing import Pool
import threading

from USB_device import Usb


class Database:
    def __init__(self):
        self.directory = 'C:/JMS'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        # check_same_thread 파라미터를 False로 설정
        self.conn = sqlite3.connect(self.directory + '/JMSPlant.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS smartFarm (
            idx INTEGER PRIMARY KEY AUTOINCREMENT,
            IsRun BOOL,
            sysfan BOOL,
            wpump BOOL,
            led BOOL,
            humidity REAL,
            temperature REAL,
            ground1 INTEGER,
            ground2 INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMP DEFAULT NULL
        )
        """
        self.cursor.execute(query)

    def insert_data(self, IsRun, sysfan, wpump, led, humidity, temperature, ground1, ground2):
        current_time = datetime.now(timezone(timedelta(hours=9)))
        current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        query = """
        INSERT INTO smartFarm (IsRun, sysfan, wpump, led, humidity, temperature, ground1, ground2,created_at,updated_at,deleted_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)
        """
        self.cursor.execute(query, (IsRun, sysfan, wpump, led, humidity, temperature, ground1, ground2,current_time_str, current_time_str))
        self.conn.commit()

class Ardu:
    def __init__(self) -> None:
        self.db = Database()
        self.port = Usb().usb_get("CH340")
        self.arduino = None
        self.defl = "0"

        self.IsRun = None
        self.sysfan = None
        self.wpump = None
        self.led = None
        self.humidity = None
        self.temperature = None
        self.ground1 = None
        self.ground2 = None
        self.a =1
        self.last_print_time = time.time()

        try:
            self.arduino = serial.Serial(self.port, 9600)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)

    def send_data(self):
        #파이썬에서 아두이노의 센서(LED, SYSFAN)를 설정
        input_1, input_2 = map(str, input("\n1. LED, 2. FAN\n(on : 1, off : 0)\ninput : ").split())
        sendDATA = input_1 + ',' + input_2
        Ar.arduino.write(sendDATA.encode())

    def read_serial_data(self):
        #아두이노에서 보낸 데이터를 data에 임시저장
        if self.arduino.in_waiting > 0:
            data = self.arduino.readline().decode().rstrip()
            return data

    def read_data(self):
        #아두이노에서 보낸 데이터를 파이썬에 변수로 저장, 출력
        data = self.read_serial_data()
        if data:
            if data.startswith("IsRun : "):
                if(int(data.split(":")[1].strip()) == 1):
                    self.IsRun          = True
                else:
                    self.IsRun          = False
            if data.startswith("SYSFAN : "):
                if(int(data.split(":")[1].strip()) == 1):
                    self.sysfan         = True
                else:
                    self.sysfan         = False
            if data.startswith("WPUMP : "):
                if(int(data.split(":")[1].strip()) == 1):
                    self.wpump          = True
                else:
                    self.wpump          = False
            if data.startswith("LED : "):
                if(int(data.split(":")[1].strip()) == 1):
                    self.led            = True
                else:
                    self.led            = False
            if data.startswith("Humidity : "):
                self.humidity       = float(data.split(":")[1].strip().split("%")[0])
            if data.startswith("Temperature : "):
                self.temperature    = float(data.split(":")[1].strip().split("*C")[0])
            if data.startswith("Ground1 :"):
                self.ground1        = int(data.split(":")[1].strip())
            if data.startswith("Ground2 :"):
                self.ground2        = int(data.split(":")[1].strip())
            # Check if it has been more than 1 second since last print
            if time.time() - self.last_print_time >= 1:#저장시간
                #print(f"Received data - \nIsRun: {self.IsRun}, SYSFAN: {self.sysfan}, WPUMP: {self.wpump}, Humidity: {self.humidity}%, Temperature: {self.temperature}°C, Ground1: {self.ground1}, Ground2: {self.ground2}")
                self.db.insert_data(self.IsRun, self.sysfan, self.wpump, self.led, self.humidity, self.temperature, self.ground1, self.ground2)
                self.last_print_time = time.time()  # Update the last print time

    def MultiProcessing_Read_Data(self):
        while True:
            self.read_data()

    def MultiProcessing_Send_Data(self):
        while True:
            try:
                self.send_data()
            except:
                print("\nRetry\n")

if __name__ == "__main__":
    Ar = Ardu()
    read_process = threading.Thread(target = Ar.MultiProcessing_Read_Data)
    read_process.start()
    send_process =  threading.Thread(target = Ar.MultiProcessing_Send_Data)
    send_process.start()

    read_process.join()
    send_process.join()
