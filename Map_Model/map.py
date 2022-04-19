from operator import methodcaller
from Caculate_Model.Condition import Condition
from Map_Model.constant import *


class Edge_Map:
    def __init__(self) -> None:
        self.PointSet = Map_Point_tuple
        self.EdgeValueDict = {name: {} for name in Map_Point_tuple}

    def addPath(self, n1: str, n2: str, value: int):
        "add Path =   n1 <-> n2 "
        if n1 in self.PointSet and n2 in self.PointSet:
            self.EdgeValueDict[n1][n2] = self.EdgeValueDict[n2][n1] = value

    def changeEdgeValue(self, n1: str, n2: str, changeVal):
        "更改边权值"
        if n1 in self.PointSet and n2 in self.PointSet:
            self.EdgeValueDict[n1][n2] = self.EdgeValueDict[n2][n1] = max(
                1, self.EdgeValueDict[n1][n2]+changeVal)

    def changeAdjacentEdgeValue(self, toPoint, changeVal: int):
        '更改点连着的所有边的权值'
        if toPoint in self.PointSet:
            for x in self.EdgeValueDict[toPoint].keys():
                self.EdgeValueDict[toPoint][x] = self.EdgeValueDict[x][toPoint] = max(
                    1, self.EdgeValueDict[x][toPoint]+changeVal)

    def retAdjacentPoint_Value(self, toPoint: str)->dict:
        '返回相邻点及其权值'
        if toPoint in self.PointSet:
            return list(self.EdgeValueDict[toPoint])
        return None

    def judgeAtoB(self, APoint, BPoint):
        'A,B之间是否有边 ,有返回True'
        return APoint in self.PointSet and BPoint in self.EdgeValueDict[APoint].keys()

    def getAtoB(self, APoint, BPoint):
        '返回A-B的边权'
        if self.judgeAtoB(APoint, BPoint):
            return self.EdgeValueDict[APoint][BPoint]
        return None

    def _PrintDict(self):
        print(self.EdgeValueDict)

    @classmethod
    def creatOriginMap(cls):
        '返回一个由Distance_Edge_dict构建的初始边权图'
        edge = Edge_Map()
        for x, value in Distance_Edge_dict.items():
            edge.addPath(x[0], x[1], value)
        return edge

    @classmethod
    def retEdgeMap_Condition(self,condition: Condition, mode):
        '根据条件修改边权图'
        edge=Edge_Map.creatOriginMap()
        # 饭点
        if RiceTime.judge_riceTime(condition.nowtime):
            for riceP in RiceTime.rice_Point_tuple:
                edge.changeAdjacentEdgeValue(
                    riceP, RiceTime.rice_Point_value)

        # 高峰时间
        if ClassTime.judge_Rush_hour(condition.nowtime):
            for rushP in ClassTime.ClassTime_Point_tuple:
                edge.changeAdjacentEdgeValue(
                    rushP, ClassTime.ClassTime_Point_value)

        # 限速点
        if mode == Mode.CyclingMode or mode == Mode.DrivingMode:
            for limitP in SpeedLimit.SpeedLimit_Point_tuple:
                edge.changeAdjacentEdgeValue(
                    limitP, SpeedLimit.SpeedLimit_Point_value)
        return edge
