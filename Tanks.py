#!/usr/bin/env python
# coding: utf-8}
from IPython.display import Audio
import turtle
import math
import random

# Set up screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Tanks war")

turtle.register_shape("space.gif")
audio_test = 'tanque_1.ogg'


def sound():
    bullet_sound = Audio(data=audio_test, autoplay=True)
    bullet_sound


# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


# make classes
class nave:
    def __init__(self, clr, angle, position, shape):
        self.angle = angle
        self.player = turtle.Turtle()
        self.player.color(clr)
        self.player.shape(shape)
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(position[0], position[1])
        self.player.setheading(angle)


class tank(nave):
    def __init__(self, clr, angle, position, shape):
        # create the player turtle
        nave.__init__(self, clr, angle, position, shape)
        self.playerspeed = 15
        self.movement = 90
        self.shot = Bullet()

    def move_forward(self):
        y = self.player.ycor()
        if y > -260:
            y = -260
        y += self.playerspeed
        self.player.sety(y)

    def move_right(self):
        x = self.player.xcor()
        if x > 280:
            x = 280
        x += self.playerspeed
        self.player.setx(x)

    def move_left(self):
        x = self.player.xcor()
        x -= self.playerspeed
        if x < -280:
            x = - 280
        self.player.setx(x)

    def move_back(self):
        y = self.player.ycor()
        if y < -280:
            y = -280
        y -= self.playerspeed
        self.player.sety(y)

    def fire(self):
        if self.shot.state == "ready":
            sound()
            self.shot.state = "fire"
            x = self.player.xcor()
            y = self.player.ycor() + 10
            self.shot.bullet.setposition(x, y)
            self.shot.bullet.showturtle()


class Bullet:
    speedbullet = 30
    state = "ready"

    def __init__(self):
        # create the player´s bullet
        self.bullet = turtle.Turtle()
        self.bullet.color("black")
        self.bullet.shape("triangle")
        self.bullet.penup()
        self.bullet.speed(0)
        self.bullet.setheading(90)
        self.bullet.shapesize(0.5, 0.5)
        self.bullet.hideturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


number_of_enemies = 5

# create an empty list fo enemies
enemies = []

# Add enemies to list
for i in range(number_of_enemies):
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    # create the enemy
    enemies.append(nave(clr="red", angle=0, position=[x, y], shape="circle"))

jugador1 = tank(clr="red", angle=90, position=[0, -250], shape="space.gif")

jugador2 = tank(clr="blue", angle=90, position=[0, -260], shape="space.gif")

# Create keyboard bindings
turtle.listen()
turtle.onkey(jugador1.move_forward, "Up")
turtle.onkey(jugador1.move_right, "Right")
turtle.onkey(jugador1.move_left, "Left")
turtle.onkey(jugador1.move_back, "Down")
turtle.onkey(jugador1.fire, "space")

turtle.onkey(jugador2.move_forward, "w")
turtle.onkey(jugador2.move_right, "d")
turtle.onkey(jugador2.move_left, "a")
turtle.onkey(jugador2.move_back, "s")
turtle.onkey(jugador2.fire, "x")

enemyspeed = 2

while True:
    perder = 0
    for enemy in enemies:
        # Move the enemy
        x = enemy.player.xcor()
        x += enemyspeed
        enemy.player.setx(x)

        # Move the enemy back and down
        if enemy.player.xcor() > 280:
            # move all enemies down
            for e in enemies:
                y = e.player.ycor()
                y -= 40
                e.player.sety(y)
            # change enemy direction
            enemyspeed *= -1

        if enemy.player.xcor() < -280:
            # move all enemies down
            for e in enemies:
                y = e.player.ycor()
                y -= 40
                e.player.sety(y)
            # change enemy direction
            enemyspeed *= -1
        if enemy.player.ycor() < -280:
            perder = 1

        # check for the colition between the bullet and the enemy
        if isCollision(jugador1.shot.bullet, enemy.player):
            # Reset the bullet
            jugador1.shot.bullet.hideturtle()
            jugador1.shot.state = "ready"
            jugador1.shot.bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.player.setposition(x, y)

        if isCollision(jugador2.shot.bullet, enemy.player):
            # Reset the bullet
            jugador2.shot.bullet.hideturtle()
            jugador2.shot.state = "ready"
            jugador2.shot.bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.player.setposition(x, y)
        # move the bullet

    if perder == 1:
        print("Game over")
        break
    if jugador1.shot.state == "fire":
        y = jugador1.shot.bullet.ycor()
        y += jugador1.shot.speedbullet
        jugador1.shot.bullet.sety(y)
    # Chek to see if the bullet has gone to the top
    if jugador1.shot.bullet.ycor() > 275:
        jugador1.shot.bullet.hideturtle()
        jugador1.shot.state = "ready"

    if jugador2.shot.state == "fire":
        y = jugador2.shot.bullet.ycor()
        y += jugador2.shot.speedbullet
        jugador2.shot.bullet.sety(y)

    # Chek to see if the bullet has gone to the top
    if jugador2.shot.bullet.ycor() > 275:
        jugador2.shot.bullet.hideturtle()
        jugador2.shot.state = "ready

