from tkinter import Button,Label,PhotoImage,Tk
from PIL import Image,ImageTk
def Glimpse(geometry:str,own:bool=False):
   global bg
   tk=Tk()
   tk.title('Glimpse')
   tk.geometry(geometry)
   tk.config(background='black')
   if own:
      tk.overrideredirect(True)
      tk.wm_attributes('-topmost','true')
   tk.focus_force()
   return tk
def SetBG(s,img:Image):
   bgi=img
   g=ImageTk.PhotoImage(bgi)
   bg.config(i=g)
d=Glimpse('10x10+500+500',True)
bgi=Image.open('pixels.png').resize((1900,1900),resample=Image.Resampling.BOX)
g=ImageTk.PhotoImage(bgi)
bg=Label(d,i=g)
bg.place(x=-5,y=-5)
d.bind('<Button-1>',lambda x:print('ok'))#Glimpse.tk.destroy();)
d.mainloop()