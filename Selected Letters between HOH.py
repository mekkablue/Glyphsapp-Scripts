#MenuTitle: selected letters between HOH
# -*- coding: utf-8 -*-
"""Opens a new tab with the selected letters and put them between a string ofHOH."""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

keyChars = "/H/O/H"

namesOfSelectedGlyphs = ["/" + l.parent.name for l in selectedLayers]
editString = ""

editString += keyChars
for GlyphName in namesOfSelectedGlyphs:
	editString += ( GlyphName + keyChars )

print output, editString
Doc.windowController().addTabWithString_( editString )
