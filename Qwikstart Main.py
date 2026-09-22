from tkinter import ttk as tk
from tkinter import *
from os import times
from os import system
from os import path
from datetime import datetime
import json
from pathlib import Path


checkInTime = datetime.now()
deadlineHr = 7
deadlineMin = 45
timeTextColor = 'black'
timeText = ''
bestTime1Mile = "0:00:00"
bestTime2Mile = "0:00:00"
bestTime3Mile = "0:00:00"

if checkInTime.hour > deadlineHr or (checkInTime.hour == deadlineHr and checkInTime.minute > deadlineMin):
    timeTextColor = 'red'
    timeText = 'You are late!'
else:
    timeTextColor = 'green'
    timeText = 'You did it!'

root = Tk()
frm = tk.Frame(root, padding = 10)
frm.grid()
#above code initializes the GUI Window

#Start of content in the GUI Window
root.title("Qwikstart")
tk.Label(frm, text="GOOD MORNING").grid(column=0, row=0)
tk.Label(frm, text = 'Time: ' + checkInTime.strftime("%I:%M:%S"), foreground=timeTextColor).grid(column=0, row=1), 
tk.Label(frm, text = timeText, foreground=timeTextColor).grid(column=1, row=1)
#^^ Block of code responsible for doing time check. 

tk.Label(frm, text = 'Your daily run').grid(column=0, row=3)
tk.Label(frm, text = 'miles ran: ').grid(column=0, row=4)
runDistance = tk.Entry(frm).grid(column=1, row=4)
tk.Label(frm, text = 'your time: ').grid(column=0, row=5)
runTime = tk.Entry(frm).grid(column=1, row=5)

tk.Label(frm, text = 'Best Time for 1 Mile: ').grid(column=0, row=6)




root.mainloop()
