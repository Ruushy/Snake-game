from turtle import Turtle
ALIGHMENT = "center"
FONT = ("Arial" , 25 , "normal")

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0 , 265)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score} " , align=ALIGHMENT , font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(" Game Over ", align=ALIGHMENT, font=FONT)
    def increase(self):
        self.score +=1
        self.clear()
        self.update()