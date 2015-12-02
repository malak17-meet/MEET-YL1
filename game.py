from meet import *
ball1={"radius":30,"x":7,"y":5,"dy":1,"dx":1}
ball2={"radius":50,"x":20,"y":8,"dy":1,"dx":1}
ball3={"radius":30,"x":10,"y":7,"dy":1,"dx":1}
cells=[]
circle1 = create_cell(ball1)
cells.append(circle1)
circle2 = create_cell(ball2)
cells.append(circle2)
circle3 = create_cell(ball3)
cells.append(circle3 )
get_screen_width



def boarders(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		
		if (cell.xcor() > width):
			cell.set_dx(-cell.get_dx()) 
		if (cell.ycor() > height):
			cell.set_dy(-cell.get_dy())




while (True):
	move_cells(cells)
	boarders(cells)

