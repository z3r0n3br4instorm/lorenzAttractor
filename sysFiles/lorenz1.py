import turtle
import math
import time
import sys
global alpha, sigma, beta, x, y, z, dt, dx, dy, dz, dtUpdate

def set_terminal_title(title):
    if sys.platform.startswith('win32'):
        # For Windows
        sys.stdout.write(f"\033]0;{title}\a")
    else:
        # For Unix-like systems (Linux, macOS, etc.)
        sys.stdout.write(f"\033]2;{title}\a")
    sys.stdout.flush()

def differentialEquations():
    global alpha, sigma, beta, x, y, z, dt, dx, dy, dz
    dx = alpha * (y - x) * dt
    dy = (x * (sigma - z) - y) * dt
    dz = (x * y - beta * z) * dt

def updateUI():
    global alpha, sigma, beta, x, y, z, dt, dx, dy, dz, dtUpdate
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.title("Lorenz Attractor Simulation :"+str(sys.argv[7]))
    screen.bgcolor("black")

    attractor_turtle = turtle.Turtle()
    attractor_turtle.speed(0)
    attractor_turtle.penup()
    attractor_turtle.color("white")

    # Move the turtle to the center of the screen
    attractor_turtle.goto(0,-20)

    print("initial:", x, y, z)
    while True:
        displayArray = [x,y,z]
        if math.isinf(x) or math.isinf(y) or math.isinf(z):
            attractor_turtle.goto(0,0)
        else:
            dt += dtUpdate
            differentialEquations()
            x = x + dx
            y = y + dy
            z = z + dz
            print((displayArray[int(sys.argv[5])]) , (displayArray[int(sys.argv[6])]))
            attractor_turtle.goto((displayArray[int(sys.argv[5])] * 10), (displayArray[int(sys.argv[6])] * 10))  # Scale the coordinates for better visualization
            attractor_turtle.pendown()
            attractor_turtle.dot(1)
if __name__ == "__main__":
    # Initial Values For alpha, beta, and sigma
    alpha = 10
    beta = 8/3
    sigma = 28
    set_terminal_title("Lorenz Attractor Simulation :"+str(sys.argv[7]))
    dtUpdate = float(sys.argv[1])
    dt = 0
    dx = 0
    dy = 0
    dz = 0
    x = float(sys.argv[2])
    y = float(sys.argv[3])
    z = float(sys.argv[4])
    print(x,y,z)
    time.sleep(1)
    updateUI()