import turtle as t
import random
import time

delay = 0.1
score = 0
high_score = 0

sc = t.Screen()
sc.title("Snake Game")
sc.bgcolor("blue")
sc.setup(width=600, height=600)
sc.tracer(0)

head = t.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = t.Turtle()
food.speed(0)
food.shape(random.choice(['square', 'triangle', 'circle']))
food.color(random.choice(['red', 'green', 'black']))
food.penup()
food.goto(0, 100)

pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

sc.listen()
sc.onkeypress(go_up, "Up")
sc.onkeypress(go_down, "Down")
sc.onkeypress(go_left, "Left")
sc.onkeypress(go_right, "Right")

segments = []

try:
    while True:
        sc.update()

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            food.goto(random.randint(-270, 270), random.randint(-270, 270))
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, "bold"))

        if head.distance(food) < 20:
            food.goto(random.randint(-270, 270), random.randint(-270, 270))
            new_segment = t.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("orange")
            new_segment.penup()
            segments.append(new_segment)
            delay = max(0.05, delay - 0.001)
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, "bold"))

        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

        if len(segments) > 0:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "Stop"
                food.goto(random.randint(-270, 270), random.randint(-270, 270))
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, "bold"))

        time.sleep(delay)

except t.Terminator:
    print("Game closed gracefully.")
