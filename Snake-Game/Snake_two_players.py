# Jeu de serpent simple en Python 3
# By Mona#6669

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Mise en place de l'affichage
wn = turtle.Screen()
wn.title("Snake Game by Mona#6669")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Tête du serpent
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(-100, 0)
head.direction = "stop"

# Tête du serpent 2
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("blue")
head2.penup()
head2.goto(100, 0)
head2.direction = "stop"

# Nourriture du serpent
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
segments2 = []

# Stylo
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Fonctions
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
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def go_up2():
    if head2.direction != "down":
        head2.direction = "up"


def go_down2():
    if head2.direction != "up":
        head2.direction = "down"


def go_left2():
    if head2.direction != "right":
        head2.direction = "left"


def go_right2():
    if head2.direction != "left":
        head2.direction = "right"


def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y + 20)

    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)

    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)

    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)


# Touches du clavier
wn.listen()
wn.onkeypress(go_up, "z")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_up2, "i")
wn.onkeypress(go_down2, "k")
wn.onkeypress(go_left2, "j")
wn.onkeypress(go_right2, "l")

# Boucle principale du jeu
while True:
    wn.update()

    # Vérifier s'il y a une collision avec la frontière
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(-100, 0)
        head.direction = "stop"

        # Cacher les segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Effacer la liste des segments
        segments.clear()

        # Reset du score
        score = 0

        # Reset du délai
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Vérifier s'il y a une collision avec la frontière
    if head2.xcor() > 290 or head2.xcor() < -290 or head2.ycor() > 290 or head2.ycor() < -290:
        time.sleep(1)
        head2.goto(100, 0)
        head2.direction = "stop"

        # Cacher les segments
        for segment2 in segments2:
            segment2.goto(1000, 1000)

        # Effacer la liste des segments
        segments2.clear()

        # Reset du score
        score = 0

        # Reset du délai
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Vérifier s'il y a une collision avec la nourriture
    if head.distance(food) < 20:
        # Déplacez la nourriture à un endroit aléatoire
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)

        # Ajouter un segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Raccourcir le délai
        delay -= 0.001

        # Augmenter le score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Vérifier s'il y a une collision avec la nourriture
    if head2.distance(food) < 20:
        # Déplacez la nourriture à un endroit aléatoire
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)

        # Ajouter un segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments2.append(new_segment)

        # Raccourcir le délai
        delay -= 0.001

        # Augmenter le score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Déplacez d'abord les segments d'extrémité dans l'ordre inverse
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Déplacez d'abord les segments d'extrémité dans l'ordre inverse
    for index in range(len(segments2) - 1, 0, -1):
        x = segments2[index - 1].xcor()
        y = segments2[index - 1].ycor()
        segments2[index].goto(x, y)

    # Déplacer le segment 0 à l'endroit où se trouve la tête
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Déplacer le segment 0 à l'endroit où se trouve la tête
    if len(segments2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x, y)

    move()
    move2()

    # Vérifiez que la tête n'entre pas en collision avec les segments du corps
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(-100, 0)
            head.direction = "stop"

            # Cacher les segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Effacer la liste des segments
            segments.clear()

            # Reset du score
            score = 0

            # Reset du délai
            delay = 0.1

            # Mise à jour de l'affichage du score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    # Vérifiez que la tête n'entre pas en collision avec les segments du corps
    for segment2 in segments2:
        if segment2.distance(head) < 20:
            time.sleep(1)
            head2.goto(100, 0)
            head2.direction = "stop"

            # Cacher les segments
            for segment2 in segments2:
                segment2.goto(1000, 1000)

            # Effacer la liste des segments
            segments2.clear()

            # Reset du score
            score = 0

            # Reset du délai
            delay = 0.1

            # Mise à jour de l'affichage du score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()