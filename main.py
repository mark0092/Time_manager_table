from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (480,853)

#from kivy.config import config
#Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivymd.theming import  ThemeManager

class Container(Screen):
	clock_time = NumericProperty(0.0)
	event = None

	def lock_time(self):
		hours = int(self.clock_time / 3600)
		minutes = int(self.clock_time / 60) % 60
		seconds = int(self.clock_time) % 60
		self.time_view.text = ":".join([str(hours), str(minutes), str(seconds)]) 

	def time_up(self, dt):
		self.clock_time += dt
		self.lock_time() 

	def break_time(self):
		self.start_b.text = "Start"
		if (self.event != None):
			self.event.cancel()
			self.event = None
		self.clock_time = 0
		self.lock_time()

	def start_click(self):
		if (self.start_b.text == "Start"):
			self.start_b.text = "Pause"
			self.event = Clock.schedule_interval(self.time_up, 0.5)
		else:
			self.start_b.text = "Start"
			if (self.event != None):
				self.event.cancel()
				self.event = None
			self.lock_time()

class Archive(Screen):
	pass


class TmApp(App):
	theme_cls = ThemeManager()
	title = 'Time manager'
	def build(self):
		sm = ScreenManager()
		sm.add_widget(Container(name='menu'))
		sm.add_widget(Archive(name='archive'))
		self.theme_cls.theme_style = 'Light'
		return sm


if __name__ == '__main__':
	TmApp().run()