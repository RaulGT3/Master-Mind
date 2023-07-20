from graphics import *
from random import seed, randint  # move these two line to the top of your main.cpp
from time import process_time

seed(process_time())
window = GraphWin('Master Mind', 360, 700)

h_circle_spacing = 5
palette_colors = ['green', 'orange', 'darkblue', 'yellow', 'darkred', 'lightblue']


def create_circle(center_x, center_y, radius, color):
    center = Point(center_x, center_y)
    circle = Circle(center, radius)
    circle.setOutline('black')
    circle.setFill(color)
    # circle.draw(window)
    return circle


def create_exit_circle(center_x, center_y, radius, ):
    exit = create_circle(center_x, center_y, radius, 'red')

    return exit


def create_color_palette(left_circle_center_x, left_circle_center_y, radius, palette_colors):
    color_pallet2 = []
    for color in palette_colors:
        circle_diameter = 2 * radius
        colors = create_circle(left_circle_center_x, left_circle_center_y, radius, color)
        left_circle_center_x += circle_diameter + h_circle_spacing
        color_pallet2.append(colors)
    return color_pallet2


def create_skel_circle(left_circle_center_x, left_circle_center_y, radius):
    skel_circle = []
    for color in range(4):
        circle_diameter = 2 * radius
        circle = create_circle(left_circle_center_x, left_circle_center_y, radius, 'white')
        left_circle_center_x += circle_diameter + h_circle_spacing
        skel_circle.append(circle)
    return skel_circle


def create_secret_code_colors(palette_colors):
    col = []
    for i in range(4):
        colo = palette_colors[randint(0, len(palette_colors) - 1)]
        col.append(colo)

    return col


def create_secret_code_circles(left_circle_center_x, left_circle_center_y, radius, secret_code_colors):
    s_code = []
    for colorss in secret_code_colors:
        circle_diameter = 2 * radius
        secreat_circles = create_circle(left_circle_center_x, left_circle_center_y, radius, colorss)
        left_circle_center_x += circle_diameter + h_circle_spacing
        s_code.append(secreat_circles)
    return s_code


def draw_circles(list_of_circles):
    for circle in list_of_circles:
        circle.draw(window)


def create_and_display_final_text(final_text_x, final_text_y, text_to_use):
    center_point = Point(final_text_x, final_text_y)
    text = Text(center_point, text_to_use)
    text.setSize(30)
    text.setStyle('italic')
    text.draw(window)
    text.setFill('gold')


def find_clicked_circle(click, list_of_circles):
    for i in range(len(list_of_circles)):
        list = list_of_circles[i]
        center_point = list.getCenter()
        radius = list.getRadius()

        if (center_point.getX() - click.getX()) ** 2 + (center_point.getY() - click.getY()) ** 2 <= radius * radius:
            return i

    return None


def is_click_in_circle(click, circle):
    center_point = circle.getCenter()
    radius = circle.getRadius()
    if (center_point.getX() - click.getX()) ** 2 + (center_point.getY() - click.getY()) ** 2 <= radius * radius:
        return True
    else:
        return False


def move_circles_up(circles, dy):
    for cir in circles:
        cir.move(0, -dy)
    window.update()


def guess_is_right(secret_code_colors, guess_colors):
    if secret_code_colors == guess_colors:
        return True
    else:
        return False


def create_feedback_skel(center_x, center_y, radius, color, length, hight):
    feed_back_circles = []
    for i in range(2):
        bottem_row = create_circle(center_x, center_y, radius, color)
        center_x += length
        feed_back_circles.append(bottem_row)
        for p in range(1):
            top_row = create_circle(center_x, center_y, radius, color)
            center_x -= length
            center_y -= hight
            feed_back_circles.append(top_row)

    return feed_back_circles


def create_feedback_circles(secret_code_colors, guess_code_colors, feedback_skel_circles):
    num_circles = 4
    feedback_circles = []
    guess_color_used = [False, False, False, False]
    secret_color_used = [False, False, False, False]
    feedback_idx = 0
    for i in range(num_circles):
        if secret_code_colors[i] == guess_code_colors[i]:
            guess_color_used[i] = secret_color_used[i] = True
            c = feedback_skel_circles[feedback_idx].clone()
            feedback_idx += 1
            c.setFill('red')
            feedback_circles.append(c)
    for i in range(num_circles):
        if not guess_color_used[i]:
            for j in range(num_circles):
                if not secret_color_used[j] and secret_code_colors[j] == guess_code_colors[i]:
                    c = feedback_skel_circles[feedback_idx].clone()
                    c.setFill('white')
                    feedback_circles.append(c)
                    feedback_idx += 1
                    secret_color_used[j] = True
                    break
    return feedback_circles


def main():
    g_window_width = 360
    g_window_height = 700
    circle_radius = 20

    leftmost_x = 50
    palette_y = g_window_height - 50
    guess_y = palette_y - 100
    guess_x = leftmost_x + circle_radius + h_circle_spacing
    exit_x = 10 + circle_radius
    exit_y = 30
    state_x = g_window_width - circle_radius - 5
    state_y = exit_y
    circle_width = 1
    secret_code_x = guess_x
    secret_code_y = 150
    hight = 50

    feedback_circle_radius = 5
    feedback_x = leftmost_x + 5 * circle_radius * 2 + 4 * h_circle_spacing + feedback_circle_radius
    feedback_y = guess_y + circle_radius - feedback_circle_radius
    feedback_h_spacing = 20
    feedback_v_spacing = 20



    random_coloers = create_secret_code_colors(palette_colors)

    skel_circles = create_circle(state_x, state_y, circle_radius, 'white')
    skel_circles.draw(window)

    skel_circles_4 = create_skel_circle(guess_x, guess_y, circle_radius)
    draw_circles(skel_circles_4)

    secreat_code = create_secret_code_circles(secret_code_x, secret_code_y, circle_radius, random_coloers)


    draw_circles(secreat_code)

    color_pallet = create_color_palette(leftmost_x, palette_y, circle_radius, palette_colors)
    draw_circles(color_pallet)
    exit_circle = create_exit_circle(exit_x, exit_y, circle_radius)
    exit_circle.draw(window)

    guesses = 0
    num_filled_guesses = 0
    num_rows = 8
    skel_circles_check = [False, False, False, False]
    skel_circles_check_true = [True, True, True, True]
    guess_circle_color = [None, None, None, None]

    while num_filled_guesses < num_rows:
        c_point = window.getMouse()
        if is_click_in_circle(c_point, exit_circle):
            window.close()
            return

        palette_idx = find_clicked_circle(c_point, color_pallet)

        if palette_idx is None:
            continue

        skel_circles.setFill(palette_colors[palette_idx])
        c_point = window.getMouse()
        idx = find_clicked_circle(c_point, skel_circles_4)

        if idx is None:
            skel_circles.setFill('white')

            continue
        num_clicks = skel_circles_check[idx] = True
        skel_circles_4[idx].setFill(palette_colors[palette_idx])
        guess_circle_color[idx] = (palette_colors[palette_idx])

        skel_circles.setFill('white')

        guesses += 1

        if None not in guess_circle_color:
            feedbackskel = create_feedback_skel(feedback_x, feedback_y, feedback_circle_radius, 'white',
                                                feedback_h_spacing, feedback_v_spacing)
            feed_back = create_feedback_circles(random_coloers, guess_circle_color, feedbackskel)
            draw_circles(feed_back)
            #feedback_y -= feedback_circle_radius *2 + feedback_v_spacing + feedback_v_spacing
            feedback_y -= feedback_circle_radius + feedback_v_spacing *2

        if skel_circles_check == skel_circles_check_true:

            row_color_checker = guess_is_right(random_coloers, guess_circle_color)

            if row_color_checker == True:
                break


            else:

                guess_y -= circle_radius + circle_radius + h_circle_spacing
                skel_circles_4 = create_skel_circle(guess_x, guess_y, circle_radius)

            if num_filled_guesses != num_rows - 1:
                draw_circles(skel_circles_4)
                num_filled_guesses += 1

            skel_circles_check = [False, False, False, False]
            guess_circle_color = [None, None, None, None]
    if num_filled_guesses == num_filled_guesses:
        guess_y += circle_radius - circle_radius - h_circle_spacing
        create_skel_circle(guess_x, guess_y, circle_radius)

    create_and_display_final_text(160, exit_y, "You Win!")

    window.getMouse()
    window.close()


main()
