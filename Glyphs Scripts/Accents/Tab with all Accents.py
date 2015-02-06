#MenuTitle: Tab w/ all Accents

# ###################################################################
#
# all accents that are in the font so far (complete list)
# 
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
#
# ToDo: - get rid of GUI and add Uppercase OR:
#       - make Dropdown for UC and LC
#
# ###################################################################


import GlyphsApp
import vanilla
from robofab.gString import dependencies, uppercase_accents, uppercase_plain, lowercase_accents, lowercase_plain


# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()


class OpenTab(object):
	def __init__(self):
		self.accentList = self.accents()
		
		self.w = vanilla.FloatingWindow((500, 100), "Open Tab:")
		self.w.myTextBox = vanilla.TextBox((10, 10, -10, 40), "Open Tab wit these guys:")
		self.w.editText = vanilla.EditText((10, 30, -100, 50), self.accentList, sizeStyle='small', callback=self.editTextCallback)
		self.w.myButton = vanilla.Button((410, 30, -10, 20), "Do it!", sizeStyle='small', callback=self.buttonCallback) 
		self.w.setDefaultButton( self.w.myButton )
		self.w.open()
	

	def accents(self):
		accentList = ""
		#ucAndLc = lowercase_plain + uppercase_plain + lowercase_special_accents + uppercase_special_accents + moreSpecial
		ucAndLc = lowercase_plain + uppercase_plain
		for l in ucAndLc:
			#print l,
			accentList += "/"+ l
			try:
				for d in dependencies[l]:
					accentList += "/"+ d
					#print accentList,
					#print d,
			except KeyError:
				#print
				continue
		return accentList
		#print accentList
	
			
	def editTextCallback(self, sender):
		print "text entry:", sender.get()
		
	def buttonCallback(self, sender):
		print self.accentList
		Glyphs.currentDocument.windowController().addTabWithString_( self.accentList )
		self.w.close()
		
OpenTab()

