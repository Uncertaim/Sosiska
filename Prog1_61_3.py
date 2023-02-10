
############################################################################# знакомство с tkinter

#from tkinter import *
#root = Tk()
#root.title('window')
#root.geometry('500x300')
#def function1():
#    w1.config(text=int(w2.get())*2)
#w2=Entry(root, bg = 'green', fg = 'white')
#w3=Button(root, text='кнопка', width = 30, height = 20, command=function1, activebackground = 'yellow', bg = 'purple', fg = 'cyan')
#w1=Label(root, text='Это подпись', width=15, bg = 'cyan', font = 'consolas')
#w1.pack()
#w2.pack()
#w3.pack()
#root.mainloop()

############################################################################# фигуры

#from tkinter import *
#root = Tk()
#root.title('window')
#root.geometry('1000x1300')
#def function1():
#    canvas.itemconfig(b, fill = 'purple')
#def function2():
#    canvas.itemconfig(b, fill = 'red')
#canvas = Canvas(root, width=800,height=800, bg = 'green')
#canvas.pack()
#canvas.create_line(15,15,150,150, width = 5)
#canvas.create_rectangle(110,130,180,180, width = 5, fill = 'yellow')
#b = canvas.create_oval(280,230,720,780, fill = 'red', outline = 'white', width = 8, activefill = 'white', activeoutline = 'pink')
#a = canvas.create_polygon(450,280,310,480,240,290,335,340, width = 5, fill = 'brown', outline = 'cyan', dash=10)
#Button(root, text='кнопка1', width = 30, height = 5, command=function1, activebackground = 'yellow', bg = 'purple', fg = 'cyan').pack()
#Button(root, text='кнопка2', width = 30, height = 5, command=function2, activebackground = 'yellow', bg = 'purple', fg = 'cyan').pack()
#root.mainloop()

############################################################################# messagebox

#from tkinter import *
#from tkinter import messagebox
#root = Tk()
#root.title('window')#подпись окна
#root.geometry('300x300')#геометрия
#def function1():
#    messagebox.showinfo('Вы получили', int(a.get())*15)
#a = Entry(root, width = 10, bg = 'gray', fg = 'white')
#a.pack()
#Button(root, text='умножить на 15', width = 30, height = 5, command=function1, bg = 'cyan', fg = 'black').pack()
#root.mainloop()

#############################################################################
'''from tkinter import*
import random
score, max_score = 0, 20
size_x, size_y = 1280, 720
def put():
    global button
    button = Button(root, text='hfdsjh', bg='gray', activebackground='pink', command = click )
    button.place(x=random.randint(20,size_x-20),y=random.randint(10,size_y-10))
def click():
     global score
     button.destroy()
     score+=1
     if score < 5:
         put()
     else:
         Label(root, text='You win, \n fewkf',).place(relx=0.5, rely=0.5)
root = Tk()
root.title('gfgs')
root.geometry(f'{size_x}x{size_y}')
root.resizable(False,False)
put()
root.mainloop()
'''
##########################################################################################Сложный калькулятор
from tkinter import *
def set_value(formula):
    if formula == '':
        label['text'] = '0'
    else:
        label['text'] = str(eval(formula))
def logic(operator):
    if operator =='C':
        set_value('')
    elif operator =='Del':
        label['text']=label['text'][0:-1]
        if label['text'] == '':
            label['text']='0'
    elif operator =='x^2':
        set_value(str((eval(label['text']))**2))
    elif operator =='=':
        set_value(label['text'])
    else:
        if label['text'] =='0':
            label['text'] =''
        label['text'] = label['text']+operator



list = ['C','Del','*','=','1','2','3','/','4','5','6','+','7','8','9','-','(','0',')','x^2']
root = Tk()
root['bg'] = 'black'
root.title('Сложный калькулятор')
root.geometry('485x550')
root.resizable(False,False)
label = Label(text='0', font=('Consolas',21,'bold'), bg='black', foreground = 'white')
x=10
y=140
for lis in list:
    com = lambda x=lis: logic(x)
    Button(text=lis,bg='beige',activebackground='red',activeforeground='blue',font=('consolas',15),command=com).place(x=x,y=y,width=115,height=80)
    x+=115
    if x>400:
        x=10
        y+=80
label.place(x=10,y=50)
root.mainloop()