#Para crear la interfaz
from tkinter import *
import time
import random

#Constantes
GAME_WIDTH = 650;
GAME_HEIGHT = 650;
SPEED = 150;
SPACE_SIZE = 50;
BODY_PARTS = 3
SNAKE_COLOR = "#B5B2B2"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
cont = 0
PASOS = random.randint(1, 10)
#Objetos
class Snake:
	def __init__(self):
		self.body_size = BODY_PARTS
		self.coordinates = []
		self.squares = []

		for i in range(0, BODY_PARTS):
			self.coordinates.append([6*SPACE_SIZE,6*SPACE_SIZE])
		
		for x, y in self.coordinates:
			square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill= SNAKE_COLOR, tag = "snake");
			self.squares.append(square)
		canvas.itemconfig(self.squares[0], fill = "#4B4B4B")

class Food:
	def __init__(self):
		x = random.randint(0, ((GAME_WIDTH / SPACE_SIZE)-1)) * SPACE_SIZE;
		y = random.randint(0, ((GAME_HEIGHT / SPACE_SIZE)-1)) * SPACE_SIZE;
		self.coordinates = [x,y]
		canvas.create_oval(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill = FOOD_COLOR, tag = "food");

#Funciones
def next_turn(snake, food):
	if cont == PASOS:
		pass

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

		label.config(text = f"Score: {score}")

		canvas.delete("food")

		food = Food() 
	else:
		del snake.coordinates[-1]

		canvas.delete(snake.squares[-1])

		del snake.squares[-1]
	for i in range(len(snake.squares)):
		if i == 0: 
			canvas.itemconfig(snake.squares[0], fill = "#4B4B4B")
		else:
			canvas.itemconfig(snake.squares[i], fill = SNAKE_COLOR)
	window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
	global direction
	if new_direction == 'left':
		if direction != 'right':
			time.sleep(150/1000)
			direction = new_direction;
	elif new_direction == 'right':
		if direction != 'left':
			time.sleep(150/1000)
			direction = new_direction
	elif new_direction == 'up':
		if direction != 'down':
			time.sleep(150/1000)
			direction = new_direction
	else:
		if direction != 'up':
			time.sleep(150/1000)
			direction = new_direction

def check_collisions():
	pass

def game_over():
	pass


#Crear ventana
window = Tk();
#Titulo del juego
window.title("Snake game demo");
#No permitimos que se pueda ampliar la ventana
window.resizable(False,False);

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