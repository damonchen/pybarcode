#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode ean13
# require: PIL package 
# win32(python2.5): http://effbot.org/downloads/PIL-1.1.7.win32-py2.5.exe
# win32(python2.6): http://effbot.org/downloads/PIL-1.1.7.win32-py2.6.exe
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


try:
    import Image, ImageDraw, ImageFont
except ImportError, e:
    raise ImportError("need PIL lib support\n %s" %e.message )

# barcode Exception
class BarcodeException(Exception):
    pass


class BarcodeMetaclass(type):
    def __init__(cls, name, bases, dict):
        super( BarcodeMetaclass, cls).__init__(name, bases, dict)
        if name == 'Barcode':
            return 
        
# define base barcode class as the barcode interface

class Barcode(object):
    name = "Barcode"
    
    def encode_barcode(self,text):
        pass
    
    def make_barcode(self, text, width, height, orient=0, xoffset=0, yoffset=10, align='CENTER', fore_color=(0,0,0), back_color=(255,255,255) ,show_text=False):
        min_width, value = self.encode_barcode(text)
        print value
        if width < min_width:
            width = int(min_width)
        im = Image.new("RGB", (width, height), back_color )
        value_len = len( value )
        bar_width = width / value_len
        
        if align == 'CENTER':
            shift_adjustment = ( width % value_len ) / 2;
        elif align == 'LEFT':
            shift_adjustment = 0
        elif align == 'RIGHT':
            shift_adjustment = ( width % value_len )
        else:
            shift_adjustment = ( width % value_len ) / 2;
            
        bar_width_modifier = 1
        
        draw = ImageDraw.Draw(im)
        
        for pos,v in enumerate(value):
            if v == '1':
                draw.rectangle( (pos*bar_width + shift_adjustment + 1 + xoffset, yoffset,
                            pos*bar_width + shift_adjustment + 1 + xoffset + bar_width/bar_width_modifier - 1, height), 
                            fill=fore_color)
        
        if show_text:
            font = ImageFont.truetype("COUR.TTF", 50)
            twidth, theight = font.getsize(text)  # text length
            # 1/10 * height
            start_y = height - 20 - 3
            pos = (xoffset, start_y, width, height )
            draw.rectangle( pos, fill = back_color )
            draw.text( (xoffset + (width-twidth) / 2, start_y), text,font=font)
            
        return im

