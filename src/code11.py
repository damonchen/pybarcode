#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode code11
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from barcode_common import check_numeric_only

c11_code_table = (
 "101011", "1101011", "1001011", "1100101", "1011011", 
"1101101", "1001101", "1010011", "1101001", "110101", 
"101101", "1011001" 
)


class Code11(Barcode):
    
    name = 'CODE-11'
    
    def _checksum(self, text):
        weight = 1
        total = 0
        
        data_to_encode_with_chechsum = list(text)
        
        # figure the c checksum
        for value in text[::-1]:
            # c checksum weights go 1-10
            if weight == 10:
                weight = 1
            
            if value != '-':
                total += int( value ) * weight
            else:
                total += 10 * weight
            weight += 1
        checksum = total % 11
        
        data_to_encode_with_chechsum.append( str( checksum ) )
        
        # k checksums are recommended on any message length greater than or equal to 10
        if len( text) >= 1:
            weight = 1
            k_total = 0
            
            # calculate k checksum
            for value in data_to_encode_with_chechsum[::-1]:
                # k checksum weight go 1-9
                if weight == 9:
                    weight = 1
                
                if value != '-':
                    k_total += int( value ) * weight
                else:
                    k_total += 10 * weight
            data_to_encode_with_chechsum.append( str(k_total) )
        return ''.join( data_to_encode_with_chechsum )
    
    def encode_barcode(self,text):
        if not check_numeric_only( text.replace('-',"") ):
            raise BarcodeException("EC11-1: Numeric data and '-' Only")
        
        # calculate the chechsums
        data_to_encode_with_chechsum = self._checksum(text)
        
        # encode data
        space = '0'
        result = []
        result.append( c11_code_table[11] )
        result.append( space )
        
        for c in data_to_encode_with_chechsum:
            if c == '-':
                index = 10
            else:
                index = int( c )
                
            result.append( c11_code_table[ index ] )
            result.append( space )
            
        result.append( c11_code_table[11] )
        
        min_width = len(text) * len( c11_code_table[0] ) * 2
        return min_width, ''.join(result)
        
