""" Nome do módulo :        com_kernel
    Ano de criação :        2020/01
    Descrição do módulo :   kernel de comunicação com o vss-sdk
    Versão :                1.0
    Pré-requisitos :        vss-core-py
    Membros :               Lorena "Ino" Bassani
"""

# begin-imports
from vsscorepy.communications.command_sender import CommandSender
from vsscorepy.communications.debug_sender import DebugSender
from vsscorepy.communications.state_receiver import StateReceiver
from vsscorepy.domain.command import Command
from vsscorepy.domain.wheels_command import WheelsCommand
from vsscorepy.domain.point import Point
from vsscorepy.domain.pose import Pose
from vsscorepy.domain.debug import Debug
from vsscorepy.domain.state import State
# end-imports


class Kernel(object):
    state_receiver = None
    command_sender = None
    debug_sender = None

    def __init__(self):
        self.state_receiver = StateReceiver()
        self.state_receiver.create_socket()

        self.command_sender = CommandSender()
        self.command_sender.create_socket()

        self.debug_sender = DebugSender()
        self.debug_sender.create_socket()


    def __build_command(self, rvel):
        command = Command()
        command.wheels_commands.append(WheelsCommand(rvel[0][0], rvel[0][1]))
        command.wheels_commands.append(WheelsCommand(rvel[1][0], rvel[1][1]))
        command.wheels_commands.append(WheelsCommand(rvel[2][0], rvel[2][1]))
        return command

    def __build_debug(self, robots_points):
        debug = Debug()
        debug.clean()

        for robot_points in robots_points:
            points = robot_points["step_points"]
            end_pose = robot_points["end_pose"]

            for point in points:
                debug.step_points.append(Point(point[0], point[1]))
            debug.final_poses.append(
                    Pose(end_pose[0], end_pose[1] + end_pose[2]))
    
    def receive_state(self):
        return self.state_receiver.receive_state()
    
    def send_command(self, rvel):
        self.command_sender.send_command(self.__build_command(rvel))

    def send_debug(self, robots_points):
        self.debug_sender.send_debug(self.__build_debug(robots_points))
    

def state_to_dict(state : State):
    dict_ball = {
        "x" : state.ball.x, 
        "y" : state.ball.y,
        "speed_x" : state.ball.speed_x,
        "speed_y" : state.ball.speed_y,
    }
    team_yellow = list()
    for state_robot in state.team_yellow:
        team_yellow.append(
            {
                "x" : state_robot.x,
                "y" : state_robot.y,
                "angle" : state_robot.angle,
                "speed_x" : state_robot.speed_x,
                "speed_y" : state_robot.speed_y,
                "speed_angle" : state_robot.speed_angle,
            }
        )
    team_blue = list()
    for state_robot in state.team_blue:
        team_blue.append(
            {
                "x" : state_robot.x,
                "y" : state_robot.y,
                "angle" : state_robot.angle,
                "speed_x" : state_robot.speed_x,
                "speed_y" : state_robot.speed_y,
                "speed_angle" : state_robot.speed_angle,
            }
        )
    return {"ball" : dict_ball, "team_yellow" : team_yellow, "team_blue" : team_blue,}