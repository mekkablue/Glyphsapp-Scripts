#MenuTitle: Set ShowInterpolation Color.py
# -*- coding: utf-8 -*-
__doc__="""
Set the interpolation color for all instances. Visible when Show Interpolations filter is active.
"""
# ###################################################################
#
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
# --> www.mirque.de <--
#
# ToDo: - Make NSColor output less hacky
#
# ###################################################################

import GlyphsApp
from AppKit import NSColor
from vanilla import *

thisFont = Glyphs.font # frontmost font
Glyphs.clearLog()
thisFont.disableUpdateInterface() # suppresses UI updates in Font View

class ColorWellWindow(object):

    def __init__(self):
        self.w = Window((150, 50), "set color")
        self.w.colorWell = ColorWell((10, 10, -10, -10),
                            callback=self.colorWellEdit,
                            color=NSColor.redColor())
        self.w.open()

    def colorWellEdit(self, sender):
        #print "color well edit!", sender.get()
        color = str(sender.get())
        color2 = color.split(" ")
        color3 = ";".join(color2[1:-1])

        ## CP Handling
        cpName = "ShowInterpolation"
        cpValue = color3

        ### OVERWRITING existing CP
        for instance in thisFont.instances:
            instance.customParameters[cpName] = cpValue

ColorWellWindow()

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
