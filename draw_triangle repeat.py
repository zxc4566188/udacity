import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("purple")
    rabbit = turtle.Turtle()
    rabbit.shape("turtle")
    for f in range(1,100000):
        for l in range(1,4):
            rabbit.forward(50)
            rabbit.right(120)
        rabbit.right(30)
        
draw_flower()


    
    
