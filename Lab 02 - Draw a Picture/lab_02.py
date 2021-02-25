"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

def print_butterfly(x, y, ancho, alto, angulo, color_rgb):
    """float*5, tuple-->mariposa
    OBJ: dibujar mariposa con parámetros"""
    arcade.draw_ellipse_filled(x, y, ancho, alto, color_rgb, -angulo)
    arcade.draw_ellipse_filled(x, y-10, ancho, alto-10, color_rgb)
    arcade.draw_ellipse_filled(x+20, y, ancho, alto, color_rgb, angulo)
    arcade.draw_ellipse_filled(x+20, y-10, ancho, alto-10, color_rgb)

def print_flower(x,y,ancho,alto,rgb_color):
    """float*4,tuple-->flor
    OBJ: dibujar una flor"""
    arcade.draw_ellipse_filled(x-7, y, ancho, alto, rgb_color)
    arcade.draw_ellipse_filled(x, y+5, ancho, alto, rgb_color)
    arcade.draw_ellipse_filled(x+7, y, ancho, alto, rgb_color)
    arcade.draw_ellipse_filled(x, y-5, ancho, alto, rgb_color)
    arcade.draw_ellipse_filled(x, y, ancho, alto, arcade.color.CHROME_YELLOW)

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.COAL)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 350, 0, arcade.color.BUD_GREEN)
arcade.draw_lrtb_rectangle_filled(0, 800, 350, 315, (214, 188, 71))

# Drawing the 'river'
arcade.draw_rectangle_filled(400, 200, 80, 1000, arcade.color.CORNFLOWER_BLUE, 80)
'''
arcade.draw_line(100, 170, 170, 182, (51, 110, 214))
arcade.draw_line(100, 160, 170, 162, (51, 110, 214))
arcade.draw_line(100, 170, 170, 182, (51, 110, 214))'''


# Draw the mountains
arcade.draw_triangle_filled(-100, 350, 150, 500, 320, 350, arcade.color.DARK_GRAY)
arcade.draw_triangle_filled(200, 350, 400, 450, 600, 350, arcade.color.DARK_GRAY)
arcade.draw_triangle_filled(400, 350, 650, 475, 850, 350, arcade.color.DARK_GRAY)

# Draw the sun
arcade.draw_circle_filled(300, 530, 50, arcade.color.CHROME_YELLOW)

# Drawing some flowers
print_flower(496,100,12,9,(255,255,255))
print_flower(443,127,12,9,(255,255,255))
print_flower(538,80,12,9,(255,255,255))
print_flower(550,119,12,9,(255,255,255))
print_flower(425,97,12,9,(255,255,255))

# Drawing a tree
arcade.draw_ellipse_filled(620, 100, 150, 40, arcade.color.DARK_GREEN)
arcade.draw_lrtb_rectangle_filled(600, 640, 250, 100, arcade.color.FRENCH_BEIGE)
arcade.draw_triangle_filled(550, 240, 620, 350, 690, 240, arcade.color.FOREST_GREEN)
arcade.draw_triangle_filled(560, 310, 620, 420, 680, 310, arcade.color.FOREST_GREEN)
arcade.draw_triangle_filled(570, 380, 620, 460, 670, 380, arcade.color.FOREST_GREEN)

arcade.draw_line(580, 100, 570, 120, arcade.color.FOREST_GREEN)
arcade.draw_line(580, 100, 580, 120, arcade.color.FOREST_GREEN)
arcade.draw_line(580, 100, 590, 120, arcade.color.FOREST_GREEN)

arcade.draw_line(620, 80, 610, 100, arcade.color.FOREST_GREEN)
arcade.draw_line(620, 80, 620, 100, arcade.color.FOREST_GREEN)
arcade.draw_line(620, 80, 630, 100, arcade.color.FOREST_GREEN)

arcade.draw_line(660, 110, 650, 130, arcade.color.FOREST_GREEN)
arcade.draw_line(660, 110, 660, 130, arcade.color.FOREST_GREEN)
arcade.draw_line(660, 110, 670, 130, arcade.color.FOREST_GREEN)

arcade.draw_ellipse_filled(475, 50, 150, 40, arcade.color.DARK_GREEN)
arcade.draw_lrtb_rectangle_filled(455, 495, 200, 50, arcade.color.FRENCH_BEIGE)
arcade.draw_triangle_filled(405, 190, 470, 300, 545, 190, arcade.color.FOREST_GREEN)
arcade.draw_triangle_filled(415, 260, 470, 370, 535, 260, arcade.color.FOREST_GREEN)
arcade.draw_triangle_filled(425, 330, 470, 410, 525, 330, arcade.color.FOREST_GREEN)

arcade.draw_line(540, 50, 530, 70, arcade.color.FOREST_GREEN)
arcade.draw_line(540, 50, 540, 70, arcade.color.FOREST_GREEN)
arcade.draw_line(540, 50, 550, 70, arcade.color.FOREST_GREEN)

arcade.draw_line(480, 33, 470, 53, arcade.color.FOREST_GREEN)
arcade.draw_line(480, 33, 480, 53, arcade.color.FOREST_GREEN)
arcade.draw_line(480, 33, 490, 53, arcade.color.FOREST_GREEN)

arcade.draw_line(450, 45, 440, 65, arcade.color.FOREST_GREEN)
arcade.draw_line(450, 45, 450, 65, arcade.color.FOREST_GREEN)
arcade.draw_line(450, 45, 460, 65, arcade.color.FOREST_GREEN)

# Drawing flowers
print_flower(100,50,12,9,(255,255,255))
print_flower(247,77,12,9,(255,255,255))
print_flower(198,30,12,9,(255,255,255))
print_flower(215,89,12,9,(255,255,255))
print_flower(48,37,12,9,(255,255,255))
print_flower(153,47,12,9,(255,255,255))
print_flower(593,87,12,9,(255,255,255))
print_flower(375,50,12,9,(255,255,255))
print_flower(625,47,12,9,(255,255,255))
print_flower(437,30,12,9,(255,255,255))
print_flower(314,69,12,9,(255,255,255))
print_flower(279,37,12,9,(255,255,255))
print_flower(394,127,12,9,(255,255,255))

# Drawing clouds
arcade.draw_circle_filled(450, 530, 20, arcade.color.WHITE)
arcade.draw_circle_filled(475, 530, 25, arcade.color.WHITE)
arcade.draw_circle_filled(500, 530, 30, arcade.color.WHITE)
arcade.draw_circle_filled(525, 530, 25, arcade.color.WHITE)
arcade.draw_circle_filled(550, 530, 20, arcade.color.WHITE)

arcade.draw_circle_filled(675, 550, 17, arcade.color.WHITE)
arcade.draw_circle_filled(700, 550, 20, arcade.color.WHITE)
arcade.draw_circle_filled(725, 550, 17, arcade.color.WHITE)

arcade.draw_circle_filled(50, 580, 40, arcade.color.WHITE)
arcade.draw_circle_filled(100, 580, 50, arcade.color.WHITE)
arcade.draw_circle_filled(150, 580, 40, arcade.color.WHITE)

# Drawing butterflies
print_butterfly(100,400,15,30,30,(255,255,255))
print_butterfly(120,437,15,30,30,(115, 183, 217))
print_butterfly(168,380,15,30,30,(209, 195, 0))
print_butterfly(134,324,15,30,30,(255,255,255))
print_butterfly(75,364,15,30,30,(196, 64, 31))
print_butterfly(77,440,15,30,30,(224, 122, 58))
print_butterfly(176,343,15,30,30,(219, 103, 219))
print_butterfly(118,376,15,30,30,(140, 41, 194))

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()