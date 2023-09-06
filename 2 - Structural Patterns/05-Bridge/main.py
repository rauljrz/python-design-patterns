from drawingapione import DrawingAPIOne
from drawingapitwo import DrawingAPITwo
from circle import Circle

def main():
    #Build the first Circle object using API One
    circle1 = Circle(1, 2, 3, DrawingAPIOne())
    #Draw a circle
    circle1.draw()

    #Build the second Circle object using API Two
    circle2 = Circle(2, 3, 4, DrawingAPITwo())

    #Draw a circle
    circle2.draw()


if __name__=="__main__":
    main()