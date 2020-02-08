# Day 3: Crossed Wires
# https://adventofcode.com/2019/day/3
import os
import sys

class Route:
    def __init__(self, direction, distance):
        self.direction, self.distance = direction, distance

    def __str__(self):
        return "{}, {}".format(self.direction, self.distance)


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)
    
    def __mod__(self, turn):
        if turn.direction == 'U':
            direction = 'up'
            print("Moving " + str(turn.distance) + " spaces to the " + direction)
            return Point(self.x, self.y + turn.distance)
        elif turn.direction == 'D':
            direction = 'down'
            print("Moving " + str(turn.distance) + " spaces to the " + direction)
            return Point(self.x, self.y - turn.distance)
        elif turn.direction == 'L':
            direction = 'left'
            print("Moving " + str(turn.distance) + " spaces to the " + direction)
            return Point(self.x - turn.distance, self.y)
        elif turn.direction == 'R':
            direction = 'right'
            print("Moving " + str(turn.distance) + " spaces to the " + direction)
            return Point(self.x + turn.distance, self.y)


if __name__ == '__main__':
    route_input = 'R75,D30,R83,U83,L12,D49,R71,U7,L72,U62,R66,U55,R34,D71,R55,D58,R83'
    route_raw = list(map(str, route_input.split(',')))
    route_sequence = [ Route(turn[0], int(turn[1:])) for turn in route_raw]
    
    starting_point = Point(0,0)
    latest_point = starting_point
    for route in route_sequence:
        latest_point = latest_point % route
        print("Latest point at " + str(latest_point))
