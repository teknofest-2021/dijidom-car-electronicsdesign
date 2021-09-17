import serial
import time
import SI7021 as SI
import datetime
import requests
import json

ser = serial.Serial(
  port='/dev/ttyUSB0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

url = "http://194.31.79.154:6068/api/Measurements/CreateMeasurement"

def req(date,plantid,soilHum,soilTemp,airQuality,airTemp,airHum):
    # date = String
    # plantıd = int
    # soilHum = float ,2
    # soilTemp = float ,2
    # airQuality = float or int
    # airTemp = float ,2
    # airHum = float ,2
    payload = json.dumps({
        
        "plantID": plantid,
        "plantHeight":0,
        "soilHumidity": soilHum,
        "soilTemperature": soilTemp,
        "airQuality": airQuality,
        "airTemperature": airTemp,
        "airHumidity": airHum,
        "measurementDate": date
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)


def Ard_Serial():
    seed_1 = ""
    seed_2 = ""
    seed_3 = ""
    seed_4 = ""
    
    Hum_1 =0
    Hum_2 =0
    Hum_3 =0
    Hum_4 =0
    Temp_1 =0
    Temp_2 =0
    Temp_3 =0
    Temp_4 =0
    PPM = 0
    for i in range(0,9):
        line_data = ser.readline().decode()
        time.sleep(0.5)
        if line_data.find('Na') >0:
            c_data = line_data.replace('Na',"") 
            Hum_1 = c_data.strip()
            Hum_1 = round((float(Hum_1)-0)*(100-0)/(1023-0)+0,2)
        if line_data.find('Nb') >0:
            c_data = line_data.replace('Nb',"") 
            Hum_2 = c_data.strip()
            Hum_2 = round((float(Hum_2)-0)*(100-0)/(1023-0)+0,2)
        if line_data.find('Nc') >0:
            c_data = line_data.replace('Nc',"") 
            Hum_3 = c_data.strip()
            Hum_3 = round((float(Hum_3)-0)*(100-0)/(1023-0)+0,2)
        if line_data.find('Nd') >0:
            c_data = line_data.replace('Nd',"") 
            Hum_4 = c_data.strip()
            Hum_4 = round((float(Hum_4)-0)*(100-0)/(1023-0)+0,2)
        if line_data.find('Ta') >0:
            c_data = line_data.replace('Ta',"") 
            Temp_1 = c_data.strip() 
        if line_data.find('Tb') >0:
            c_data = line_data.replace('Tb',"")
            Temp_2 = c_data.strip()
        if line_data.find('Tc') >0:
            c_data = line_data.replace('Tc',"") 
            Temp_3 = c_data.strip() 
        if line_data.find('Td') >0:
            c_data = line_data.replace('Td',"") 
            Temp_4 = c_data.strip()    
        if line_data.find('PPM') >0:
            c_data = line_data.replace('PPM',"")
            PPM = c_data.strip()
    seed_1 = str(Hum_1)+"#"+str(Temp_1)+"#"+str(PPM)
    seed_2 = str(Hum_2)+"#"+str(Temp_2)+"#"+str(PPM)
    seed_3 = str(Hum_3)+"#"+str(Temp_3)+"#"+str(PPM)
    seed_4 = str(Hum_4)+"#"+str(Temp_4)+"#"+str(PPM)
    return seed_1,seed_2,seed_3,seed_4

def data_parse_push(data):
    date = datetime.datetime.now()
    dt_string = date.strftime("%Y-%m-%dT%H:%M")
    dt_string = str(dt_string)
    pars = data.split("#")
    Car_Temp = float(format(SI.CelsTemp(),'.2f'))
    Car_Humadity = float(format(SI.Humidity(),'.2f'))
    plantid = int(pars[0])
    soilHumidity = float(pars[1])
    soilTemperature = float(pars[2])
    airQuality = float(pars[3])
    req(dt_string,plantid,soilHumidity,soilTemperature,airQuality,Car_Temp,Car_Humadity)

while True:
    date = datetime.datetime.now()
    minute = date.minute
    if minute %15 ==0:
        seed1,seed2,seed3,seed4 = Ard_Serial()  
        Save_out1 = "5"+"#"+seed1
        Save_out2 = "2"+"#"+seed2
        Save_out3 = "3"+"#"+seed3
        Save_out4 = "4"+"#"+seed4
        data_parse_push(Save_out1)
        data_parse_push(Save_out2)
        data_parse_push(Save_out3)
        data_parse_push(Save_out4)
        time.sleep(65)
    time.sleep(5)

