# futval_graph.py

from graphics import *


def main():
    # Introduction
    print("This program draws a plot investment in 10 years")

    # Get principal and interest rate.
    principal = eval(input("Enter the initial Principal: "))
    rt = eval(input("Enter the interest rate: "))

    # Create a graphics window
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), '0.0k').draw(win)
    Text(Point(20, 190), '10.0k').draw(win)
    Text(Point(20, 150), '12.0k').draw(win)
    Text(Point(20, 110), '14.0k').draw(win)
    Text(Point(20, 70), '16.0k').draw(win)
    Text(Point(20, 30), '18.0k').draw(win)

    # Draw lines
    line = Line(Point(40, 230), Point(40, 1))
    line.draw(win)
    line2 = Line(Point(40, 230), Point(319, 230))
    line2.draw(win)

    # Draw bar for initial bar.
    height = 10000 * 0.004 + (principal - 10000) * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years.
    for year in range(1, 10):
        # Calculate the principal for the next year
        principal = principal * (1 + (rt / 100))
        height2 = 40 + (principal - 10000) * 0.02
        # draw bar for successive years
        y = year * 25 + 40
        bar2 = Rectangle(Point(y, 230), Point(y + 25, 230 - height2))
        bar2.setFill('green')
        bar2.setWidth(2)
        bar2.draw(win)

    input("Press <Enter> to quit")
    win.close()


main()
