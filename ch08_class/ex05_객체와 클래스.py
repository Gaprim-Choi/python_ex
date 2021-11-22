"""robot_name = 'R1'
robot_pos = 0

def robot_move():
    global robot_pos
    robot_pos = robot_pos + 1
    print("{0} postion: {1}".format(robot_name, robot_pos))

robot_move()

robot_name1 = 'R2'
robot_pos1 = 10

def robot_move1():
    global robot_pos1
    robot_pos1 = robot_pos1 + 1
    print("{0} postion: {1}".format(robot_name1, robot_pos1))

robot_move1()"""


class Robot():
    def __init__(self, name, pos):
        self.name =name
        self.pos = pos
    def move(self):
        self.pos =self.pos+1
        print("{0}{1}".format(self.name, self.pos))

robor1 = Robot("R1",1)
robor2 = Robot("R2",10)

robor1.move()
robor2.move()