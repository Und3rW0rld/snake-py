#Para crear la interfaz
from tkinter import *
import time
import random

#Constantes
GAME_WIDTH = 650
GAME_HEIGHT = 650
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#B5B2B2"
FOOD_COLOR = "black"
BACKGROUND_COLOR = "grey"
cont = 0
pasos = random.randint(1, 10)
comida = True
new_direction = ""
#Objetos
class Snake:
	def __init__(self):
		self.body_size = BODY_PARTS
		self.coordinates = []
		self.squares = []

		for i in range(0, BODY_PARTS):
			self.coordinates.append([6*SPACE_SIZE,6*SPACE_SIZE])
		
		for x, y in self.coordinates:
			square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill= SNAKE_COLOR, tag = "snake")
			self.squares.append(square)
		canvas.itemconfig(self.squares[0], fill = "#4B4B4B")

class Food:
	def __init__(self):
		x = random.randint(0, ((GAME_WIDTH / SPACE_SIZE)-1)) * SPACE_SIZE
		y = random.randint(0, ((GAME_HEIGHT / SPACE_SIZE)-1)) * SPACE_SIZE
		self.coordinates = [x,y]
		canvas.create_oval(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill = FOOD_COLOR, tag = "food")

#Funciones
def next_turn(snake, food):
	global cont, pasos, comida, new_direction, direction

	
	if new_direction == 'left':
		if direction != 'right':
			direction = new_direction
	elif new_direction == 'right':
		if direction != 'left':
			direction = new_direction
	elif new_direction == 'up':
		if direction != 'down':
			direction = new_direction
	elif new_direction == 'down':
		if direction != 'up':
			direction = new_direction
		
	if comida == False:
		cont += 1
		if cont == pasos:
			comida = True
			food = Food()
			paso = random.randint(1, 10)
			cont = 0

	x, y = snake.coordinates[0]
	if direction == "up":
		y -= SPACE_SIZE
	elif direction == "down":
		y += SPACE_SIZE
	elif direction == "left":
		x -= SPACE_SIZE

	elif direction == "right":
		x += SPACE_SIZE

	snake.coordinates.insert(0, (x,y))

	square = canvas.create_rectangle(x, y, x +SPACE_SIZE, y+SPACE_SIZE, fill = SNAKE_COLOR)

	snake.squares.insert(0, square)
		#print(f"coordenadas snake {snake.coordinates[0]} coordenadas food {food.coordinates}")
	if x == food.coordinates[0] and y == food.coordinates[1]:
		global score 
		score += 1
		comida = False
		label.config(text = f"Score: {score}")
		canvas.delete("food")

			 
	else:
		del snake.coordinates[-1]

		canvas.delete(snake.squares[-1])

		del snake.squares[-1]
	
	canvas.itemconfig(snake.squares[0], fill="#4B4B4B")
	canvas.itemconfig(snake.squares[1], fill=SNAKE_COLOR)

	if check_collisions(snake):
		game_over()
	else:
		window.after(SPEED, next_turn, snake, food)

def change_direction(nd):
	global new_direction
	new_direction = nd

def check_collisions(snake):
	x,y = snake.coordinates[0]
	if x >= GAME_WIDTH or x < 0:
		return True
	elif y >= GAME_HEIGHT or y < 0:
		return True


	for body_part in snake.coordinates[1:]:
		if x == body_part[0] and y == body_part[1]:
			return True

	return False

def game_over():
	canvas.delete(ALL)
	canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
	restart_button.place(x=canvas.winfo_width()/2 - 60, y=canvas.winfo_height()/2 + 200)

def restart_game():
    global snake, food, score, direction, new_direction

    # Reset game variables to initial values
    new_direction = 'down'
    restart_button.place_forget()
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    comida = True
    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))
    next_turn(snake, food)


#Crear ventana
window = Tk()
#Titulo del juego
window.title("Snake game demo")
#No permitimos que se pueda ampliar la ventana
window.resizable(False,False)

#Inicializamos los puntos
score = 0
#Direccion inicial de la snake
direction = 'down'
#Texto de los puntos en pantalla
label = Label(window, text = f"Score: {score}", font = ('consolas', 20))
label.pack()

#Creamos el 'Tablero' de juego
canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width =GAME_WIDTH)
canvas.pack()

restart_button = Button(window, text="Restart", command=restart_game, font=('consolas', 20))

#Intentamos centrar la ventana
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)- (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y-40}")

window.bind('<Left>', lambda event: change_direction("left"))
window.bind('a', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction("right"))
window.bind('d', lambda event: change_direction("right"))
window.bind('<Up>', lambda event: change_direction("up"))
window.bind('w', lambda event: change_direction("up"))
window.bind('<Down>', lambda event: change_direction("down"))
window.bind('s', lambda event: change_direction("down"))


snake = Snake()
food = Food()

next_turn(snake, food)

#Bucle principal de la aplicación
window.mainloop()