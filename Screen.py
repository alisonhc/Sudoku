from graphics import*
from Remove import*
from Generation import*

def main():
    win = GraphWin("Sudoku", 522, 522)
    win.setBackground('OliveDrab3')
    rect = Rectangle(Point(29, 29), Point(497, 497))
    rect.setWidth(4)
    rect.draw(win)

    list1 = [Line(Point(185, 29), Point(185, 497)), Line(Point(341, 29), Point(341, 497)),
             Line(Point(29, 185), Point(497, 185)), Line(Point(29, 341), Point(497, 341))]
    for x in list1:
        x.setWidth(4)
        x.draw(win)

    list2 = [Line(Point(x, 29), Point(x, 497)) for x in (80, 131, 236, 287, 392, 443)]
    for x in list2:
        x.setWidth(1)
        x.draw(win)

    list3 = [Line(Point(29, x), Point(497, x)) for x in (80, 131, 236, 287, 392, 443)]
    for x in list3:
        x.setWidth(1)
        x.draw(win)

    def generateNums(grid):
        print(grid)
        num = [[Text(Point(x, y), i) for (x, i) in zip((55, 106, 157, 211, 262, 313, 367, 418, 469), j)]
               for (y, j) in zip((55, 106, 157, 211, 262, 313, 367, 418, 469), grid)]
        for y in num:
            for x in y:
                if x.getText() is not 0:
                    x.setSize(36)
                    x.setFace("arial")
                    x.draw(win)

    generateNums(make_full_grid(3))

    win.getMouse()
    win.getMouse()
    win.close()

main()
