#MenuTitle: Set Size for Alignment Zones
'''
enter a Value for the AZ and the script adds the zones according to your Font Dimensions

let me know if you have ideas for improving;
Mark Froemberg aka DeutschMark @ GitHub
https://github.com/DeutschMark/Glyphsapp-Scripts
'''
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
Selection = Font.selectedLayers

#print Font.fontMasters
for master in Font.masters:
	print master
print

class Window( object ):
    def __init__( self ):
        InputPosX = 90
        InputWidth = 50
        textHeight = 40
        self.w = vanilla.FloatingWindow( (250, 45), "set Alignment Zones" )
        
        self.w.suffixText = vanilla.TextBox((10, 10, -10, textHeight), "AZ Size:")
        self.w.suffixValue = vanilla.EditText((InputPosX, 10, InputWidth, 20), "15", sizeStyle='small')
        self.w.make_button = vanilla.Button((-80, 12, -15, 17), "Create", sizeStyle='small', callback=self.addSuffix)
    
        self.w.open()

    def addSuffix(self, sender):
    	size = int(self.w.suffixValue.get())
    		
	### the untouchable code:
	### get the dimensions of the font
	for master in Font.masters:
		print master
		posA = master.ascender
		posC = master.capHeight
		posX = master.xHeight
		posB = 0
		posD = master.descender

		dimensions = [ (posA, size), (posC, size), (posX, size), (posB, -size), (posD, -size) ]

		print dimensions
		newZones = []
		for d in dimensions:
			pos, size = d
			a = GSAlignmentZone.alloc().init()
			a.setSize_(size)
			a.setPosition_(pos)
			newZones.append(a)	

		#font.disableUpdateInterface()

		master.setAlignmentZones_(newZones)
		#print master.alignmentZones

		#font.enableUpdateInterface()
		self.w.close()
		
Window()
