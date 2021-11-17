import serial
import struct
from datetime import datetime

PORT = 'COM3'  # 每台電腦不一樣

UMPACK_PAT = '<ccHHHcc'

with serial.Serial(PORT, 9600, bytesize=8, parity='N', stopbits=1) as ser:
    while True:
        data = ser.read(10)
        unpacked = struct.unpack(UMPACK_PAT, data)
        ts = datetime.now()
        pm25 = unpacked[2] / 10.0
        pm10 = unpacked[3] / 10.0
        print(f'{ts}: PM2.5 = {pm25} ,PM10 = {pm10}')
