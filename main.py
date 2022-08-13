from time import sleep
from tkinter import Button,Label,PhotoImage,Tk
from PIL import Image,ImageTk
def SetBG():
   global g
   g=ImageTk.PhotoImage(bgi)
   bg.config(i=g)
def Glimpse(geometry:str,own:bool=False):
   global bg,bgi
   tk=Tk()
   tk.title('Glimpse')
   tk.geometry(geometry)
   tk.config(background='black')
   if own:
      tk.overrideredirect(True)
      tk.wm_attributes('-topmost','true')
   tk.focus_force()
   bgi=Image.open('pixels.png').resize((1900,1900),resample=Image.Resampling.BOX)
   bg=Label(tk)
   SetBG()
   bg.place(x=-5,y=-5)
   return tk
def move(w:Tk,x:int=0,y:int=0):
   w.geometry(f'+{x}+{y}')
   w.after(1,lambda:move(w,x+1,y))
d=Glimpse('100x100+50+50',True)
d.bind('<Control-q>',lambda x:d.destroy())
# d.bind('<Button-1>',lambda x:d.geometry(f'+{x.x*10}+{x.y*10}'))
move(d)
d.mainloop()