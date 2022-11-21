import turtle
import math
import random
from maps import levels

# Окно игры
wn = turtle.Screen()
wn.bgcolor("#ddd")
wn.title("Лабиринт")
wn.setup(700, 700)

#стены/серые квадратики
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#999")
        self.pu()
        self.speed(0)

#Игрок/зеленый квадратик
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.pu()
        self.speed(0)
        self.gold = 0

#движение игрока
    def go_up(self):
        x_cord = self.xcor()
        y_cord = self.ycor() + 24
        if (x_cord, y_cord) not in walls:
            self.goto(x_cord, y_cord)

    def go_down(self):
        x_cord = self.xcor()
        y_cord = self.ycor() - 24
        if (x_cord, y_cord) not in walls:
            self.goto(x_cord, y_cord)

    def go_right(self):
        x_cord = self.xcor() + 24
        y_cord = self.ycor()
        self.shape("square")
        if (x_cord, y_cord) not in walls:
            self.goto(x_cord, y_cord)

    def go_left(self):
        x_cord = self.xcor() - 24
        y_cord = self.ycor()
        self.shape("square")
        if (x_cord, y_cord) not in walls:
            self.goto(x_cord, y_cord)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 5:
            return True
        else:
            return False


#Выход/красный квадратик
class Exit(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#ff0000")
        self.pu()
        self.goto(x, y)

#Отображение экрана после прохождения
class EndScreen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pu()
        self.home()

#Размер и шрифт текста
    def viewScreen(self, tekst):
        FONT_SIZE = 14
        FONT = ("Arial", FONT_SIZE, "bold")
        self.home()
        self.sety(-FONT_SIZE / 2)
        self.write(tekst, align="center", font=FONT)
        self.hideturtle()
        screen = turtle.Screen()
        screen.exitonclick()

walls = []
exits = []
exitPos = []

#Игровое поле лабиринта/Правила
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            pole = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if pole == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if pole == 'P':
                player.goto(screen_x, screen_y)
            if pole == 'W':
                exitPos.append((screen_x, screen_y))
                exits.append(Exit(screen_x, screen_y))


#Управление игрока
pen = Pen()
player = Player()
wn.tracer(0)
wn.tracer(1)
turtle.listen()
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
wn.tracer(0)

setup_maze(random.choice(levels)) #Случайный выбор карты лабиринта

#Заголовок победы когда игрок доходит до выхода
while True:
    for exit in exits:
        if player.is_collision(exit):
            wn.clear()
            ending = EndScreen()
            ending.viewScreen("Победа! Нажмите на крестик окна или на экран чтобы закрыть игру")
    wn.update()
