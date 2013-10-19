#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode ean8
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from string import digits
from barcode_common import check_numeric_only

ean_codeA_table = (
"0001101", "0011001", "0010011", "0111101", "0100011", 
"0110001", "0101111", "0111011", "0110111", "0001011")

ean_codeC_table = (
"1110010", "1100110", "1101100", "1000010", "1011100", 
"1001110", "1010000", "1000100", "1001000", "1110100")


class Ean8(Barcode):
    
    name = 'EAN-8'
    
    def encode_barcode(self,text):
        self.raw_data = text
        self.check_digit()
        
        if len( self.raw_data ) != 8 and len( self.raw_data ) != 7:
            raise BarcodeException("EEAN8-1: Invalid data length. (7 or 8 numbers only)")
        
        # check numeric only
        if not check_numeric_only( self.raw_data ):
            raise BarcodeException("EEAN8-2: Numberic only.")
        
        # encode the data
        result = []
        result.append( '101' )
        
        for i in range( len(self.raw_data) / 2 ):
            result.append( ean_codeA_table[ int(self.raw_data[i] ) ] )
        
        # center guard bars
        result.append( '01010')
        
        # second half (encoded using right hand / even parity)
        for i in range( len(self.raw_data) / 2, len(self.raw_data) ):
            result.append( ean_codeC_table[ int(self.raw_data[i]) ] )
            
        result.append('101')
        
        min_width = len( self.raw_data ) * len( ean_codeA_table[0] ) * 2
        
        return min_width, ''.join(result)
    
    def check_digit(self):
        # calculate the checksum digit if necessary
        if len(self.raw_data) == 7:
            # calculate the chechsum digit
            even = 0
            odd = 0
            
            for i in range(0,7,2):
                odd += int(self.raw_data[i])*3
            
            for i in range(1,6,2):
                even += int( self.raw_data[i])
            
            total = even + odd
            chechsum = total % 10
            chechsum = 10 - chechsum
            if chechsum == 10:
                chechsum = 0
            self.raw_data += str( chechsum )
            
        
def main():
    ean8 = Ean8()
    im = ean8.make_barcode('1234567', 350, 150 )
    im.save("barcode-ean8.bmp", 'BMP')
    
if __name__ == '__main__':
    main()
