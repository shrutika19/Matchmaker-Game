import random
import time
import tkinter
from tkinter import Tk, Button, DISABLED
from tkinter import messagebox

timeleft =60

def countdown():
    
    global timeleft 

    if timeleft > 0: 
   
        timeleft -= 1
 
        timeLabel.config(text = "Time Left: "
                               + str(timeleft)) 
                                 
        timeLabel.after(1000, countdown)
        timeLabel.grid(row=0,column=20)

    if timeleft == 0:
        root.destroy()
        messagebox.showinfo("Title","Game finished")
    

    

def show_symbol(x,y):
    global first
    global previousX,previousY
    buttons[x,y]['text']=button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
        first =True




root = Tk()
root.geometry("750x600")
root.title('Matchmaker')
root.resizable(width=False, height=False)
buttons = {}
first = True
previousX = 0
previousY = 0
button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']
random.shuffle(symbols)
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12)) 
timeLabel.grid()


for x in range(6):
    for y in range(4):
         button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=7, height=7)
         button.grid(column=x, row=y)
         buttons[x, y] = button
         button_symbols[x, y] = symbols.pop()

       
if timeleft == 60:
    countdown()
        
root.mainloop()
   
    
    
