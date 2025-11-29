import math

def collision(ball, brick):
    closest_x = max(brick.pos[0], min(ball.pos[0], brick.pos[0] + brick.width))
    closest_y = max(brick.pos[1], min(ball.pos[1], brick.pos[1] + brick.height))

    distance_x = closest_x - ball.pos[0]
    distance_y = closest_y - ball.pos[1]

    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

    if distance < ball.radius:
        if distance_x < distance_y:
            ball.x_speed = -ball.x_speed
        else:
            ball.y_speed = -ball.y_speed
        return True
    return False

def boundary_collision(ball, boundary):
    if ball.x_speed > 0 and ball.pos[0] > boundary.RIGHT_SIDE:
        ball.x_speed = -ball.x_speed
    if ball.x_speed < 0 and ball.pos[0] < boundary.LEFT_SIDE:
        ball.x_speed = -ball.x_speed
    if ball.y_speed < 0 and ball.pos[1] < boundary.TOP_SIDE:
        ball.y_speed = -ball.y_speed