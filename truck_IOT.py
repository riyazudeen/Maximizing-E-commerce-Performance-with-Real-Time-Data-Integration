from datetime import datetime
import time
import requests
import json

def truck_location(truck_id,latitude,longitude,speed,vehicle_speed,engine_rpm,fuel_level,temperature,oil_pressure,battery_voltage, odometer_reading ,fuel_consumption ,brake_status,front_left,rear_left,humidity ,atmospheric_pressure):
    try: 
        truck_id += 1
        latitude += 1
        longitude += 1
        speed += 1
        vehicle_speed += 1
        engine_rpm += 1
        fuel_level += 1
        temperature +=1
        oil_pressure +=1
        battery_voltage +=1
        odometer_reading += 1
        fuel_consumption += 1
        brake_status +=1
        front_left +=1
        rear_left +=1
        humidity += 1
        atmospheric_pressure += 1
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = datetime.today().strftime('%d-%m-%Y')
        data  = {"time":f"{current_time}",
                 "date":f"{today}",
                 "truck_data" : {
          "truck_id": f"TRK00{truck_id}",
          "gps_location": {
            "latitude": latitude,
            "longitude": longitude,
            "altitude": 89,
            "speed": speed
          },
          "vehicle_speed": vehicle_speed,
          "engine_diagnostics": {
            "engine_rpm": engine_rpm,
            "fuel_level": fuel_level,
            "temperature": temperature,
            "oil_pressure": oil_pressure,
            "battery_voltage": battery_voltage
          },
          "odometer_reading": odometer_reading,
          "fuel_consumption": fuel_consumption,
          "vehicle_health_and_maintenance": {
            "brake_status": "Good",
            "tire_pressure": {
              "front_left": front_left,
              "front_right": 32,
              "rear_left": rear_left,
              "rear_right": 35
            },
            "transmission_status": "Operational"
          },
          "environmental_conditions": {
            "temperature": temperature,
            "humidity": humidity,
            "atmospheric_pressure": atmospheric_pressure
          },
        }}

        api_url = "your aip url"
        trucks_data = {"trucks": []}
        for _ in range(3):
          trucks_data["trucks"].append(data)
        jsondata = json.dumps(trucks_data)
        response = requests.post(api_url,json=jsondata)
        if response.status_code == 200: 
               print("uploaded !")
               print(jsondata)     
               print(response)     
               print(response.content)     
        else:
              print(jsondata)
              print(response)
    except Exception as e:
              print(e)


while True: 
      truck_id = 1
      latitude = 34
      longitude = -118
      speed = 65
      vehicle_speed = 65
      engine_rpm = 2500
      fuel_level = 90
      temperature =75
      oil_pressure =40
      battery_voltage =13
      odometer_reading = 102345
      fuel_consumption = 32
      brake_status =22
      front_left =32
      rear_left =35
      humidity = 90
      atmospheric_pressure = 13
      print("this will run after every 30 sec")
      truck_location(latitude,longitude,speed,vehicle_speed,engine_rpm,fuel_level,temperature,oil_pressure,battery_voltage,odometer_reading,fuel_consumption,brake_status,front_left,rear_left,humidity,atmospheric_pressure,909)
      time.sleep(30)
