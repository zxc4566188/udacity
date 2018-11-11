import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("purple")
    rabbit = turtle.Turtle()
    for l in range(1,5):
        rabbit.forward(100)
        rabbit.right(90)
   
    
    

    window.exitonclick()

draw_square()
