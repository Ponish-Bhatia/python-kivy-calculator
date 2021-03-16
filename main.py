from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup 
import math
class MyLayout(Widget):
	def buttonpressnumber(self, texta):
		symbol_added_boy=False
		try:
			int(texta)
			self.ids.potato.text = self.ids.potato.text + '{}'.format(texta)
			symbol_added_boy=False
		except ValueError:
			try:
				if texta=='+' or texta=='-' or texta=='*' or texta=='/' or texta=='(' or texta==')' or texta=='exp':
					if not texta=='exp':
						if symbol_added_boy==True:
							self.ids.potato.text=self.ids.potato.text[0]+texta
						else:
							self.ids.potato.text = self.ids.potato.text + '{}'.format(texta)
							symbol_added_boy=True
					else:
						if symbol_added_boy==True:
							self.ids.potato.text.pop()
							self.ids.potato.text = self.ids.potato.text + '{}'.format('**')
						else:
							self.ids.potato.text = self.ids.potato.text + '{}'.format('**')
							symbol_added_boy=True
				elif texta=='clear':
						self.ids.potato.text = ''
						#self.ids.potato.text self.ids.potato.text self.ids.potato.text
				elif texta=='<------':
					c = list(self.ids.potato.text)
					c.pop()
					d = ''
					for n in c:
						g = n 
						d = d + g
						r = n
					self.ids.potato.text = d
				elif texta=='sqr rt':
					self.ids.potato.text = self.ids.potato.text + '{}'.format('math.sqrt(') 
				elif texta=='=':
					exec('self.ids.potato.text' + ' ' + '=' + ' ' + 'str(' + self.ids.potato.text + '' + ')')
				elif texta=='.':
					self.ids.potato.text = self.ids.potato.text + '{}'.format('.') 
			except Exception:
				a = '''GridLayout:
		cols:1
			Label:
				text:'Think before writing mad by the TextBox'
			Button:
				onpress:root.dismiss
				text:'I promise that I wont do that again' '''
				m = GridLayout(cols=1, rows=8)
				m.add_widget(Label(text='Hi....'))
				m.add_widget(Label(text='I met an '))
				m.add_widget(Label(text='idiot'))
				m.add_widget(Label(text='first time in my life...'))
				m.add_widget(Label(text='Do you know that'))
				m.add_widget(Label(text='you added invalid data?'))
				m.add_widget(Label(text='If not then yap.'))
				butt = Button(text='I promise that I wont do that again')
				m.add_widget(butt)
				ponish = Popup(title='Bad INpuT', content=m) # Builder.load_string(a))
				butt.bind(on_press=ponish.dismiss)
				ponish.open()
	Builder.load_file(".\\awsome.kv")

class AwsomeApp(App):
	def build(self):
		self.title = 'calculator'
		self.icon  = './calcula.ico'
		return MyLayout()
if __name__ == '__main__':
	AwsomeApp().run()
