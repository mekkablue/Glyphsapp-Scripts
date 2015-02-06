#MenuTitle: Show FontInfo for Instances

#Doc = Glyphs.currentDocument
thisFont = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

print thisFont.familyName, "\n"
for instance in thisFont.instances:
	if instance.active:		
		print '"%s" (%s)\n--> active' % ( instance.name, instance.weight )
	else:
		print '("%s" (%s))' % ( instance.name, instance.weight )
	if instance.isItalic:
		print "is Italic"
	if instance.isBold:
		print "is the Bold linked to: %s" % instance.linkStyle
	print "Interpolation Values:\n\tWeight:\t%s [%s]\n\tWidth:\t%s [%s] " % ( instance.weight, instance.weightValue, instance.width, instance.widthValue )
	if instance.customParameters:
		print instance.customParameters
	print