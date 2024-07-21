target_pos_x = 7
target_pos_y = 8

start_pos_x = 0
start_pos_y = 0
position = (start_pos_x, start_pos_y)

movement_x = 1
movement_y = 2

while position != (target_pos_x, target_pos_y):
    if movement_x == 1:
        position = (start_pos_x, start_pos_y)
        print(position)
        start_pos_x += movement_x
        start_pos_y += movement_y
        movement_x += 1
        movement_y -= 1
    else:
        position = (start_pos_x, start_pos_y)
        print(position)
        start_pos_x += movement_x
        start_pos_y += movement_y
        movement_x -= 1
        movement_y += 1
