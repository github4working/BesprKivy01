import kivy

kivy.require('1.11.1')
# Testcommentary
#1
#2
#3

# Testcommentary
#1
#2
#3
from kivy.config import Config
Config.set('graphics', 'width', "300")
Config.set('graphics', 'height', '40')
# Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

#from KivyOnTop import register_topmost

from kivy.core.window import Window
from kivy.clock import Clock
import re #regular expression

ticker = 0

                                                                #Builder.load_string('''MyGrid: ''')
class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 5
        #Window.clearcolor = (0.282, 0.31, 0.34, 0)

        Window.bind(on_key_down=self.key_pressed)

        self.start = Button(text='Start', background_normal='')
        #self.start.bind(on_press=self.btn)                                  # Eingabefehler abfangen
        self.start.bind(on_press=self.start_calc)

        self.add_widget(self.start)

        self.add_widget(Label(text='Anz', color=(0,0,0,1), bold= True))

        self.anz_mitarb = TextInput(input_filter="float", multiline=False, hint_text='15', halign="center", padding=[0, 11, 0, 11])  #is_focusable=True, focused=True)
        self.add_widget(self.anz_mitarb)

        self.add_widget(Label(text='Lohn', color=(0,0,0,1), bold= True))
        self.stdlohn = TextInput(input_filter="float", multiline=False, hint_text='77', halign="center", padding=[0, 11, 0, 11])
        self.add_widget(self.stdlohn)

    def key_pressed(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.start_calc(instance)


    def start_calc(self, instance):
        self.clear(instance)
        self.new_win()
        self.start_pressed()


    def clear(self, instance):
        MyGrid.clear_widgets(self, children=None)

    def new_win(self):
        Window.size = (220, 28)
        self.cols = 1
        self.total = Label(text='0')
        self.add_widget(self.total)

    def start_pressed(self):
        Clock.schedule_interval(self.update_label, 1)

    def update_label(self, *args):
        global ticker
        self.get_values()

        ticker = ticker + (self.amount * self.wage) / 3600
        self.total.text = str(round(ticker, 2)) + '€'

    def get_values(self):
        if self.anz_mitarb.text == '':
            self.amount = float(self.anz_mitarb.hint_text)
        else:
            self.amount = float(self.anz_mitarb.text)

        if self.stdlohn.text == '':
            self.wage = float(self.stdlohn.hint_text)
        else:
            self.wage = float(self.stdlohn.text)


class MyApp(App):
    # def on_start(self, *args):
    #     TITLE = 'Grenzebach MeetingValue'
    #     Window.set_title(TITLE)
    #     register_topmost(Window, TITLE)
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()