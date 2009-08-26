#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygtk
pygtk.require('2.0')
import gtk
from gtlib import translate as translate

# Class main contains the GUI and event Handlers
class Main(object):
	# Initializing the Variables and components
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Translate!")
		self.hbox = gtk.HBox(False, 0)
		self.vbox = gtk.VBox(False, 0)
		self.vbox.add(self.hbox)
		self.window.add(self.vbox)

		self.input_field = gtk.Entry()
		self.button = gtk.Button('Translate')
		self.button.connect('clicked', self.handleTranslate)
		#self.result_field = gtk.Entry()

		self.hbox.add(self.input_field)
		self.hbox.add(self.button)
		self.vbox.add(self.hbox)
		#self.vbox.add(self.result_field)

		self.window.show_all()

	# Handle the Translate Button Click
	def handleTranslate(self, widget):
		#self.result_field.set_text('Loading...')
		result = translate(self.input_field.get_text(), 'en ar es ja fa zh hi')
		for c in self.vbox.children()[1:]:
			self.vbox.remove(c)	#.remove_all()# = gtk.VBox(False, 0)	
		#self.vbox.add(self.hbox)
		for lang in result.items():
			result_field = gtk.Entry()
			result_field.set_text(lang[1].strip())
			field_hbox = gtk.HBox(False, 0)
			field_label = gtk.Label(lang[0])
			field_hbox.add(field_label)
			field_hbox.add(result_field)
			self.vbox.add(field_hbox)
			field_hbox.show_all()
			#text += lang[1]
		#self.window.add(self.vbox)			
		#self.result_field.set_text(text.strip().decode('utf-8'))


def main():
	gtk.main()

if __name__ == '__main__':
	o = Main()
	main()
