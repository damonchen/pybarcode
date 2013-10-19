#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode isbn
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from ean13 import Ean13
from barcode_common import check_numeric_only


class ISBN(Barcode):
    
    name = 'ISBN'
    
    def encode_barcode(self,text):
        self.raw_data = text
        
        if not check_numeric_only(self.raw_data):
            raise BarcodeException("EBOOKLANDISBN-1: Numberic Data Only")
        
        type = "UNKNOWN"
        value = list( self.raw_data )

        if len(self.raw_data) == 10 or len( self.raw_data ) == 9:
            if len( self.raw_data ) == 10:
                value = value[:9] + value[10:]
            value.insert(0, '978')
            type = 'ISBN'
            ISBN.name = 'ISBN-10'
        elif len( self.raw_data ) == 12 and self.raw_data.startswith('978'):
            type = 'BOOKLAND-NOCHECKDIGIT'
            ISBN.name = 'ISBN-13'
        elif len( self.raw_data ) == 13  and self.raw_data.startswith('978'):
            type = 'BOOKLAND-CHECKDIGTI'
            value = value[:12] + value[13:]
            ISBN.name = 'ISBN-13'

        if type == 'UNKNOWN':
            raise BarcodeException("EBOOKLANDISBN-2: Invalid input.  Must start with 978 and be length must be 9, 10, 12, 13 characters.")
        
        ean13 = Ean13()
        
        return ean13.encode_barcode( ''.join( value ) )
        
def main():
    isbn = ISBN()
    im = isbn.make_barcode('1234567890', 350, 150 )
    im.save("barcode-isbn.bmp", 'BMP')
    
if __name__ == '__main__':
    main()

    
    