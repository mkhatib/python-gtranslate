import sys
import gtk
import pygtk
from gtlib import translate as translate

# Class main contains the GUI and event Handlers
class Main(object):
	# Initializing the Variables and components
	def __init__(self):
		self.window = Window()
		self.text_field = TextField()
		self.button = Button('Translate')
		self.button.connect('click', self.handleTranslate)
		self.text_area = TextArea()
		self.show()

	# Showing the UI
	def show(self):
		self.window.add(self.text_field)
		self.window.add(self.button)
		self.window.add(self.text_area)
		self.window.show_all()

	# Handle the Translate Button Click
	def handleTranslate(self):
		self.text_area.setValue('Loading...')
		result = translate(self.text_field.getValue())
		text = ''
		for lang in result.items():
			text += lang[0] + ' - ' + lang[1]
			
		self.text_area.setText(text)



if __name__ == '__main__':
	main()