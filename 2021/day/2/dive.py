import sys
import os

if __name__ == "__main__":
  odometer = 0
  depth = 0
  with open(os.path.join(sys.path[0], 'input.txt'), 'r') as moves:
    for move in moves:
      direction, units = move.split(" ")
      if direction == "forward":
        odometer += int(units)
      elif direction == "up":
        depth -= int(units)
      elif direction == "down":
        depth += int(units)
      print("final: %s * %s = %s" % (odometer, depth, odometer * depth))
