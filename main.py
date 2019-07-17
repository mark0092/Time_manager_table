from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (480,853)

class Container(GridLayout):
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
		self.start_b.text = "Старт"
		if (self.event != None):
			self.event.cancel()
			self.event = None
		self.clock_time = 0
		self.lock_time()

	def start_click(self):
		if (self.start_b.text == "Старт"):
			self.start_b.text = "Пауза"
			self.event = Clock.schedule_interval(self.time_up, 0.5)
		else:
			self.start_b.text = "Старт"
			if (self.event != None):
				self.event.cancel()
				self.event = None
			self.lock_time()

class TmApp(App):
	def build(self):
		cont = Container()
		return cont


if __name__ == '__main__':
	TmApp().run()