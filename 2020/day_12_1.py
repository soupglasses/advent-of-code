import sys
import turtle
from typing import Optional


def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = [(line[0], int(line[1:]))
            for line in raw.splitlines()]
    return data



DIRECTIONS = {'N': 90, 'S': 270, 'E': 0, 'W': 180}


def move_direction(direction: str, distance: int):
    old_heading = turtle.heading()
    direction = DIRECTIONS[direction]
    turtle.setheading(direction)
    turtle.forward(distance)
    turtle.setheading(old_heading)

def do_action(action: str, value: int):
    if action == 'F':
        turtle.forward(value)
    elif action == 'L':
        turtle.left(value)
    elif action == 'R':
        turtle.right(value)
    elif action in 'NSEW':
        move_direction(action, value)
    else:
        raise NotImplementedError


if __name__ == '__main__':
    turtle.speed(0)                # max speed
    turtle.tracer(False)           # disable screen refresh
    turtle.screensize(4000, 4000)  # allow scrolling canvas

    instructions = parse_data("inputs/example_12.txt")

    for action, value in instructions:
        do_action(action, value)

    east, north = map(abs, turtle.pos())
    print('A1:', int(east + north))

    turtle.update()  # update screen
    turtle.done()    # show screen till closed
