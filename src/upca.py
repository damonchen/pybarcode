#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode upca
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from barcode_common import check_numeric_only,get_country_codes

upc_codeA_table = ( 
"0001101", "0011001", "0010011", "0111101", "0100011", 
"0110001", "0101111", "0111011", "0110111", "0001011" )

upc_codeB_table = (
"1110010", "1100110", "1101100", "1000010", "1011100", 
"1001110", "1010000", "1000100", "1001000", "1110100"
)

class UPCA(Barcode):
    
    name = 'UPCA'
    
    def checksum_digit(self):
        try:
            raw_data_holder = self.raw_data
            
            even = 0
            odd = 0
            for index, value in enumerate(raw_data_holder):
                if index % 2 == 0:
                    odd += int( value ) * 3
                else:
                    even += int( value )
            total = even + odd
            checksum = total % 10
            checksum = 10 - checksum
            if checksum == 10:
                checksum = 0
            
            self.raw_data = raw_data_holder + str(checksum)[0]
        except:
            raise BarcodeException("EUPCA-4: Error calculating check digit.")
    
    def encode_barcode(self, text):
        if len(text) != 11 or len(text) != 12:
            raise BarcodeException("EUPCA-1: Data length invalid. (Length must be 11 or 12)")
        
        if not check_numeric_only(text):
            raise BarcodeException("EUPCA-2: Numeric Data Only")
        
        self.raw_data = text
        
        result = []
        result.append("101") # start with guard bars
        
        # first number
        result.append( upc_codeA_table[ int(self.raw_data[0]) ] )
        
        # second (group) of numbers
        for i in range(1,6):
            result.append( upc_codeA_table[ int(self.raw_data[i]) ] )
        
        # add divider bars
        result.append( '01010' )
        
        # third (group) of numbers
        for i in range(6,11):
            result.append( upc_codeB_table[ int(self.raw_data[i]) ] ) 
            
        # fouth 
        result.append( upc_codeB_table[ int(self.raw_data[-1]) ] )
        
        # add ending guard bars
        result.append('101')
        
        # get the manufacturer assigning country
        country_code = get_country_codes()
        two_digit_code = "0" + self.raw_data[0]
        try:
            self.country_assigning_manufacturer_code = country_code[two_digit_code]
        except:
            raise BarcodeException("EUPCA-3: Country assigning manufacturer code not found.")
        
        min_width = len(self.raw_data) * len(upc_codeA_table[0]) * 2
        return min_width, ''.join(result)
        
        
        
