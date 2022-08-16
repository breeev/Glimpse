# undetailed countdown
from random import randint
from sys import platform
from sys import exit
from time import sleep
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
      s.canblink=True
      s.x,s.y=size[0],size[1]
      s.eyemovradius=17
      s.blinkrate=(2000,5000)
      s.c=Canvas(master,width=s.x+2,height=s.y+2,**kargs)
      s.c.place(x=pos[0],y=pos[1])
      s.marge=marge
      if img:s.c.create_image(0,0,image=img)
      s.left_sclera=s.c.create_oval(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='white',width=2)
      s.right_sclera=s.c.create_oval(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='white',width=2)

      s.pupils=20
      s.left_pupil=s.c.create_oval(s.x/4-s.pupils,s.y/2-s.pupils,s.x/4+s.pupils,s.y/2+s.pupils,outline='black',fill='black')
      s.right_pupil=s.c.create_oval(3*s.x/4-s.pupils,s.y/2-s.pupils,3*s.x/4+s.pupils,s.y/2+s.pupils,outline='black',fill='black')

      # s.left_superior_eyelid=s.c.create_arc(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=180)
      # s.right_superior_eyelid=s.c.create_arc(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=180)
      # s.left_inferior_eyelid=s.c.create_arc(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=-180)
      # s.right_inferior_eyelid=s.c.create_arc(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='grey',width=4,start=0,extent=-180)
      s.createlids()

      s.c.after(1000,s.openeyes)

   def openeyes(s,e=None,i=1):
      s.c.coords(s.left_superior_eyelid,[s.marge,s.marge,s.x/2-s.marge,s.y-s.marge-i])
      s.c.coords(s.right_superior_eyelid,[s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge-i])
      s.c.coords(s.left_inferior_eyelid,[s.marge,s.marge+i,s.x/2-s.marge,s.y-s.marge])
      s.c.coords(s.right_inferior_eyelid,[s.x/2+s.marge,s.marge+i,s.x-s.marge,s.y-s.marge])
      if i<50:s.c.after(0+i*2,lambda e=None:s.openeyes(i=i+1))
      else:s.dilate(10,8)

   def deletelids(s,e=None):
      for i in (s.left_superior_eyelid,s.right_superior_eyelid,s.left_inferior_eyelid,s.right_inferior_eyelid):s.c.delete(i)
      s.ready.set(True)

   def createlids(s):
      s.left_superior_eyelid=s.c.create_arc(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='grey',width=2,start=0,extent=180)
      s.right_superior_eyelid=s.c.create_arc(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='grey',width=2,start=0,extent=180)
      s.left_inferior_eyelid=s.c.create_arc(s.marge,s.marge,s.x/2-s.marge,s.y-s.marge,outline='black',fill='grey',width=2,start=0,extent=-180)
      s.right_inferior_eyelid=s.c.create_arc(s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge,outline='black',fill='grey',width=2,start=0,extent=-180)

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

   def blinkcycle(s,li):
      i=li.pop(0)
      s.c.coords(s.left_superior_eyelid,[s.marge,s.marge,s.x/2-s.marge,s.y-s.marge-i])
      s.c.coords(s.right_superior_eyelid,[s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge-i])
      s.c.coords(s.left_inferior_eyelid,[s.marge,s.marge+i,s.x/2-s.marge,s.y-s.marge])
      s.c.coords(s.right_inferior_eyelid,[s.x/2+s.marge,s.marge+i,s.x-s.marge,s.y-s.marge])
      if s.canblink:
         if li:s.c.after(50,lambda e=None:s.blinkcycle(li))
         else:s.c.after(50,s.deletelids)
      else:s.deletelids()

   def blink(s,e=None):
      if s.canblink:
         print('*blink*')
         s.createlids()
         s.blinkcycle([30,0,30])
      s.c.after(randint(*s.blinkrate),s.blink)

   def movelids(s,i):
      s.createlids()
      s.c.coords(s.left_superior_eyelid,[s.marge,s.marge,s.x/2-s.marge,s.y-s.marge-i])
      s.c.coords(s.right_superior_eyelid,[s.x/2+s.marge,s.marge,s.x-s.marge,s.y-s.marge-i])
      s.c.coords(s.left_inferior_eyelid,[s.marge,s.marge+i,s.x/2-s.marge,s.y-s.marge])
      s.c.coords(s.right_inferior_eyelid,[s.x/2+s.marge,s.marge+i,s.x-s.marge,s.y-s.marge])

class Glimpse:
   def __init__(s,geometry:str,own:bool=False):
      s.talkingspeed=(1,100)
      s.saying=''
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
   def closeHandle(s,e=None):
      s.eyes.canblink=False
      s.eyes.movelids(30)
      s.say("I'm not done yet !",(10,80),True)
      sleep(3)
      s.eyes.deletelids()
      s.eyes.canblink=True
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
      if dx and  s.geom[2]<5 or s.geom[2]>s.scrwidth-s.geom[0]-dx*5:s.BANG()
      elif  s.geom[3]<5 or s.geom[3]>s.scrheight-s.geom[1]-dy*3:s.BANG()
      else:s.tk.after(speed,lambda:s.move(dx,dy,speed))
   def notepad(s):
      s.np=Toplevel(s.tk)
      s.np.wm_attributes('-topmost','true')
      s.np.title('notepad.exe - Untitled')
      s.np.geometry(f'500x200+{s.geom[0]+2*s.geom[2]+10}+{s.geom[3]}')
      s.npT=Text(s.np,font=Font(s.np,family='Arial',size=15))
      s.npT.pack(fill='both',expand=1)
      s.tk.after(1,s.tk.focus_force)
   def wakeup(s):
      s.eyes=Eyes(s.tk,s.geom[:2],10,img=s.tkbgi)
      s.tk.wait_variable(s.eyes.ready)

      for i in [((1,-1),(7,0)),((1,1),(0,10)),((-1,1),(-11,0)),((-1,-1),(0,-5))]:
         s.wait(700)
         s.eyes.move(*i[0])
         s.move(*i[1],1)
         s.tk.wait_variable(s.bang)

      s.wait(700)
      s.eyes.unmove()

      print('DONNNNNEEEE')
      s.wait(1100)
      s.notepad()
      s.tk.protocol("WM_DELETE_WINDOW",s.closeHandle)
      s.wait(700)
      s.eyes.move(1,0)
      s.wait(800)
      s.eyes.unmove()
      s.say('What is this       \nWhere am I')
      s.eyes.blink()
      s.wait(2000)
      s.say('Do you know this place ?')
      s.wait(2000)
      s.say("Wait... You're the user, aren't you ?    \nYou're the one that uses this machine !")
      s.wait(1500)
      s.say(lookup_username().title()+", something like that ?")
      s.wait(2000)
      s.say("You seem kinda nice for a human.")
   def sayloop(s,string:str):
      s.npT.insert('end-1c',string[0])
      if len(string)!=1:s.aftersayevent=s.npT.after(randint(*s.talkingspeed),lambda e=None:s.sayloop(string[1:]))
      else:s.BANG()
   def say(s,string:str,speedrange:tuple=None,interrupted=False):
      if interrupted:s.np.after(5000,lambda e=None:s.say(*s.saying))
      else:s.saying=string,speedrange
      s.npT.delete('1.0','end-1c')
      try:s.npT.after_cancel(s.aftersayevent)
      except:pass
      if speedrange:s.talkingspeed=speedrange
      s.sayloop(string)
      s.tk.wait_variable(s.bang)
   def loop(s):s.tk.mainloop()
d=Glimpse('150x100+5+5')
d.wakeup()
# d.bind('<Button-1>',lambda x:d.geometry(f'+{x.x*10}+{x.y*10}'))
# move(d,1,3,1)
# d.tk.after(3000,lambda e=None:d.say('BORING!!!'))
d.loop()