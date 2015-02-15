#MenuTitle: Create empty .suffix Glyphs from selected Glyphs

# ###################################################################
#
# select the Characters to copy, put a suffix and get copies with
# the according suffix
#
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
# --> www.mirque.de <--
#
# ToDo: - make a Version that creates unempty Copies
#
# ###################################################################

import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
Selection = Font.selectedLayers
#help(Font)

listOfGlyphNames = [ x.parent.name for x in Selection ]

class Window( object ):
    def __init__( self ):
        InputPosX = 90
        InputWidth = 50
        textHeight = 40
        self.w = vanilla.FloatingWindow( (250, 45), "suffix glyphs" )
        
        self.w.suffixText = vanilla.TextBox((10, 10, -10, textHeight), "suffix:")
        self.w.suffixValue = vanilla.EditText((InputPosX, 10, InputWidth, 20), ".ss01", sizeStyle='small')

        self.w.make_button = vanilla.Button((-80, 12, -15, 17), "Create", sizeStyle='small', callback=self.addSuffix)
    
        self.w.open()

		
    def buttonCheck( self, sender ):
        myClassName = sender.get()
        listOfGlyphNames
        


    def addSuffix(self, sender):
        
        suffix = self.w.suffixValue.get()
        print suffix
                
        for letter in listOfGlyphNames:
            print letter
            glyph = letter + suffix
            print glyph
        
            newglyph = GSGlyph(glyph)
            newglyph.setLeftMetricsKey_(letter)
            newglyph.setRightMetricsKey_(letter)
            Font.addGlyph_(newglyph)
            
            
            
	

Window()
