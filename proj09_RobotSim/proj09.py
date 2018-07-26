# proj09: Simulating robots
# Name:
# Date:

import math
import random

import proj09_visualize
# import pylab

# === Provided classes


class Position(object):
    """
    A Position represents a posation in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x = self.getX()
        old_y = self.getY()
        # Compute the change in position
        change_y = speed * math.cos(math.radians(angle))
        change_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + change_x
        new_y = old_y + change_y
        return Position(new_x, new_y)

# === Problems 1


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.cleaned = []
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
    
    def cleanTileAtPosition(self, pos):

        x = math.floor(pos.getX())

        y = math.floor(pos.getY())

        if (x, y) not in self.cleaned:
            self.cleaned.append((x, y))

        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """

    def isTileCleaned(self, m, n):

        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m,n) in self.cleaned
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return int(self.width)*int(self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return int(len(self.cleaned))

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        a = random.randint(0, self.width)
        b = random.randint(0, self.height)
        pos = Position(a, b)
        return pos

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return 0 <= pos.getX() and pos.getX() < self.width and 0 <= pos.getY() and pos.getY() < self.height


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        if speed > 0:
            self.speed = speed
        self.direct = int(360*random.random())
        self.pos = Position(1, 1)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direct

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direct = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        raise NotImplementedError


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        p1 = self.pos
        p2 = self.pos.getNewPosition(self.direct, self.speed)
        if self.room.isPositionInRoom(p2):
            self.pos = p2
            self.room.cleanTileAtPosition(self.pos)
        else:
            self.direct = int(360*random.random())

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    totaltime = 0
    num = num_trials
    while num > 0:
        anim = proj09_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        i = num_robots
        robots = []
        while i > 0:
            if robot_type == "StandardRobot":
                robots.append(StandardRobot(room, speed))
                i -= 1
        while min_coverage*room.getNumTiles() > room.getNumCleanedTiles():
            for robot in robots:
                robot.updatePositionAndClean()
            totaltime += 1
            anim.update(room, robots)
        num -= 1
        anim.done()
    return float(totaltime/num_trials)

runSimulation(10, 1, 10, 10, 1, 1, "StandardRobot")

# === Problem 4


def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    times1 = []
    for num_robots in range(1, 11):
        times1.append(runSimulation(num_robots, 1, 20, 20, .8, 1, "StandardRobot"))
    print times1

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    times2 = []
    times2.append(runSimulation(2, 1, 100, 4, .8, 1, "StandardRobot"))
    print times2

# === Problem 5


# class RandomWalkRobot(Robot):
#     """
#     A RandomWalkRobot is a robot with the "random walk" movement strategy: it
#     chooses a new direction at random after each time-step.
#     """
#     def updatePositionAndClean(self):
#         """
#         Simulate the passage of a single time-step.
#         Move the robot to a new position and mark the tile it is on as having
#         been cleaned.
#         """
#         self.direct = int(360 * random.random())
#         while not self.room.isPositionInRoom(self.pos.getNewPosition(self.direct, self.speed)):
#             self.direct = int(360 * random.random())
#         self.pos = self.pos.getNewPosition(self.direct, self.speed)
#         self.room.cleanTileAtPosition(self.pos)
#
#
# runSimulation(2, 1, 10, 10, 1, 2, "RandomWalkRobot")

# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    raise NotImplementedError
