import sys
import os

if __name__ == "__main__":
  odometer = 0
  depth = 0
  aim  = 0
  with open(os.path.join(sys.path[0], 'input.txt'), 'r') as moves:
    for move in moves:
      direction, units = move.split(" ")
      units = int(units)
      if direction == "forward":
        odometer += units
        depth += aim * units
      elif direction == "up":
        # depth -= units
        aim -= units
      elif direction == "down":
        # depth += units
        aim += units
      print("final: %s * %s = %s (aim=%s)" % (odometer, depth, odometer * depth, aim))
