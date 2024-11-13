import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Dibujo de Yoseth Lima Tola")
screen.bgcolor("lightblue")

# Texto de nombre
name = turtle.Turtle()
name.hideturtle()
name.color("black")
name.penup()
name.goto(0, 200)
name.write("Yoseth Lima Tola", align="center", font=("Arial", 20, "bold"))

# Dibujo de la cabeza
head = turtle.Turtle()
head.shape("circle")
head.color("peachpuff")
head.shapesize(2)  # Tamaño de la cabeza
head.penup()
head.goto(0, 100)


# Dibujo del cuerpo
body = turtle.Turtle()
body.color("black")
body.pensize(3)
body.penup()
body.goto(0, 80)
body.pendown()
body.goto(0, 0)

# Dibujo de los brazos
arms = turtle.Turtle()
arms.color("black")
arms.pensize(3)
arms.penup()
arms.goto(0, 50)
arms.pendown()
arms.goto(-40, 20)  # Brazo izquierdo
arms.penup()
arms.goto(0, 50)
arms.pendown()
arms.goto(40, 20)  # Brazo derecho

# Dibujo de la ropa (círculos)
shirt = turtle.Turtle()
shirt.shape("circle")
shirt.color("blue")
shirt.shapesize(2, 1.5)  # Tamaño de la camisa
shirt.penup()
shirt.goto(0, 20)

# Dibujo de las piernas
legs = turtle.Turtle()
legs.color("black")
legs.pensize(3)
legs.penup()
legs.goto(0, 0)
legs.pendown()
legs.goto(-20, -50)  # Pierna izquierda
legs.penup()
legs.goto(0, 0)
legs.pendown()
legs.goto(20, -50)  # Pierna derecha

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()

