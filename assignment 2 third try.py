##this is a program in turtle that will draw a dart board


from turtle import *
def main() :

    shape("turtle")
    pendown()
    pencolor("yellow")
    pensize(5)
    speed(20)
    radius=200
    subradius=0
    forward(radius)
    left(90)
    sideCount = 0
    color = "yellow"
    
    while  sideCount <80:

            if sideCount>0 and sideCount<20:
                if color == "yellow":
                    color = "black"
                
                elif color== "black":
                      color="yellow"

            if sideCount==20:
                subradius=subradius+20
                home()
                forward(radius-subradius)
                left(90)
                
            if sideCount>20 and sideCount<40:
                if color == "yellow":
                    color = "black"
                
                elif color== "black":
                      color="yellow"

            if sideCount==40:
                subradius=subradius+80
                home()
                forward(radius-subradius)
                left(90)
                
            if sideCount>40 and sideCount<60:
                if color == "yellow":
                    color = "black"
                
                elif color== "black":
                      color="yellow"
                      
            if sideCount==60:
                ##stop
                subradius=subradius+10
                home()
                forward(radius-subradius)
                left(90)
                
            if sideCount>60 and sideCount<80:
                if color == "yellow":
                    color = "black"
                
                elif color== "black":
                      color="yellow"
                

            pencolor(color)
            fillcolor(color)
            circle(radius-subradius, 18)
            pendown()
            begin_fill()
            left(90)
            forward(radius-subradius)
            left(162)
            forward(radius-subradius)
            end_fill()
            left(90)
            circle(radius-subradius,18)
            penup()
            sideCount = sideCount + 1

    home()
    forward(30)
    begin_fill()
    pencolor("black")
    fillcolor("black")
    left(90)
    circle(30)
    end_fill()
    
    home()
    forward(20)
    begin_fill()
    pencolor("red")
    fillcolor("red")
    left(90)
    circle(20)
    end_fill()
    home()
                    

main()
