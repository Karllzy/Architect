import DobotDllType as dType
import math

"""##############################
用于机械臂的控制
修改人：李振业
最后修改日期：2018/11/14 23.07
##############################"""


class Architect:
    """
        用于控制机械臂进行搭建的类
    """
    def __init__(self, ground_height=-20, origin=(245, 150, -20)):
        """
        初始化
        :param ground_height:地面的高度
        :param origin: 搭建坐标系的起始点
        """
        self.ground_height = ground_height
        self.origin = origin

    def build_layer(self, shape):
        pass

    def build_wall(self, shape):
        pass

