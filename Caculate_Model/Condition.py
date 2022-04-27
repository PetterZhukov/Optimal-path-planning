import random
from datetime import time

from Map_Model.constant import Map_Point_tuple


# 常量对应
'weather'
weather_Sunny = 'Sunny'
weather_cloudy = 'cloudy'
weather_rainy = 'rainy'
weather_Tuple = (weather_Sunny, weather_cloudy, weather_rainy)
# 上下界
'temperature'
temperature_Max = 40
temperature_Min = 0
'time'
# 权值


class Condition:
    def __init__(self, weather=None, temperature=None, starting=None, ending=None, nowtime: time = None) -> None:
        self.weather = weather if weather != None else self.init_weather()
        self.temperature = temperature if temperature != None else self.init_temperature()
        self.starting = starting if starting != None else self.init_starting()
        self.ending = ending if ending != None else self.init_endpoint()
        self.nowtime = nowtime if nowtime != None else self.init_nowtime()

    def Print(self):
        print(self.__dict__)

    def init_weather(self):
        return random.choice(weather_Tuple)

    def init_temperature(self):
        return random.randint(temperature_Min, temperature_Max)

    def init_starting(self):
        return random.choice(Map_Point_tuple)

    def init_endpoint(self):
        endpoint = random.choice(Map_Point_tuple)
        while endpoint == self.starting:
            endpoint = random.choice(Map_Point_tuple)
        return endpoint

    def init_nowtime(self):
        return time(random.randint(7, 22), random.randint(0, 59))

