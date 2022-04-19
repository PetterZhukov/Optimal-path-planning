from datetime import time


"""
 包括
    模式信息
    点的信息
    边的信息
    特殊点、边
    条件信息
"""

# 模式信息


class Mode:
    WalkingMode = 'W'
    CyclingMode = 'C'
    DrivingMode = 'D'


# 地点信息
# 教学楼
BoBei = "博学北楼"
BoNan = "博学南楼"
DuBei = "笃行北楼"
DuNan = "笃行南楼"
SE_D_Building = "理工D楼"
SocialScience_Building = "社科楼"
# 宿舍
LiYuan = "李园"
JuYuan = "桔园"
# 食堂
LiuYuan_canteen = "榴园食堂"
JuYuan_canteen = "桔园食堂"
HuiYuan_canteen = "蕙园食堂"
MeiYuan_canteen = "梅园食堂"
# 体育馆
Gym = "体育馆"
North_Gym = "北体育馆"
South_Gym = "南体育馆"
# 其他
Carving = "石雕"

'所有点'
Map_Point_tuple = (
    # 教学楼
    BoBei,
    BoNan,
    DuBei,
    DuNan,
    SE_D_Building,
    SocialScience_Building,
    # 宿舍
    LiYuan,
    JuYuan,
    # 食堂
    LiuYuan_canteen,
    JuYuan_canteen,
    HuiYuan_canteen,
    MeiYuan_canteen,
    # 体育馆
    Gym,
    North_Gym,
    South_Gym,
    # 其他
    Carving,
)

'关于所有路径的边权集'
Distance_Edge_dict = {

    (HuiYuan_canteen, Gym): 194,
    (Gym, North_Gym): 300,
    (North_Gym, LiuYuan_canteen): 343,
    (North_Gym, SE_D_Building): 309,
    (LiuYuan_canteen, JuYuan_canteen): 242,
    (LiuYuan_canteen, BoBei): 258,
    (SE_D_Building, BoBei): 345,
    (JuYuan_canteen, JuYuan): 100,
    (JuYuan_canteen, LiYuan): 97,
    (JuYuan_canteen, JuYuan): 90,
    (LiYuan, DuBei): 143,
    (BoBei, DuBei): 144,
    (LiYuan, MeiYuan_canteen): 456,
    (LiYuan, DuNan): 379,
    (DuNan, BoNan): 124,
    (DuNan, MeiYuan_canteen): 258,
    (BoNan, Carving): 378,
    (MeiYuan_canteen, Carving): 434,
    (Carving, SocialScience_Building): 151,
    (Carving, South_Gym): 183,
    (DuBei, DuNan): 329,
    (BoBei, BoNan): 320,
    (JuYuan_canteen,BoBei):329,
}
'自行车停车点'
Bicycle_parking_point_tuple = (
    BoBei,
    BoNan,
    Gym,
    JuYuan_canteen,
    LiYuan,        
    LiuYuan_canteen,
    MeiYuan_canteen,
    South_Gym,
)
'汽车停车点'
Car_parking_point_tuple=(
    LiuYuan_canteen,
    SE_D_Building,
    SocialScience_Building,
)

"条件信息"
# '限速点'


class SpeedLimit:
    SpeedLimit_Point_tuple = (

    )
    SpeedLimit_Point_value = 200


# '上下课高峰'
class ClassTime:
    ClassTime_timedate_tuple = (
        (time(7, 30), time(8, 30)),
        (time(11, 40), time(12, 20)),
        (time(13, 40), time(14, 20)),
        (time(17, 0), time(17, 40)),
        (time(18, 40), time(19, 10)),
        (time(21, 10), time(21, 40)),
    )
    ClassTime_Point_tuple = (
        BoBei,
        BoNan,
    )
    ClassTime_Point_value = 300

    @classmethod
    def judge_Rush_hour(cls, judgeTime: time):
        '判断当前是不是高峰时间,是则 return True'
        res = False
        for t in cls.ClassTime_timedate_tuple:
            if t[0] <= judgeTime <= t[1]:
                res = True
                break
        return res


# '饭点'
class RiceTime:
    riceTime_tuple = (
        (time(11, 20), time(13, 00)),
        (time(17, 30), time(18, 30)),
    )
    rice_Point_tuple = (
        JuYuan_canteen,
    )
    rice_Point_value = -300

    @classmethod
    def judge_riceTime(cls, judgeTime: time):
        '判断当前是不是饭点,是则 return True'
        res = False
        for t in cls.riceTime_tuple:
            if t[0] <= judgeTime <= t[1]:
                res = True
                break
        return res


if __name__ == '__main__':
    print(RiceTime.rice_Point_tuple)
