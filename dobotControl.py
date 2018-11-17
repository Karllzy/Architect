import DobotDllType as dType
import mm
import numpy

"""##############################
用于机械臂的控制
修改人：李振业, 宁南鑫
最后修改日期：2018/11/17 8:44
##############################"""


class Architect:
    """
        用于控制机械臂进行搭建的类
    """

    def __init__(self, height=20, origin=(245, 150, -20)):
        """
        Initialization
        :param height
        :param origin:
        """
        self.api = dType.load()
        self.height = height
        self.origin = origin
        self.CON_STATE = {
            dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
            dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
            dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}  # Connection status dictionary

        self.COM_STATE = {
            dType.DobotCommunicate.DobotCommunicate_NoError: "No_Error",
            dType.DobotCommunicate.DobotCommunicate_BufferFull: "Buffer_Full",
            dType.DobotCommunicate.DobotCommunicate_Timeout: "Time_Out"}  # Command excution status dictionary
        self.mm = mm.Manger()

    def connect_and_home(self):
        """
        connect and return to zero
        :return:
        """
        # Communicate at 115200 baud rate and print communication status
        state = dType.ConnectDobot(self.api, "", 115200)[0]
        print("Connect status:", self.CON_STATE[state])

        if (state == dType.DobotConnect.DobotConnect_NoError):
            # Clear tasks from old queues
            dType.SetQueuedCmdClear(self.api)

            # Set motion parameters
            dType.SetHOMEParams(self.api, 250, 0, 50, 0, isQueued=1)
            dType.SetPTPJointParams(self.api, 200, 200, 200, 200,
                                    200, 200, 200, 200, isQueued=1)
            dType.SetPTPCommonParams(self.api, 100, 100, isQueued=1)

            # Return to zero
            dType.SetHOMECmd(self.api, temp=0, isQueued=1)
            # Execution command queue
            dType.SetQueuedCmdStartExec(self.api)

    def get_brick(self, brick_kind):
        """
        get the brick that the main function needed
        if the material is not enough it will return False
        or it will get the brick successfully and return True
        :param brick_kind:  the kind of needed brick
        :return: Boolean Value
        """
        position = self.mm.withdraw_brick(brick_kind)
        if position:
            x, y, z = position[0], position[1], position[2]
            dType.SetPTPCmd(self.api, dType.PTPMode.MOVJXYZMode, x, y, z, rHead=0, isQueued=1)
            dType.SetEndEffectorSuctionCup(self.api, enableCtrl=1, on=1, isQueued=1)
            self.raise_up()
            return x, y
        return False

    def build_layer(self, layer, height):
        """
        construct a standard floor
        :param layer:all the bricks' information
        :return:the position of break point if failed /False
        """
        for brick in layer:
            brick_kind = brick[2]
            if self.get_brick(brick_kind):
                # put the brick to the required place
                x = self.get_brick(brick_kind)[0]
                y = self.get_brick(brick_kind)[1]
                theta_1 = numpy.arctan(y / x)
                theta_2 = numpy.arctan(brick[0] / brick[1])
                R = theta_2 - theta_1

                x_1 = brick[0]
                y_1 = brick[1]
                dType.SetPTPCmd(self.api, dType.PTPMode.MOVJXYZMode,
                                x_1, y_1, height + 20, rHead=R, isQueued=1)
                dType.SetPTPCmd(self.api, dType.PTPMode.MOVJXYZMode,
                                x_1, y_1, height, rHead=R, isQueued=1)
                dType.SetEndEffectorSuctionCup(self.api, enableCtrl=1, on=0, isQueued=1)
                self.raise_up()
                return False
            else:
                return brick

    def raise_up(self, height=20):
        """
        rasie up the machine
        :return:
        """
        current_pose = dType.GetPose(self.api)
        dType.SetPTPCmd(self.api, dType.PTPMode.MOVJXYZMode,
                        current_pose[0], current_pose[1], current_pose[2] + height, rHead=0, isQueued=1)

    def build(self, model):
        """
        construct a model
        :param model: layer dictionary
        :return:
        """
        height = self.height
        for layer in model:
            break_point = self.build_layer(layer, height)
            if break_point:
                return break_point
            height += 20
        return False



