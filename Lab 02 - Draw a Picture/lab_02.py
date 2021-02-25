"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

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

# Drawing flowers
arcade.draw_ellipse_filled(93, 50, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(100, 55, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(107, 50, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(100, 45, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(100, 50, 12, 9, arcade.color.CHROME_YELLOW)

arcade.draw_ellipse_filled(140, 77, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(147, 82, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(154, 77, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(147, 72, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(147, 77, 12, 9, arcade.color.CHROME_YELLOW)

arcade.draw_ellipse_filled(121, 25, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(128, 30, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(135, 25, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(128, 20, 12, 9, arcade.color.WHITE)
arcade.draw_ellipse_filled(128, 25, 12, 9, arcade.color.CHROME_YELLOW)


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


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()