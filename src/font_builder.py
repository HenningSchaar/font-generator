from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.fontBuilder import FontBuilder as FBuilder

class FontBuilder:
    def __init__(self):
        self.font_builder = FBuilder(1000, isTTF=True)
        self.glyphs = {}
        self.widths = {}  # Store width for each glyph
        
        # Add .notdef glyph (required)
        pen = TTGlyphPen(None)
        pen.moveTo((0, 0))
        pen.lineTo((0, 1000))
        pen.lineTo((1000, 1000))
        pen.lineTo((1000, 0))
        pen.closePath()
        self.glyphs['.notdef'] = pen.glyph()
        self.widths['.notdef'] = 1000
        
    def add_character(self, char, bitmap):
        # Create a new glyph using TTGlyphPen
        pen = TTGlyphPen(None)
        
        # Scale factor to fit the em square
        scale = 1000 / max(bitmap.shape[0], bitmap.shape[1])
        
        # Calculate actual width for this character
        width = int(bitmap.shape[1] * scale)
        
        for y in range(bitmap.shape[0]):
            for x in range(bitmap.shape[1]):
                if bitmap[y, x]:
                    x_pos = x * scale
                    y_pos = (bitmap.shape[0] - y) * scale
                    pen.moveTo((x_pos, y_pos))
                    pen.lineTo((x_pos + scale, y_pos))
                    pen.lineTo((x_pos + scale, y_pos - scale))
                    pen.lineTo((x_pos, y_pos - scale))
                    pen.closePath()
        
        # Store the glyph and its width
        self.glyphs[char] = pen.glyph()
        self.widths[char] = width + 50  # Add some padding between characters

    def save_font(self, font_name):
        # Setup basic font info
        glyph_order = ['.notdef'] + sorted(k for k in self.glyphs.keys() if k != '.notdef')
        self.font_builder.setupGlyphOrder(glyph_order)
        
        # Setup character map (excluding .notdef)
        cmap = {ord(char): char for char in self.glyphs.keys() if char != '.notdef'}
        self.font_builder.setupCharacterMap(cmap)
        
        # Setup glyphs
        self.font_builder.setupGlyf(self.glyphs)
        
        # Set up metrics with actual character widths
        metrics = {char: (self.widths[char], 0) for char in glyph_order}
        self.font_builder.setupHorizontalMetrics(metrics)
        
        # Set up other required tables
        self.font_builder.setupHorizontalHeader(ascent=800, descent=200)
        self.font_builder.setupNameTable({
            "familyName": "Heavy Clouds",
            "styleName": "Regular",
            "uniqueFontIdentifier": "HeavyClouds-Regular",
            "fullName": "Heavy Clouds Regular",
            "version": "Version 1.0",
            "psName": "HeavyClouds-Regular",
            "manufacturer": "Custom",
            "copyright": "Copyright (c) 2024"
        })
        self.font_builder.setupOS2()
        self.font_builder.setupPost()
        
        # Save the font
        self.font_builder.save(f"{font_name}.ttf")