# move at four edges of screen before going back to center
from sys import platform
from sys import exit
if platform!='win32':exit()
from os import system
from getuser import lookup_username
# print(getuser.lookup_username())
try:from tkinter import Label,Tk
except ModuleNotFoundError:from Tkinter import Label,Tk
from PIL import Image,ImageTk
from subprocess import getoutput
try:exec('dic={'+getoutput('curl ipinfo.io').split('{')[1])
except:dic={i:None for i in 'ip,hostname,city,region,country,loc,org,postal,timezone,readme'.split(',')}
print(dic)
from pywinauto.application import Application
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
   if own:tk.overrideredirect(True)
   tk.wm_attributes('-topmost','true')
   tk.focus_force()
   bgi=Image.open('pixels.png').resize((1900,1900),resample=Image.Resampling.BOX)
   bg=Label(tk)
   SetBG()
   bg.place(x=-5,y=-5)
   return tk
def move(w:Tk,dx,dy,speed,x:int=0,y:int=0):
   w.geometry(f'+{x}+{y}')
   w.after(speed,lambda:move(w,dx,dy,speed,x+dx,y+dy))
def live():
   app=Application().start("notepad.exe")
   app.UntitledNotepad.Edit.type_keys("pywinauto Works!",with_spaces=True)
d=Glimpse('100x100+50+50')
d.bind('<Control-q>',lambda x:d.destroy())
# d.bind('<Button-1>',lambda x:d.geometry(f'+{x.x*10}+{x.y*10}'))
# move(d,1,3,1)
d.after(3000,live)
d.mainloop()