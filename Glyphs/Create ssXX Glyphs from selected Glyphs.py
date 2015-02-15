#MenuTitle: Create empty .ssXX-Copies from selected Glyphs

# ###################################################################
#
# select the Characters to copy, put a number and get XX copies with
# the according .ssXX suffix
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

# help(Font)

listOfGlyphNames = [ x.parent.name for x in Selection ]


class Window( object ):
    def __init__( self ):
        self.w = vanilla.FloatingWindow( (150, 45), ".ssXX" )

        self.w.popUpButton = vanilla.PopUpButton((10, 10, -90, 20), [str(i+1) for i in range(20)])
        self.w.make_button = vanilla.Button((-80, 12, -15, 17), "Create", sizeStyle='small', callback=self.addSuffix)
    
        self.w.open()

		
    def buttonCheck( self, sender ):
        myClassName = sender.get()
        listOfGlyphNames


    def addSuffix(self, sender):

        #print listOfGlyphNames
                
        index = self.w.popUpButton.get()
        value = self.w.popUpButton.getItems()[index]
        
        amount = int(value)
        print amount

        suffix = ".ss"
                
        for i in range(amount):
            for letter in listOfGlyphNames:
                ### best version: add .zfill(2) after the suffx:
                glyph = letter + suffix + str(i+1).zfill(2)
                print glyph
                
                newglyph = GSGlyph(glyph)
                newglyph.setLeftMetricsKey_(letter)
                newglyph.setRightMetricsKey_(letter)
                Font.addGlyph_(newglyph)
        
        self.w.close()

Window()
