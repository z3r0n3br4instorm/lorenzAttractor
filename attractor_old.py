import turtle

global alpha, sigma, beta, x, y, z, dt, dx, dy, dz

# Initial Values For alpha, beta, and sigma
alpha = 10
beta = 8/3
sigma = 28
dt = 0.0001
dx = 0
dy = 0
dz = 0
x = 0.01
y = 0.0
z = 0.0

def differentialEquations():
    global alpha, sigma, beta, x, y, z, dt, dx, dy, dz
    dx = alpha * (y - x) * dt
    dy = (x * (sigma - z) - y) * dt
    dz = (x * y - beta * z) * dt

def updateUI():
    global alpha, sigma, beta, x, y, z, dt, dx, dy, dz
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.title("Lorenz Attractor")
    screen.bgcolor("black")

    attractor_turtle = turtle.Turtle()
    attractor_turtle.speed(0)
    attractor_turtle.penup()
    attractor_turtle.color("white")

    # Move the turtle to the center of the screen
    attractor_turtle.goto(0,-10)

    print("initial:", x, y, z, dx, dy, dz)
    try:
        while True:
            dt += 0.00001
            differentialEquations()
            x = x + dx
            y = y + dy
            z = z + dz
            print(x, y, z)
            attractor_turtle.goto(x * 10, y * 10)  # Scale the coordinates for better visualization
            attractor_turtle.pendown()
            attractor_turtle.dot(1)
    except:
        print("Value Reached to infinity !")

if __name__ == "__main__":
    updateUI()
