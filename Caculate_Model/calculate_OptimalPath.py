from Map_Model.constant import (Bicycle_parking_point_tuple,
                                Car_parking_point_tuple, Map_Point_tuple, Mode)
from Map_Model.map import Edge_Map

from Caculate_Model.Condition import Condition

value_TransformFunction_Dict = {
    Mode.WalkingMode: lambda x: x,
    Mode.CyclingMode: lambda x: x,
    Mode.DrivingMode: lambda x: x,
}


class optimal_path_value:
    def __init__(self, optimalValue, *optimalPath) -> None:
        self.optimalValue = optimalValue
        self.optimalPath = optimalPath

    def getValue(self):
        return self.optimalValue

    def getPath(self):
        return self.optimalPath


def Dijistra_algorithm_calculate(Edge: Edge_Map, starting, ending) -> optimal_path_value:
    '求边权图中点到点的最优路径'

    AllPointTuple = Map_Point_tuple

    distanceDict = {name: -1 for name in AllPointTuple}
    pathDict = {name: [] for name in AllPointTuple}
    judgedList = [starting]
    notjudgedList = list(AllPointTuple)
    notjudgedList.remove(starting)

    for point in notjudgedList:
        if Edge.judgeAtoB(point, starting):
            distanceDict[point] = Edge.getAtoB(point, starting)
            pathDict[point] = [starting]

    while set(judgedList) != set(AllPointTuple):
        minPoint = ''
        minValue = -1
        for name in notjudgedList:
            if distanceDict[name] != -1:
                if minValue == -1 or distanceDict[name] < minValue:
                    minPoint, minValue = name, distanceDict[name]
        judgedList.append(minPoint)
        notjudgedList.remove(minPoint)

        # 更新路径
        for point in notjudgedList:
            if Edge.judgeAtoB(point, minPoint) \
                and (distanceDict[point] == -1
                     or Edge.getAtoB(point, minPoint)+distanceDict[minPoint] < distanceDict[point]):
                distanceDict[point] = Edge.getAtoB(
                    point, minPoint)+distanceDict[minPoint]
                pathDict[point] = pathDict[minPoint] + [minPoint]
    return optimal_path_value(distanceDict[ending], pathDict[ending]+[ending])


def calculate_optimal_path_Mode(Edge: Edge_Map, starting, ending, mode: Mode):
    "计算3种mode对应的最优路径"
    if mode == Mode.WalkingMode:
        return Dijistra_algorithm_calculate(Edge, starting, ending)
    elif mode == Mode.CyclingMode:
        first = True
        optimal_Path = None
        optimal_Value = None
        for i in Bicycle_parking_point_tuple:
            for j in Bicycle_parking_point_tuple:
                if i != j:
                    path1 = Dijistra_algorithm_calculate(Edge, starting, i)
                    path2 = Dijistra_algorithm_calculate(Edge, i, j)
                    path3 = Dijistra_algorithm_calculate(Edge, j, ending)
                    Value = 10*(path1.getValue()+path3.getValue()) + \
                        path2.getValue()
                    if first or Value < optimal_Value:
                        first = False
                        optimal_Path = (path1.getPath(),path2.getPath(),path3.getPath())
                        optimal_Value = 4 * \
                            (path1.getValue()+path3.getValue())+path2.getValue()
        return optimal_path_value(optimal_Value,*optimal_Path)
    elif mode == Mode.DrivingMode:
        first = True
        optimal_Path = None
        optimal_Value = None
        for i in Car_parking_point_tuple:
            for j in Car_parking_point_tuple:
                if i != j:
                    path1 = Dijistra_algorithm_calculate(Edge, starting, i)
                    path2 = Dijistra_algorithm_calculate(Edge, i, j)
                    path3 = Dijistra_algorithm_calculate(Edge, j, ending)
                    Value = 10 * (path1.getValue()+path3.getValue()) + \
                        path2.getValue()
                    if first or Value < optimal_Value:
                        first = False
                        optimal_Path = (path1.getPath(),path2.getPath(),path3.getPath())
                        optimal_Value = 10 * \
                            (path1.getValue()+path3.getValue())+path2.getValue()
        return optimal_path_value(optimal_Value,*optimal_Path)
