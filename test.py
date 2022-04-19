import datetime
from Caculate_Model.Condition import *
from Caculate_Model.calculate_OptimalPath import *

from Map_Model.constant import *
from Map_Model.map import *

if not True:
    Mapset = list(Map_Point_set)
    M = Edge_Map()
    M.addPath(Mapset[0], Mapset[1], 10)
    M._PrintDict()

if not True:
    'test condition'
    init_Condition().Print()

if     not    True:
    Ad = LiuYuan_canteen
    Bd = South_Gym
    print(calculate_optimal_path_Mode(
        Edge_Map.creatOriginMap(), Ad, Bd, Mode.DrivingMode).__dict__)


if True:
    Ad = LiuYuan_canteen
    Bd = South_Gym
    print(calculate_optimal_path_Mode(Edge_Map.retEdgeMap_Condition(
        init_Condition(), Mode.DrivingMode), Ad, Bd, Mode.DrivingMode).__dict__)
