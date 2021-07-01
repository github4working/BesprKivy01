import kivy


kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


from kivy.core.window import Window
from kivy.clock import Clock
import re #regular expression


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 5
        Window.size = (300, 28)


        self.start = Button(text='Start')                                           # on enter
        #self.start.bind(on_press=self.btn)                                  # Eingabefehler abfangen
        self.start.bind(on_press=self.start_calc)

        self.add_widget(self.start)

        self.add_widget(Label(text='Anz'))

        self.anz_mitarb = TextInput(multiline=False, hint_text='15')  # is_focusable=True, focused=True)
        self.add_widget(self.anz_mitarb)

        self.add_widget(Label(text='Lohn'))
        self.stdlohn = TextInput(multiline=False, hint_text='20')
        self.add_widget(self.stdlohn)


    # def start_popup(self, instance):
    #     Window.size = (400, 400)
    #     self.start.bind(on_press=self.popup.open)
    #
    # def on_enter(self):
    #     Clock.schedule_once(self.start_calc)


    #
    # def press_enter(self):
    #     pass


    def start_calc(self, instance):
        self.clear(instance)
        self.new_win()
        self.on_start()


    def clear(self, instance):
        MyGrid.clear_widgets(self, children=None)

    def new_win(self):
        Window.size = (220, 28)
        self.cols = 1
        self.total = Label(text='0')
        self.add_widget(self.total)

    def on_start(self):
        Clock.schedule_interval(self.update_label, 1)

    def update_label(self, *args):
        self.get_values()

        self.total_p_min = float(self.total_str) + (self.amount * self.wage) / 3600
        self.total.text = str("{0:.2f}".format(self.total_p_min))+'€'



    def get_values(self):
        pattern = re.compile("[A-Za-z]+")
        self.total_str = '0'


        # if (self.anz_mitarb.text is '' or self.stdlohn.text is ''):
        #     print('String leer')

        #
        #
        # elif(pattern.fullmatch(self.anz_mitarb.text)):
        #     print('String enthält Buchstaben!')
        #     #self.anz_mitarb.text = ''
        #     #self.stdlohn.text = ''
        #     #self.update_label()
        #
        # elif(pattern.fullmatch(self.stdlohn.text)):
        #     print('String enthält Buchstaben!')
        #
        # else:
        self.total_nb = re.search('\d+[,.]\d+|\d+', self.total.text)
        self.total_str = str(self.total_nb[0])
        self.amount = float(self.anz_mitarb.text)
        self.wage = float(self.stdlohn.text)

#     def btn(self):
#         show_popup()
#
# def show_popup():
#     show_popup = P()
#
#     popupWindow = Popup(title='test', content = show_popup, size_hint=(None, None), size=(400,400))
#     popupWindow.open()

# class P(FloatLayout):
#     self.start = Button(text='Start')
#     self.add_widget(self.start)
#     self.add_widget(Label(text='Lohn'))

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()