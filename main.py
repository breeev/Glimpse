# move at four edges of screen before going back to center
# undetailed countdown
from random import randint
from sys import platform
from sys import exit
from tkinter import BooleanVar, Canvas, IntVar, Text, Toplevel
from tkinter.font import Font
if platform!='win32':exit()
from getuser import lookup_username
# print(getuser.lookup_username())
try:from tkinter import Label,Tk
except ModuleNotFoundError:from Tkinter import Label,Tk
from PIL import Image,ImageTk
from subprocess import getoutput
try:exec('dic={'+getoutput('curl ipinfo.io').split('{')[1])
except:dic={i:None for i in 'ip,hostname,city,region,country,loc,org,postal,timezone,readme'.split(',')}
# print(dic)
class Eyes:
   def __init__(s,master:Tk,size:tuple,marge:int=0,pos:tuple=(-2,-2),img=None,**kargs):
      s.ready=BooleanVar(master)
      s.ready.set(False)
      s.x,s.y=size[0],size[1]
      s.eyemovradius=20
      s.c=Canvas(master,width=s.x+2,height=s.y+2,**kargs)
      s.c.place(x=pos[0],y=pos[1])
      s.marge=marge
      if img:s.c.create_image(0,0,image=img)
      s.left_sclera=s.c.create_oval(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='white',width=2)
      s.right_sclera=s.c.create_oval(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='white',width=2)

      s.pupils=20
      s.left_pupil=s.c.create_oval(s.x/4-s.pupils,s.y/2-s.pupils,s.x/4+s.pupils,s.y/2+s.pupils,outline='black',fill='black')
      s.right_pupil=s.c.create_oval(3*s.x/4-s.pupils,s.y/2-s.pupils,3*s.x/4+s.pupils,s.y/2+s.pupils,outline='black',fill='black')

      s.left_superior_eyelid=s.c.create_arc(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=180)
      s.right_superior_eyelid=s.c.create_arc(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=180)

      s.left_inferior_eyelid=s.c.create_arc(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=-180)
      s.right_inferior_eyelid=s.c.create_arc(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=-180)

      s.c.after(1000,s.openeyes)

   def openeyes(s,e=None,i=1):
      s.c.coords(s.left_superior_eyelid,[s.marge,s.marge,s.x/2-s.marge,s.y-s.marge-i])
      s.c.coords(s.right_superior_eyelid,[s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge-i])
      s.c.coords(s.left_inferior_eyelid,[s.marge,s.marge+i,s.x/2-s.marge,s.y-s.marge])
      s.c.coords(s.right_inferior_eyelid,[s.x/2+s.marge,s.marge+i,s.x-s.marge,s.y-s.marge])
      if i<50:s.c.after(0+i*2,lambda e=None:s.openeyes(i=i+1))
      else:s.dilate(10,8)

   def deletelids(s):
      for i in (s.left_superior_eyelid,s.right_superior_eyelid,s.left_inferior_eyelid,s.right_inferior_eyelid):s.c.delete(i)
      s.ready.set(True)

   def pupilsize(s,size):
      s.pupils=size
      s.c.delete(s.left_pupil)
      s.c.delete(s.right_pupil)
      s.left_pupil=s.c.create_oval(s.x/4-s.pupils,s.y/2-s.pupils,s.x/4+s.pupils,s.y/2+s.pupils,outline='black',fill='black')
      s.right_pupil=s.c.create_oval(3*s.x/4-s.pupils,s.y/2-s.pupils,3*s.x/4+s.pupils,s.y/2+s.pupils,outline='black',fill='black')

   def dilate(s,delay,size):
      if size!=s.pupils:
         s.pupilsize(s.pupils+(1 if size>s.pupils else -1))
         s.c.after(delay,lambda e=None:s.dilate(delay,size))
      else:s.deletelids()

   def move(s,x,y):
      s.unmove()
      s.c.coords(s.left_pupil,[s.x/4-s.pupils+x*s.eyemovradius,s.y/2-s.pupils+y*s.eyemovradius,s.x/4+s.pupils+x*s.eyemovradius,s.y/2+s.pupils+y*s.eyemovradius])
      s.c.coords(s.right_pupil,[3*s.x/4-s.pupils+x*s.eyemovradius,s.y/2-s.pupils+y*s.eyemovradius,3*s.x/4+s.pupils+x*s.eyemovradius,s.y/2+s.pupils+y*s.eyemovradius])

   def unmove(s):
      s.c.coords(s.left_pupil,[s.x/4-s.pupils,s.y/2-s.pupils,s.x/4+s.pupils,s.y/2+s.pupils])
      s.c.coords(s.right_pupil,[3*s.x/4-s.pupils,s.y/2-s.pupils,3*s.x/4+s.pupils,s.y/2+s.pupils])

class Glimpse:
   def __init__(s,geometry:str,own:bool=False):
      s.talkingspeed=(1,100)
      s.tk=Tk()
      s.scrwidth,s.scrheight=s.tk.winfo_screenwidth(),s.tk.winfo_screenheight()
      s.bang=BooleanVar(value=False)
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
   def BANG(s,e=None):
      print('BANG !')
      s.bang.set(True)
      s.bang.set(False)
   def wait(s,t):
      s.tk.after(t,s.BANG)
      s.tk.wait_variable(s.bang)
   def move(s,dx,dy,speed):
      s.geom=s.geom[:2]+[s.geom[2]+dx,s.geom[3]+dy]
      s.tk.geometry(f'+{s.geom[2]}+{s.geom[3]}')
      if dx and  s.geom[2]<0 or s.geom[2]>s.scrwidth-s.geom[0]-dx:s.BANG()
      elif  s.geom[3]<0 or s.geom[3]>s.scrheight-s.geom[1]-dy*5:s.BANG()
      else:s.tk.after(speed,lambda:s.move(dx,dy,speed))
   def notepad(s):
      s.np=Toplevel(s.tk)
      s.np.wm_attributes('-topmost','true')
      s.np.title('notepad.exe - Untitled')
      s.np.geometry(f'500x200+{s.geom[0]+2*s.geom[2]}+{s.geom[3]}')
      s.npT=Text(s.np,font=Font(s.np,family='Arial',size=30))
      s.npT.pack(fill='both',expand=1)
      s.tk.after(1,s.tk.focus_force)
   def wakeup(s):
      s.eyes=Eyes(s.tk,s.geom[:2],10,img=s.tkbgi)
      s.tk.wait_variable(s.eyes.ready)

      for i in [((1,-1),(4,0)),((1,1),(0,4)),((-1,1),(-4,0)),((-1,-1),(0,-4))]:
         s.wait(700)
         s.eyes.move(*i[0])
         s.move(*i[1],1)
         s.tk.wait_variable(s.bang)

      s.wait(700)
      s.eyes.unmove()

      print('DONNNNNEEEE')
      s.wait(1100)
      s.notepad()
      s.wait(700)
      s.eyes.move(1,0)
      s.wait(800)
      s.eyes.unmove()
      s.say('What is this       \nWhere am I')
   def sayloop(s,string:str):
      s.npT.insert('end-1c',string[0])
      if len(string)!=1:s.npT.after(randint(*s.talkingspeed),lambda e=None:s.sayloop(string[1:]))
   def say(s,string:str,speedrange:tuple=None):
      s.npT.delete('1.0','end-1c')
      if speedrange:s.talkingspeed=speedrange
      s.sayloop(string)
   def loop(s):s.tk.mainloop()
d=Glimpse('150x100+0+0')
d.wakeup()
# d.bind('<Button-1>',lambda x:d.geometry(f'+{x.x*10}+{x.y*10}'))
# move(d,1,3,1)
# d.tk.after(3000,lambda e=None:d.say('BORING!!!'))
d.loop()