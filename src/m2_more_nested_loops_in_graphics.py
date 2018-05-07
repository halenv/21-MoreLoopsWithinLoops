"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------

    c1 = rectangle.get_upper_left_corner()
    c2 = rectangle.get_lower_right_corner()
    dx = rectangle.get_width()
    dy = rectangle.get_height()

    count = 0
    for k in range(n):
        new_c1 = rg.Point(c1.x - (k * (1/2 * dx)), c1.y - (k * dy))
        new_c2 = rg.Point(c2.x - (k * (1/2 * dx)), c2.y - (k * dy))
        new_start = rg.Rectangle(new_c1, new_c2)
        new_start.attach_to(window)
        window.render(0.01)
        count = count + 1

        for j in range(count - 1):
            next_c1 = rg.Point(new_c1.x + ((j + 1) * dx), new_c1.y)
            next_c2 = rg.Point(new_c2.x + ((j + 1) * dx), new_c2.y)
            next_rect = rg.Rectangle(next_c1, next_c2)
            next_rect.attach_to(window)
            window.render(0.01)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
