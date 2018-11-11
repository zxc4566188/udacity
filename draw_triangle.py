import turtle

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("purple")
    rabbit = turtle.Turtle()
    rabbit.shape("turtle")
    cat = turtle.Turtle()
    cat.shape("arrow")
    dog = turtle.Turtle()
    for k in range(1,4):
        rabbit.forward(100)
        rabbit.right(120)
        dog.forward(100)
        dog.right(120)
        cat.forward(100)
        cat.right(120)
            
draw_triangle()


    
    
