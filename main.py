from tkinter import *


import calendar


def showCal() :


	new_gui = Tk()
	

	new_gui.config(background = "white")


	new_gui.title("KRISHNA_DUA")


	new_gui.geometry("550x600")


	fetch_year = int(year_field.get())


	cal_content = calendar.calendar(fetch_year)

	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")


	cal_year.pack()
	
	new_gui.mainloop()

	

if __name__ == "__main__" :


	gui = Tk()
	gui.minsize(390,844)
	

	gui.config(background = "white")


	gui.title("KRISHNA_DUA")

	
	gui.geometry("250x140")

	
	cal = Label(gui, text = "\n\nCALENDAR\n", bg = "lightblue",
							font = ("times", 28, 'bold') , width=390)

	
	year = Label(gui, text = "\n\nEnter Year\n\n", bg = "light green" , width=390)
	
	year_field = Entry(gui ,width=390)

	
	Show = Button(gui, text = "\nShow Calendar\n", fg = "Black",
							bg = "Red", command = showCal , width=390)


	Exit = Button(gui, text = "\nExit\n", fg = "Black", bg = "Red", command = exit , width=390)
	

	cal.pack(pady=1)

	year.pack(pady=1)

	year_field.pack(pady=1)

	Show.pack(pady=1)

	Exit.pack(pady=1)
	
	# start the GUI
	gui.mainloop()
