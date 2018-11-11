import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")
    rabbit = turtle.Turtle()
    rabbit.shape("arrow")
    rabbit.color("yellow")
    for f in range(1,37):
        for l in range(1,5):
            rabbit.forward(100)
            rabbit.right(90)
        rabbit.right(10)
        
draw_flower()


    
    
