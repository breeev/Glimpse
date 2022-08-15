# move at four edges of screen before going back to center
# undetailed countdown
from random import randint
from sys import platform
from sys import exit
from tkinter import Canvas, Text, Toplevel
if platform!='win32':exit()
from getuser import lookup_username
# print(getuser.lookup_username())
try:from tkinter import Label,Tk
except ModuleNotFoundError:from Tkinter import Label,Tk
from PIL import Image,ImageTk
from subprocess import getoutput
try:exec('dic={'+getoutput('curl ipinfo.io').split('{')[1])
except:dic={i:None for i in 'ip,hostname,city,region,country,loc,org,postal,timezone,readme'.split(',')}
print(dic)
class Eyes:
   def __init__(s,master:Tk,size:tuple,marge:int=0,pos:tuple=(-2,-2),img=None,**kargs):
      s.x,s.y=size[0],size[1]
      s.c=Canvas(master,width=s.x+2,height=s.y+2,**kargs)
      s.c.place(x=pos[0],y=pos[1])
      s.size=size
      if img:s.c.create_image(0,0,image=img)
      s.left_sclera=s.c.create_oval(0+marge,0+marge,s.x/2-marge,s.y-marge,outline='black',fill='white',width=2)
      s.right_sclera=s.c.create_oval(s.x/2+marge,0+marge,s.x-marge,s.y-marge,outline='black',fill='white',width=2)

      pupils=10
      s.left_pupil=s.c.create_oval(s.x/4-pupils,s.y/2-pupils,s.x/4+pupils,s.y/2+pupils,outline='black',fill='black')
      s.right_pupil=s.c.create_oval(3*s.x/4-pupils,s.y/2-pupils,3*s.x/4+pupils,s.y/2+pupils,outline='black',fill='black')

      s.left_superior_eyelid=s.c.create_arc(0+marge,0+marge,s.x/2-marge,s.y-marge,outline='black',fill='grey',width=4,start=0,extent=180)
      s.right_superior_eyelid=s.c.create_arc(s.x/2+marge,0+marge,s.x-marge,s.y-marge,outline='black',fill='grey',width=4,start=0,extent=180)

      s.left_inferior_eyelid=s.c.create_arc(0+marge,0+marge,s.x/2-marge,s.y-marge,outline='black',fill='grey',width=4,start=0,extent=-180)
      s.right_inferior_eyelid=s.c.create_arc(s.x/2+marge,0+marge,s.x-marge,s.y-marge,outline='black',fill='grey',width=4,start=0,extent=-180)

      s.c.after(2000,lambda e=None:s.c.coords(s.left_superior_eyelid,[0+marge,0+marge,s.x/2-marge,s.y-marge-30]))
class Glimpse:
   def __init__(s,geometry:str,own:bool=False):
      s.talkingspeed=(10,300)
      s.tk=Tk()
      s.tk.title('Glimpse')
      s.tk.geometry(geometry)
      s.geom=geometry.split('x')
      s.geom+=s.geom.pop(-1).split('+')
      s.geom=[int(i) for i in s.geom]
      s.tk.config(background='black')
      if own:s.tk.overrideredirect(True)
      s.tk.wm_attributes('-topmost','true')
      s.tk.focus_force()
      s.bgi=Image.open('pixels.png').resize((1900,1900),resample=Image.Resampling.BOX)
      s.bg=Label(s.tk)
      s.SetBG()
      s.bg.place(x=-5,y=-5)
      s.tk.bind('<Control-q>',lambda x=None:s.tk.destroy())
   def SetBG(s):
      s.tkbgi=ImageTk.PhotoImage(s.bgi)
      s.bg.config(i=s.tkbgi)
   def move(s,dx,dy,speed,x:int=0,y:int=0):
      s.tk.geometry(f'+{x}+{y}')
      s.tk.after(speed,lambda:s.move(dx,dy,speed,x+dx,y+dy))
   def notepad(s):
      s.np=Toplevel(s.tk)
      s.np.title('notepad.exe - Untitled')
      s.np.geometry(f'500x500+{s.geom[0]+2*s.geom[2]}+{s.geom[3]}')
      s.npT=Text(s.np)
      s.npT.pack(fill='both',expand=1)
      s.tk.after(1,s.tk.focus_force)
   def wakeup(s):
      s.eyes=Eyes(s.tk,s.geom[:2],10,img=s.tkbgi)
      s.tk.after(2000,s.notepad)
   def sayloop(s,string:str):
      s.npT.insert('end-1c',string[0])
      if len(string)!=1:s.npT.after(randint(*s.talkingspeed),lambda e=None:s.sayloop(string[1:]))
   def say(s,string:str,speedrange:tuple=None):
      s.npT.delete('1.0','end-1c')
      if speedrange:s.talkingspeed=speedrange
      s.sayloop(string)
   def loop(s):s.tk.mainloop()
d=Glimpse('150x100+50+50')
d.wakeup()
# d.bind('<Button-1>',lambda x:d.geometry(f'+{x.x*10}+{x.y*10}'))
# move(d,1,3,1)
d.tk.after(3000,lambda e=None:d.say('BORING!!!'))
d.loop()