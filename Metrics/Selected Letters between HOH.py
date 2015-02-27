#MenuTitle: Tab with selected letters between HOH
# -*- coding: utf-8 -*-
__doc__="""
New Tab with selected characters as placeholders between HH*HHOO*OO
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
