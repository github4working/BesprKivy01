import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols  = 2

        self.inside.add_widget(Label(text="First Name: "))

        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name"))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        # self.add_widget(self.ins_inside)

    def pressed(self, instance):
        print("Pressed")

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run()
