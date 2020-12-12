import turtle

def rel_pos():
    return [x1 - x2 for (x1, x2) in zip(waypoint.pos(), ship.pos())]

def waypoint_move(direction: str, distance: int):
    x, y = waypoint.pos()
    if direction == 'N':
        waypoint.setpos(x, y + distance)
    elif direction == 'S':
        waypoint.setpos(x, y - distance)
    elif direction == 'E':
        waypoint.setpos(x + distance, y)
    elif direction == 'W':
        waypoint.setpos(x - distance, y)
    else:
        raise NotImplementedError

def move_forward(times: int):
    for _ in range(times):
        diff_pos = rel_pos()
        ship.setpos(waypoint.pos())
        waypoint.setpos([x + y for (x, y) in zip(waypoint.pos(), diff_pos)])

def waypoint_rotate_clockwise(degrees: int):
    times = degrees // 90  # rotations only happen in 90 degree increments
    for _ in range(times):
        x_r, y_r = rel_pos()
        x_s, y_s = ship.pos()
        waypoint.setpos(x_s + y_r, y_s - x_r)

def waypoint_rotate_counter_clockwise(degrees: int):
    waypoint_rotate_clockwise(360 - degrees)  # TODO only does to 270 degrees

def do_action(action: str, value: int):
    if action == 'F':
        move_forward(value)
    elif action == 'R':
        waypoint_rotate_clockwise(value)
    elif action == 'L':
        waypoint_rotate_counter_clockwise(value)
    elif action in 'NSEW':
        waypoint_move(action, value)


# Setup turtle
turtle.hideturtle()
turtle.tracer(0, 0)

ship = turtle.Turtle()
ship.setpos(0, 0)
ship.clear()
ship.speed(0)

waypoint = turtle.Turtle()
waypoint.color('red')
waypoint.setpos(10, 1)
waypoint.clear()
ship.speed(0)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        instructions = [(line[0], int(line[1:]))
                        for line in f.read().splitlines()]

    for action, value in instructions:
        do_action(action, value)

    east, north = map(abs, ship.pos())
    print('A2:', int(east + north))

    turtle.update()
    turtle.done()
