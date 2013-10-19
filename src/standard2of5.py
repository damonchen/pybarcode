#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode standard2of5
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from barcode_common import check_numeric_only


s25_code_table = (
"11101010101110", "10111010101110", "11101110101010", 
"10101110101110", "11101011101010", "10111011101010", 
"10101011101110", "10101110111010", "11101010111010", 
"10111010111010"
)


class Standard2of5(Barcode):
    def encode_barcode(self,text):
 
        if not check_numeric_only(text):
            raise BarcodeException("ES25-1: Numeric Data Only")
        
        result = []
        result.append( '11011010' )
        
        for value in text:
            result.append( s25_code_table[ int(value) ] ) 
        
        # add ending bars
        result.append("1101011")
        
        min_width = len(text) * len( s25_code_table[0] ) * 4
        return min_width, ''.join( result ) 
