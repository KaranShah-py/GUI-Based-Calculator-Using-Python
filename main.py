from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from PIL import ImageTk, Image
import math
from collections import deque

# Basic window 
root = Tk()
root.title('Calculator')
root.iconbitmap('Images/calculator.ico')
root.config(bg='#3f5258')
root.geometry('460x683')
root.maxsize(width=460, height=683)
root.minsize(width=460, height=683)

global history_list
history_list = deque(maxlen=14)

# functions 
def insert_in_box(number):
    entry_field.insert(END, number)

def backspace():
    number = str(entry_field.get())
    entry_field.delete(len(number)-1, END)

def addition():
    global first_number
    first_number = entry_field.get()
    global f_num
    f_num = float(first_number)
    entry_field.delete(0,END)
    global sign
    sign = "+"

def subtraction():
    global first_number
    first_number = entry_field.get()
    global f_num
    f_num = float(first_number)
    entry_field.delete(0,END)
    global sign
    sign = "-"

def multiplication():
    global first_number
    first_number = entry_field.get()
    global f_num
    f_num = float(first_number)
    entry_field.delete(0,END)
    global sign
    sign = "x"

def division():
    global first_number
    first_number = entry_field.get()
    global f_num
    f_num = float(first_number)
    entry_field.delete(0,END)
    global sign
    sign = "/"

def percentage():
    global first_number
    first_number = entry_field.get()
    global f_num
    f_num = float(first_number)
    entry_field.delete(0,END)
    global sign
    sign = "%"

def change_sign():
    first_number = entry_field.get()
    f_num = float(first_number)
    if f_num > 0:
        f_num = -1 * f_num
    elif f_num == 0:
        f_num = f_num
    else:
        f_num = -1 * f_num
    entry_field2.delete(0,END)
    entry_field.delete(0,END)
    entry_field2.insert(0, str(f'{float(first_number)} ='))
    entry_field.insert(0, f_num)
    history_list.append(f'{entry_field2.get()} {entry_field.get()}')

def square_():
    first_number = entry_field.get()
    f_num = float(first_number)
    squ = math.pow(f_num,float(2))

    entry_field2.delete(0,END)
    entry_field.delete(0,END)
    entry_field2.insert(0, str(f'{f_num}² ='))
    entry_field.insert(0, squ)

    history_list.append(f'{entry_field2.get()} {entry_field.get()}')

def square_root():
    first_number = entry_field.get()
    f_num = float(first_number)
    squ = round(math.sqrt(f_num),4)

    entry_field.delete(0, END)
    entry_field2.delete(0,END)
    entry_field2.insert(0, str(f'√{f_num} ='))
    entry_field.insert(0, squ)

    history_list.append(f'{entry_field2.get()} {entry_field.get()}')


def reciprocal():
    first_number = entry_field.get()
    f_num = float(first_number)
    reci = round(float(1/f_num),4)

    entry_field2.delete(0, END)
    entry_field.delete(0,END)
    entry_field2.insert(0, str(f'1 / {f_num} ='))
    entry_field.insert(0,reci)

    history_list.append(f'{entry_field2.get()} {entry_field.get()}')

def equal():
    second_number = entry_field.get()
    entry_field2.delete(0, END)
    entry_field.delete(0,END)
    if sign == "+":
        entry_field2.insert(0, str(f'{f_num} {sign} {float(second_number)} ='))
        entry_field.insert(0,round(f_num + float(second_number),4))
    elif sign == "-":
        entry_field2.insert(0, str(f'{f_num} {sign} {float(second_number)} ='))
        entry_field.insert(0,round(f_num - float(second_number),4))
    elif sign == "x":
        entry_field2.insert(0, str(f'{f_num} {sign} {float(second_number)} ='))
        entry_field.insert(0,round(f_num * float(second_number),4))
    elif sign == '/':
        entry_field2.insert(0, str(f'{f_num} {sign} {float(second_number)} ='))
        entry_field.insert(0,round(float(f_num / float(second_number)),4))
    elif sign == '%':
        entry_field2.insert(0, str(f'{f_num} {sign} {float(second_number)} ='))
        entry_field.insert(0,round(float(f_num/float(second_number)*100),1))
    else:
        entry_field2.insert(0, str(f'{f_num} {sign} {float(second_number)} ='))
        entry_field.insert(0, float((f_num / float(second_number))*100))
    history_list.append(f'{entry_field2.get()} {entry_field.get()}')

    
def clear():
    entry_field.delete(0, END)
    entry_field2.delete(0,END)

def clear_only():
    entry_field.delete(0, END)

def history_():
    # Basic window for records
    history_window = Toplevel()
    history_window.title('Previous History')
    history_window.config(bg='#3f5258')
    history_window.geometry('460x685')
    history_window.minsize(width=460, height=685)
    history_window.maxsize(width=460, height=685)

    # functions
    def inserting_in_the_entry_boxes():
        for i in range(0, len(history_list)):
            if i == 0:
                entry_fieldH14.insert(0, history_list[0])
            elif i == 1:
                entry_fieldH13.insert(0, history_list[1])
            elif i == 2:
                entry_fieldH12.insert(0, history_list[2])
            elif i == 3:
                entry_fieldH11.insert(0, history_list[3])
            elif i == 4:
                entry_fieldH10.insert(0, history_list[4])
            elif i == 5:
                entry_fieldH09.insert(0, history_list[5])
            elif i == 6:
                entry_fieldH08.insert(0, history_list[6])
            elif i == 7:
                entry_fieldH07.insert(0, history_list[7])
            elif i == 8:
                entry_fieldH06.insert(0, history_list[8])
            elif i == 9:
                entry_fieldH05.insert(0, history_list[9])
            elif i == 10:
                entry_fieldH04.insert(0, history_list[10])
            elif i == 11:
                entry_fieldH03.insert(0, history_list[11])
            elif i == 12:
                entry_fieldH02.insert(0, history_list[12])
            elif i == 13:
                entry_fieldH01.insert(0, history_list[13])
    
    # Defining buttons, frames, images, and other widgets 
    entry_fieldH01 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH02 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH03 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH04 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH05 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH06 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH07 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH08 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH09 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH10 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH11 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH12 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH13 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))
    entry_fieldH14 = Entry(history_window, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=LEFT, width=42, font=('Helvetica',20))

    exit_button = Button(history_window,text='Exit', padx=20, pady=10, bg='#27393f', foreground='white', activebackground='White', activeforeground='black', borderwidth=0, relief=GROOVE, command=history_window.destroy)

    # Putting the buttons and other widgets on the screen
    entry_fieldH01.grid(row=0,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH02.grid(row=1,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH03.grid(row=2,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH04.grid(row=3,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH05.grid(row=4,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH06.grid(row=5,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH07.grid(row=6,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH08.grid(row=7,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH09.grid(row=8,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH10.grid(row=9,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH11.grid(row=10,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH12.grid(row=11,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH13.grid(row=12,column=0,columnspan=4, padx=1, pady=5)
    entry_fieldH14.grid(row=13,column=0,columnspan=4, padx=1, pady=5)
    
    exit_button.grid(row=14, column=0, sticky=W, padx=2, pady=2)
    # calling the function 
    inserting_in_the_entry_boxes()
    
# Defining Buttons, labels and frames
top_frame = Frame(root, bg='#3f5258', borderwidth=0, relief=GROOVE, width=20, height=15)
options = Button(top_frame,text='☰', bg='#3f5258', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, font=('Helvetica', 20, BOLD), relief=GROOVE, padx=15, pady=10)
Top_label = Label(top_frame, text='STANDARD', bg='#3f5258', foreground='White',borderwidth=0 , font=('Helvetica', 20, BOLD), relief=GROOVE, padx=15, pady=10,)
blank = Button(top_frame,text='  ', bg='#3f5258', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, font=('Helvetica', 20, BOLD), relief=GROOVE, padx=37, pady=10, state= DISABLED)
history = Button(top_frame,text='H', bg='#3f5258', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, font=('Helvetica', 20, BOLD), relief=GROOVE, padx=15, pady=10, command=history_)


entry_field2 = Entry(root, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='White', justify=RIGHT, font=('Helvetica',15))
entry_field2.grid(row=1,column=0,columnspan=4,sticky=W+E, pady=10)

entry_field = Entry(root, borderwidth=1, bg='#3f5258', relief=FLAT, foreground='white', justify=RIGHT, font=('Helvetica',30))
entry_field.grid(row=2,column=0,columnspan=4,sticky=W+E, pady=10)


button1 = Button(root,text='1', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(1))
button2 = Button(root,text='2', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(2))
button3 = Button(root,text='3', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(3))
button4 = Button(root,text='4', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(4))
button5 = Button(root,text='5', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(5))
button6 = Button(root,text='6', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(6))
button7 = Button(root,text='7', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(7))
button8 = Button(root,text='8', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(8))
button9 = Button(root,text='9', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(9))
button0 = Button(root,text='0', padx=50, pady=30, bg='#101c25', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box(0))

buttonsq = Button(root,text='x²', padx=48, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=square_)
buttonre = Button(root,text='1/x', padx=44.5, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=reciprocal)
buttonro = Button(root,text='√x', padx=46, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=square_root)
buttoneq = Button(root,text='=', padx=50, pady=30, bg='#189ad3', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=equal)

buttonpl = Button(root,text='+', padx=49, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=addition)
buttonmi = Button(root,text='-', padx=50, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=subtraction)
buttonmu = Button(root,text='x', padx=50, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=multiplication)
buttondi = Button(root,text='/', padx=50, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=division)
buttonmp = Button(root,text='+/-', padx=44.5, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=change_sign)
buttondo = Button(root,text='. ', padx=50, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=lambda: insert_in_box('.'))
buttoncl = Button(root,text='C', padx=48, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=clear)
buttonce = Button(root,text='CE', padx=47, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=clear_only)
buttonbs = Button(root,text='<-', padx=46, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=backspace)
buttonpe = Button(root,text='%', padx=48, pady=30, bg='#27393f', foreground='white', activebackground='white', activeforeground='black', borderwidth=0, relief=GROOVE, command=percentage)


# Putting buttons labels and frames in the GUI.
top_frame.grid(row=0, column=0, columnspan=4, sticky=W+E)
options.grid(row=0, column=0, padx=2, pady=1, sticky=W)
Top_label.grid(row=0, column=1, padx=2, pady=1, sticky=W)
blank.grid(row=0, column=2, padx=1, pady=1, sticky=N)
history.grid(row=0, column=3, padx=1, pady=1, sticky=N)


buttonpe.grid(row=3, column=0, padx=1, pady=1)
buttonce.grid(row=3, column=1, padx=1, pady=1)
buttoncl.grid(row=3, column=2, padx=1, pady=1)
buttonbs.grid(row=3, column=3, padx=1, pady=1)

buttonsq.grid(row=4, column=0, padx=1, pady=1)
buttonre.grid(row=4, column=1, padx=1, pady=1)
buttonro.grid(row=4, column=2, padx=1, pady=1)
buttondi.grid(row=4, column=3, padx=1, pady=1)

button7.grid(row=5, column=0, padx=1, pady=1)
button8.grid(row=5, column=1, padx=1, pady=1)
button9.grid(row=5, column=2, padx=1, pady=1)
button4.grid(row=6, column=0, padx=1, pady=1)
button5.grid(row=6, column=1, padx=1, pady=1)
button6.grid(row=6, column=2, padx=1, pady=1)
button1.grid(row=7, column=0, padx=1, pady=1)
button2.grid(row=7, column=1, padx=1, pady=1)
button3.grid(row=7, column=2, padx=1, pady=1)
button0.grid(row=8, column=1, padx=1, pady=1)

buttonpl.grid(row=5, column=3, padx=0, pady=1)
buttonmi.grid(row=6, column=3, padx=0, pady=1)
buttonmu.grid(row=7, column=3, padx=0, pady=1)
buttondo.grid(row=8, column=2, padx=0, pady=1)
buttoneq.grid(row=8, column=3, padx=2, pady=1)
buttonmp.grid(row=8, column=0, padx=1, pady=1)


# Mainloop
root.mainloop()

# This code is contributed by Karan Shah.