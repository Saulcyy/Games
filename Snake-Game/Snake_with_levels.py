# Jeu de serpent simple en Python 3
# By Mona#6669

import turtle
import time
import random

delay = 0.1
level = 1

# Score
score = 0
high_score = 0

# Mise en place de l'affichage
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Tête du serpent
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Nourriture du serpent
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Stylo
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0  Level: 1", align="center", font=("Courier", 16, "normal"))


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


# Touches du clavier
wn.listen()
wn.onkeypress(go_up, "z")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "d")

# Boucle principale du jeu
while True:
    wn.update()

    # Vérifier s'il y a une collision avec la frontière
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
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

        # Reset niveaux
        level = 1

        pen.clear()
        pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                  font=("Courier", 16, "normal"))

    # Vérifier s'il y a une collision avec la nourriture
    if head.distance(food) < 20:
        # Déplacez la nourriture à un endroit aléatoire
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
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
        pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                  font=("Courier", 16, "normal"))

    # Déplacez d'abord les segments d'extrémité dans l'ordre inverse
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Déplacer le segment 0 à l'endroit où se trouve la tête
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Vérifiez que la tête n'entre pas en collision avec les segments du corps
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
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

            # Reset des niveaux
            level = 1

            # Mise à jour de l'affichage du score
            pen.clear()
            pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                      font=("Courier", 16, "normal"))

    # Niveaux
    if level == 1 and score == 50:
        level += 1
        delay *= 0.9
    if level == 2 and score == 100:
        level += 1
        delay *= 0.9
    if level == 3 and score == 150:
        level += 1
        delay *= 0.9
    if level == 4 and score == 200:
        level += 1
        delay *= 0.9
    if level == 5 and score == 250:
        level += 1
        delay *= 0.9
    if level == 6 and score == 300:
        level += 1
        delay *= 0.9
    if level == 7 and score == 350:
        level += 1
        delay *= 0.9
    if level == 8 and score == 400:
        level += 1
        delay *= 0.9
    if level == 9 and score == 450:
        level += 1
        delay *= 0.9
    if level == 10 and score == 500:
        level += 1
        delay *= 0.9
    if level == 11 and score == 550:
        level += 1
        delay *= 0.9
    if level == 12 and score == 600:
        level += 1
        delay *= 0.9
    if level == 13 and score == 650:
        level += 1
        delay *= 0.9
    if level == 14 and score == 700:
        level += 1
        delay *= 0.9
    if level == 15 and score == 750:
        level += 1
        delay *= 0.9
    if level == 16 and score == 800:
        level += 1
        delay *= 0.9
    if level == 17 and score == 850:
        level += 1
        delay *= 0.9
    if level == 18 and score == 900:
        level += 1
        delay *= 0.9
    if level == 19 and score == 950:
        level += 1
        delay *= 0.9
    if level == 20 and score == 1000:
        level += 1
        delay *= 0.9


    time.sleep(delay)

wn.mainloop()