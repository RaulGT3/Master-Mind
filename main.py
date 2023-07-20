from graphics import *
from random import seed, randint # move these two line to the top of your main.cpp
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
      #circle.draw(window)
      return circle



def create_exit_circle(center_x, center_y, radius,):

    exit2 = []
    exit = create_circle(center_x,center_y ,radius,'red')
    exit2.append(exit)
    return exit2




def create_color_palette(left_circle_center_x, left_circle_center_y, radius, palette_colors):
    color_pallet2 =[]
    for color in palette_colors:
        circle_diameter = 2 * radius
        colors  = create_circle(left_circle_center_x, left_circle_center_y, radius, color)
        left_circle_center_x += circle_diameter + h_circle_spacing
        color_pallet2.append(colors)
    return color_pallet2


def create_skel_circle(left_circle_center_x, left_circle_center_y, radius):
    skel_circle = []
    for color in range(4):
        circle_diameter = 2 * radius
        circle  = create_circle(left_circle_center_x, left_circle_center_y, radius, 'white')
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
    s_code =[]
    for colorss in secret_code_colors:
        circle_diameter = 2 * radius
        secreat_circles = create_circle(left_circle_center_x, left_circle_center_y, radius, colorss)
        left_circle_center_x += circle_diameter + h_circle_spacing
        s_code.append(secreat_circles)
    return s_code



def draw_circles(list_of_circles):
    for circle in list_of_circles:
        circle.draw(window)


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
    state_x = g_window_width - circle_radius-5
    state_y = exit_y
    circle_width = 1
    secret_code_x = guess_x
    secret_code_y = 150

    random_coloers = create_secret_code_colors(palette_colors)


    skel_circles = create_skel_circle(state_x, state_y, circle_radius)
    draw_circles(skel_circles)

    skel_circles_4 = create_skel_circle(guess_x, guess_y, circle_radius)
    draw_circles(skel_circles_4)

    secreat_code = create_secret_code_circles(secret_code_x, secret_code_y, circle_radius, random_coloers)

    draw_circles(secreat_code)


    color_pallet = create_color_palette(leftmost_x, palette_y, circle_radius, palette_colors)
    draw_circles(color_pallet)
    exit_circle = create_exit_circle(exit_x, exit_y, circle_radius)
    draw_circles(exit_circle)



    # perhpas more code here...
    #mouse_click = window.getMouse()
    #if is_click_in_circle(mouse_click, exit_circle):
        #window.close()
    #return  # return from "main" will terminate the program.
    #elif  # the rest of the conditions here.
    # the rest of the code here...





    window.getMouse()
    window.close()

main()

