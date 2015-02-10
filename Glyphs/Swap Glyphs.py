#MenuTitle: Swap Glyphs

# ###################################################################
#
# Swaps 2 Characters (basically just renaming each other)
# 
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
#
# ToDo: - 
#
# ###################################################################

Doc = Glyphs.currentDocument
Font = Glyphs.font
Selection = Font.selectedLayers

listOfGlyphNames = [ x.parent.name for x in Selection ]

if len(listOfGlyphNames) == 2:
    Selection[1].parent.name = "Temp"

    print listOfGlyphNames
    Selection[0].parent.name = listOfGlyphNames[1]
    Selection[1].parent.name = listOfGlyphNames[0]
else:
    #pass
    from robofab.interface.all.dialogs import Message
    Message("Select only TWO glyphs")

    

