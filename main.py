from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.core.window import Window
import webbrowser
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
Window.size = (300, 500)


def webbrowser2():
    webbrowser.open('http://www.anywebsite.domain')


screen_helper = """
ScreenManager:
    LandingScreen:
    TypeScreen:
    NoteScreen:
    MenuScreen:

<LandingScreen>:
    name: 'land'
    MDIconButton:
        halign: "center"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        icon: "typewriter"
        user_font_size: "120sp"
        on_press: root.manager.current = 'menu'
    MDLabel:
        text: 'Created by Rharm Manju'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        theme_text_color: "Hint"




<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'SimText'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDRoundFlatButton:
        text: 'Type'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'type'
    MDRoundFlatButton:
        text: 'Notes'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'note'
    MDLabel:
        text: 'Menu'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H4'
    MDIconButton:
        halign: "center"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        icon: "typewriter"
        user_font_size: "120sp"
        on_press: 
 
<TypeScreen>:
    label_wid: label_field
    name: 'type'
    MDLabel:
        text: 'SimText'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDLabel:
        text: 'Type'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H4'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'menu'
    MDTextField:
        id: text_field
        multiline: True
        size_hint: (.95, None)
        hint_text: ''
        pos_hint: {'center_x':0.5,'center_y':0.5}
        font_size: '14'
    MDIconButton:
        icon: "typewriter"
        user_font_size: "30sp"
        ripple_scale: .5
        pos_hint: {"center_y": .51}
        pos: text_field.width - self.width + dp(8), 0
        on_press: label_field.text = text_field.text
        on_release: text_field.text = ''
        
    MDLabel:
        id: label_field
        text: ''
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        theme_text_color: "Hint"
     
    
    
    

    

<NoteScreen>:
    name: 'note'
    MDLabel:
        text: 'SimText'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDLabel:
        text: 'Notes'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass


class TypeScreen(Screen):
    pass


class NoteScreen(Screen):
    pass


class LandingScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(TypeScreen(name='type'))
sm.add_widget(NoteScreen(name='note'))
sm.add_widget(TypeScreen(name='land'))


class AppApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(screen_helper)
        return self.screen


    def gettext(self, text):
        self.label_field.text = text


AppApp().run()
