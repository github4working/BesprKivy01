import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
import kivy.clock


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)                  #Fenster verkleinern
        self.cols = 6
        Window.size = (300, 40)
                                                                #Berechnung der Werte
                                                                #verankern
        self.start = Button(text='Start')

        self.start.bind(on_press=self.start_calc)
        self.add_widget(self.start)

        self.add_widget(Label(text= 'Verbrauch €'))

        self.add_widget(Label(text='Anz'))
        self.anz_mitarb = TextInput(multiline=False, hint_text='15')
        self.add_widget(self.anz_mitarb)

        self.add_widget(Label(text='Lohn'))
        self.stdlohn = TextInput(multiline=False, hint_text='20', )
        self.add_widget(self.stdlohn)

    def start_calc(self, instance):
        self.clear(instance)
        self.show_label()
        self.verbrauch(instance)


    def clear(self, instance):
        MyGrid.clear_widgets(self, children=None)

    def verbrauch(self, instance):
         # self.anzahl = int(self.anz_mitarb.text)
         # self.lohn = int(self.stdlohn.text)
        # self.verbrauch = anzahl * (lohn / 60)           #jede Sekunde
        # self.gesamt+=self.verbrauch
        #
        # self.anz_mitarb.text = ""
        # self.stdlohn.text = ""
        pass

    def show_label(self):
        self.cols = 1
        Window.size = (300, 40)
        self.add_widget(Label('Verbrauch €'))



    #def my_callback(dt):
        #pass

    #Clock.schedule_interval(my_callback, 1)






class MyApp(App):
    def build(self):
        return MyGrid()




if __name__ == "__main__":
    MyApp().run()