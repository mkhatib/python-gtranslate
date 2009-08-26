#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygtk
pygtk.require('2.0')
import gtk
from gtlib import translate as translate
import languages


# Class main contains the GUI and event Handlers
class Main(object):
	
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False
	# Initializing the Variables and components
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Translate!")
		self.window.connect('delete_event', self.delete_event)
		self.field_hbox = gtk.HBox(False, 0)
		self.languages_hbox = gtk.HBox(False, 0)
		self.vbox = gtk.VBox(False, 0)
		self.vbox.add(self.field_hbox)
		self.window.add(self.vbox)

		self.input_field = gtk.Entry()
		self.button = gtk.Button('Translate')
		self.button.connect('clicked', self.handleTranslate)
		#self.result_field = gtk.Entry()
		self.languages_buttons = []
                for lang in languages.LANGUAGES_CODES.items():
			lb = gtk.ToggleButton(lang[0])
			self.languages_buttons.append(lb)
			self.languages_hbox.add(lb)
		
		self.field_hbox.add(self.input_field)
		self.field_hbox.add(self.button)
		self.vbox.add(self.field_hbox)
		self.vbox.add(self.languages_hbox)
		#self.vbox.add(self.result_field)

		self.window.show_all()

	# Handle the Translate Button Click
	def handleTranslate(self, widget):
		#self.result_field.set_text('Loading...')
		to_langs = ''
		for lb in self.languages_buttons:
			if lb.get_active(): to_langs += languages.LANGUAGES_CODES[lb.get_label()] + ' '

		if len(to_langs.strip()) == 0: return
		result = translate(self.input_field.get_text(), to_langs.strip())
		for c in self.vbox.children()[2:]:
			self.vbox.remove(c)	
		
		
		for lang in result.items():
			result_field = gtk.Entry()
			result_field.set_text(lang[1].strip())
			field_hbox = gtk.HBox(False, 0)
			field_label = gtk.Label(languages.CODES_LANGUAGES[lang[0]])
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
