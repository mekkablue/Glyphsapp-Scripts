#MenuTitle: Set Alignment Zones by Size
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
#help(Font)

#print Font.fontMasters
#print Font.masters

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

		
    def buttonCheck( self, sender ):
        size = sender.get()
        

    def addSuffix(self, sender):
    		size = int(self.w.suffixValue.get())
    		print size
    		
		### the untouchable code:
		### get the dimensions of the font
		master = Font.masters[0]
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
