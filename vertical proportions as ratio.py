#MenuTitle: Vertical Proportions as Ratio
'''
put your desired proportions for instance 5 : 10 : 5;
it will recalculate whatever your upm is set to;
ignores the cap height for now;
let me know if you have ideas for improving;
Mark Frömberg aka DeutschMark @ GitHub
https://github.com/DeutschMark/Glyphsapp-Scripts
'''

import GlyphsApp
import vanilla

font = Glyphs.font
Layer = font.selectedLayers[0]
master = font.masters[0]
upm = font.upm

class dialog(object):
	def __init__(self):
		InputPosX = 90
		InputWidth = 30
		textHeight = 40

		self.w = vanilla.FloatingWindow((250, 130), "Proportions as Ratio")

		# ascender
		self.w.myTextBox1a = vanilla.TextBox((10, 10, -10, textHeight), "ascender")
		self.w.editTextNr1 = vanilla.EditText((InputPosX, 10, InputWidth, 20), "5.5", sizeStyle='small')
		self.w.myTextBox1b = vanilla.TextBox((130, 10, 10, textHeight), unichr(int('23AB', 16)))
		
		# bracket extension
		self.w.myTextBox2 = vanilla.TextBox((130, 22, 10, textHeight), unichr(int('23AA', 16)))
		
		# xHeight		
		self.w.myTextBox3a = vanilla.TextBox((10, 35, -10, textHeight), "xHeight")
		self.w.editTextNr2 = vanilla.EditText((InputPosX, 35, InputWidth, 20), "10", sizeStyle='small')
		self.w.myTextBox3b = vanilla.TextBox((130, 35, 10, textHeight), unichr(int('23AC', 16)))
		self.w.myTextBox3c = vanilla.TextBox((150, 35, -10, textHeight), str(upm) + " upm")
		
		# bracket extension
		self.w.myTextBox4 = vanilla.TextBox((130, 47, 10, textHeight), unichr(int('23AA', 16)))
		
		# descender
		self.w.myTextBox5a = vanilla.TextBox((10, 60, -10, textHeight), "descender")
		self.w.editTextNr3 = vanilla.EditText((InputPosX, 60, InputWidth, 20), "5", sizeStyle='small')
		self.w.myTextBox5b = vanilla.TextBox((130, 60, 10, textHeight), unichr(int('23AD', 16)))
		
		# Button
		self.w.myButton = vanilla.Button((10, 100, -10, 20), "Do it!", sizeStyle='small', callback=self.buttonCallback) 
		self.w.setDefaultButton( self.w.myButton )
		self.w.open()
	
	def buttonCallback(self, sender):
		ascender = self.w.editTextNr1.get()
		xHeight = self.w.editTextNr2.get()
		descender = self.w.editTextNr3.get()

		### function for calculating
		a = float(ascender)
		b = float(xHeight)
		c = float(descender)
		sumAll = a + b + c
		#print "sum:", sumAll
		a = round(float(ascender) / sumAll * upm)
		b = round(float(xHeight) / sumAll * upm)
		c = round(float(descender) / sumAll * upm)
				
		total = a + b + c
		print "unrounded total upm:", total
		difference = total - upm
		roundedA = a - difference

		print "ascender:", roundedA, "above the xHeight"
		print "xHeight:", b
		print "descender:", -c
		
		master.ascender = roundedA + b		
		master.xHeight = b
		master.descender = -c				
		

dialog()
