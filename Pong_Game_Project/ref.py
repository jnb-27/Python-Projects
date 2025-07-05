def is_side_collision(ball, paddle):
    if ball.dx > 0:  # Only if moving toward paddle (right)
        within_x = (340 < ball.xcor() < 360)
        within_y = (paddle.ycor() - 50 < ball.ycor() < paddle.ycor() + 50)
        return within_x and within_y
    return False

def is_top_or_bottom_collision(ball, paddle):
    # Ball must be horizontally close to paddle to touch its top/bottom
    within_y_top = abs(ball.ycor() - (paddle.ycor() + 50)) < 10  # top edge
    within_y_bottom = abs(ball.ycor() - (paddle.ycor() - 50)) < 10  # bottom edge
    within_x = (paddle.xcor() - 10 < ball.xcor() < paddle.xcor() + 10)  # horizontally overlapping
    return (within_y_top or within_y_bottom) and within_x

# # Side collision (bounce on x-axis)
# if is_side_collision(ball, paddle):
#     ball.setx(340)  # Push it away from paddle
#     ball.dx *= -1

# # Top or bottom collision (bounce on y-axis)
# elif is_top_or_bottom_collision(ball, paddle):
#     # Determine whether to bounce up or down
#     if ball.ycor() > paddle.ycor():
#         ball.sety(paddle.ycor() + 60)  # push above top edge
#     else:
#         ball.sety(paddle.ycor() - 60)  # push below bottom edge
#     ball.dy *= -1