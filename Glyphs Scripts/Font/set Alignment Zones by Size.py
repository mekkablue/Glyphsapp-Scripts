#MenuTitle: Set Alignment Zones by Size
'''
enter a Value for the AZ and the script adds the zones according to your Font Dimensions

let me know if you have ideas for improving;
Mark Froemberg aka DeutschMark @ GitHub
https://github.com/DeutschMark/Glyphsapp-Scripts
'''

font = Glyphs.currentDocument.font
master = font.masters[0]

### this is your desired zone size:
size = 13

### -------------------------------
### the untouchable code:
### get the dimensions of the font
posA = master.ascender
posC = master.capHeight
posX = master.xHeight
posB = 0
posD = master.descender

dimensions = [
    (posA, size), 
    (posC, size), 
    (posX, size), 
    (posB, -size), 
    (posD, -size)
]

newZones = []
for d in dimensions:
    pos, size = d
    a = GSAlignmentZone.alloc().init()
    a.setSize_(size)
    a.setPosition_(pos)
    newZones.append(a)

font.disableUpdateInterface()

master.setAlignmentZones_(newZones)
#print master.alignmentZones

font.enableUpdateInterface()
