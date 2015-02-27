#MenuTitle: Note for Selection
# -*- coding: utf-8 -*-
__doc__="""
Add a note to all selected characters (UI)
"""
# ###################################################################
# 
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
# --> www.mirque.de <--
#
# ToDo: -
#
# ###################################################################

Glyphs.clearLog()
from robofab.interface.all.dialogs import AskString
Note = AskString("What is your Note for the Selected Glyphs?")

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
	thisGlyph.setNote_(Note)
	
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
	print "%s -->" % thisGlyph.name, Note

Glyphs.showMacroWindow()
