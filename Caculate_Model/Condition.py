import random
from datetime import time

from Map_Model.constant import Map_Point_tuple


# 常量对应
'weather'
weather_Sunny='Sunny'
weather_cloudy='cloudy'
weather_rainy='rainy'
weather_Tuple=(weather_Sunny,weather_cloudy,weather_rainy)
# 上下界
'temperature'
temperature_Max=35
temperature_Min=5
'time'
# 权值

class Condition:
    def __init__(self,weather,temperature,starting,ending,nowtime:time) -> None:
        self.weather=weather
        self.temperature=temperature
        self.starting=starting
        self.ending=ending
        self.nowtime=nowtime
    def Print(self):
        print(self.__dict__)

class init_Condition(Condition):
    def __init__(self) -> None:
        self.weather=random.choice(weather_Tuple)
        self.temperature=random.randint(temperature_Min,temperature_Max)
        self.starting=random.choice(Map_Point_tuple)
        endpoint=random.choice(Map_Point_tuple)
        while endpoint==self.starting:
            endpoint=random.choice(Map_Point_tuple)
        self.ending=endpoint
        self.nowtime=time(random.randint(7,22),random.randint(0,60))