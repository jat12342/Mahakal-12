from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.toast.kivytoast.kivytoast import toast
from kivy.uix.image import Image
from kivymd.uix.carousel import MDCarousel
import sqlite3
import webbrowser 
from kivy.core.audio import SoundLoader
from gtts import gTTS



kv='''
Manager:
    Fr:
    Fir:
    Sec:
 
<Fr>:
    name:'fr'          
    FitImage:
        source:'assests/a7.png'
        
    MDLabel:
        text:'ENTER YOU NAME:- '       
        pos_hint:{'center_x':0.5,'center_y':0.8} 
        bold:True             
        md_text_color:1,0,0,0                                       
    MDTextField:
        id:f1
        pos_hint:{'center_x':0.9,'center_y':0.8}
        bold:True                                                                           
    MDFloatingActionButton:
        id:fa1
        on_press:
            app.con()                                                                                                                                                                                                      
                                                                            
<Fir>:
    name:'home'
    FitImage:
        source:'assests/a7.png'
    MDCarousel:
        id:c1
        direction:'right'
        pos_hint : {'center_x':0.5,'center_y':0.74}
        size_hint_y:0.5
         





    MDTopAppBar:
        id:ab1
        title:'OUR APP '
        md_bg_color:1,0,0,1
        pos_hint:{'top':1}
        left_action_items:[['menu',lambda x:nd1.set_state('open')]]
            
    MDNavigationDrawer:
        id:nd1
        FitImage:
            source:'assests/b1.png'
        
               


<Sec>:
    name:'s2'    











'''




class Fr(Screen):
    pass

class Fir(Screen):
    pass
    
class Sec(Screen):
    pass

class Manager(ScreenManager):
    pass





class Demo(MDApp):
    def build(self):
        self.u= Builder.load_string(kv)
        return self.u
        
        
    def on_start(self):
        a = 0
        for i in range(0,8):
            self.u.get_screen('home').ids.c1.add_widget(Image(source=f'assests/a{a}.png'))  
            a += 1   
            
    def con(self):
        try:
            cd=self.u.get_screen('fr').ids.f1.text
            d=f'HELLO {cd} WELCOME IN OUR APP'
            g = gTTS(text=d,lang='hi',slow=False)
            g.save('jw.mp3')
            S = SoundLoader.load('/storage/emulated/0/jw.mp3')
            S.play()
            self.u.current = 'home'
            
        
        except Exception as e:
            toast(e)           
        


Demo().run()

