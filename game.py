import meet
import random
user_cell_dictionary={"radius":30,"x":6,"y":6,"dy":1,"dx":1,"color":"yellow"}

cells=[]


x=0
while x<24:
	x+=1
	ball3={"radius":random.randint(3,10),"x":meet.get_random_x(),"y":meet.get_random_y(),"dy":1,"dx":1}

	circle3 = meet.create_cell(ball3)
	cells.append(circle3)
	


user_cell=meet.create_cell(user_cell_dictionary)
cells.append(user_cell)





def Edge(cells):
	h=meet.get_screen_width() 
	w=meet.get_screen_height() 
	for cell in cells:
		if cell.xcor() + cell.get_radius() >= h:
			x=cell.get_dx()
			cell.set_dx(-x)
		elif cell.xcor() - cell.get_radius()<= -h:
			x=cell.get_dx()
			cell.set_dx(-x)
		if cell.ycor() + cell.get_radius() >= w:
			y=cell.get_dy()
			cell.set_dy(-y)
		elif cell.ycor() - cell.get_radius() <= -w:
			y=cell.get_dy()
			cell.set_dy(-y)

def collison():
	for cell in cells:
		for cell2 in cells:
			if(((cell.xcor()-cell2.xcor())**2+(cell.ycor()-cell2.ycor())**2)**0.5 ) < cell.get_radius() + cell2.get_radius():
				if (cell.get_radius() < cell2.get_radius()):
					cell.goto(meet.get_random_x(),meet.get_random_y())
					cell2.set_radius(cell2.get_radius()+1)
					if cell==user_cell:
						exit()
				if (cell.get_radius() > cell2.get_radius()):
					cell2.goto(meet.get_random_x(),meet.get_random_y())
					cell.set_radius(cell.get_radius()+1)
					if cell2==user_cell:
						exit()


			





while (True):
	direction = meet.get_user_direction(user_cell)
	user_cell.set_dx(direction[0])
	user_cell.set_dy(direction[1])
	meet.move_cells(cells)
	Edge(cells)
	collison()	

