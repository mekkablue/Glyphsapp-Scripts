#MenuTitle: Tab with selected letters between HOH
# -*- coding: utf-8 -*-

# ###################################################################
#
# Opens a new tab with the selected letters and put them between a
# bunch of HOH*HOHO etc
#
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
#
# ToDo: solve the twisted 'size' variable
#
# ###################################################################

import GlyphsApp
from PyObjCTools.AppHelper import callAfter

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

keyChars = "/H/O/H"

namesOfSelectedGlyphs = ["/" + l.parent.name for l in selectedLayers]
editString = ""

editString += keyChars
for GlyphName in namesOfSelectedGlyphs:
	editString += ( GlyphName + keyChars )

print "output:", editString
callAfter(Glyphs.currentDocument.windowController().addTabWithString_, editString)
