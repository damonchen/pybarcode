#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode ean13
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from barcode_common import check_numeric_only, get_country_codes

ean_codeA_table = (
"0001101", "0011001", "0010011", "0111101", "0100011", 
"0110001", "0101111", "0111011", "0110111", "0001011")

ean_codeB_table = (
"0100111", "0110011", "0011011", "0100001", "0011101", 
"0111001", "0000101", "0010001", "0001001", "0010111"
)

ean_codeC_table = (
"1110010", "1100110", "1101100", "1000010", "1011100", 
"1001110", "1010000", "1000100", "1001000", "1110100")

ean_pattern = (
"aaaaaa", "aababb", "aabbab", "aabbba", "abaabb", 
"abbaab", "abbbaa", "ababab", "ababba", "abbaba"
)


class Ean13(Barcode):
    
    name = 'EAN-13'
    
    def encode_barcode(self,text):
        self.raw_data = self.check_digit(text)
        
        if len(self.raw_data) < 12 or len( self.raw_data) > 13:
            raise BarcodeException("EEAN13-1: Data length invalid.(Length must be 12 or 13)")
        
        if not check_numeric_only( self.raw_data ):
            raise BarcodeException("EEAN13-2: Numberic Data Only.")
        
        pattern_code = ean_pattern[ int( self.raw_data[0] ) ]
        result = []
        result.append( '101' )
        for pos in range(6):
            if pattern_code[pos] == 'a':
                result.append( ean_codeA_table[ int(self.raw_data[pos+1]) ])
            if pattern_code[pos] == 'b':
                result.append( ean_codeB_table[ int(self.raw_data[pos+1]) ])
        
        # add divider bars
        result.append('01010')
        for pos in range(1,6):
            result.append( ean_codeC_table[ int( self.raw_data[pos+6] ) ] )
        
        # checksum digit
        cs = int( self.raw_data[-1] )
        
        # add checksum
        result.append( ean_codeC_table[cs] )
        
        # add ending bars
        result.append( '101' )
        
        country_codes = get_country_codes()
        
        self.country_assigning_manufacturer_code = "N/A"
        two_digit_code = self.raw_data[0:2]
        three_digit_code = self.raw_data[0:3]
        try:
            self.country_assigning_manufacturer_code = country_codes[ three_digit_code ]
        except Exception:
            try:
                self.country_assigning_manufacturer_code = country_codes[ two_digit_code ]
            except:
                raise BarcodeException("EEAN13-3: Country assigning manufacturer code not found.")
        finally:
            country_codes
        
        min_width = len( self.raw_data ) * len( ean_codeA_table[0] ) * 2
                
        return min_width,''.join(result)
    
    
        
    def check_digit(self,text):
        try:
            raw_data_holder = text[0:12]
            
            even = 0
            odd = 0
            
            for i in range(len(raw_data_holder)):
                if i % 2 == 0:
                    odd += int( raw_data_holder[i] )
                else:
                    even += int( raw_data_holder[i] ) * 3
            
            total = even + odd 
            cs = total % 10
            cs = 10 - cs
            if cs == 10:
                cs = 0
            text = raw_data_holder + str(cs)[0]
            return text
        except Exception:
            raise BarcodeException("EEAN13-4: Error calculating check digit.")

def main():
    ean13 = Ean13()
    im = ean13.make_barcode('123456789012', 350, 150 )
    im.save("barcode-ean13.bmp", 'BMP')
    
if __name__ == '__main__':
    main()

