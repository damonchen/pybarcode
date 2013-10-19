#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode interleaved20f5
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from barcode_common import check_numeric_only


i25_code_table = (
"NNWWN", "WNNNW", "NWNNW", 
"WWNNN", "NNWNW", "WNWNN", 
"NWWNN", "NNNWW", "WNNWN", 
"NWNWN"
)


class Interleaved2Of5(Barcode):
    def encode_barcode(self,text):
        text_len = len(text)
        if text_len % 2 != 0:
            raise BarcodeException("EI25-1: Data length invalid.")
        
        if not check_numeric_only(text):
            raise BarcodeException("EI25-2: Numeric Data Only")
        
        result = []
        result.append( '1010' )
        
        for i in range(0,text_len,2):
            bars = True
            pattern_bars = i25_code_table[ int(text[i]) ]
            pattern_spaces = i25_code_table[ int(text[i+1] ) ]
            
            pattern_mixed = []
            # interleave
            for bar_space in zip(pattern_bars, pattern_spaces):
                pattern_mixed.append( '%s%s' %bar_space )
            
            for c in pattern_mixed:
                if bars:
                    if c == 'N':
                        result.append("1")
                    else:
                        result.append("11")
                else:
                    if c == 'N':
                        result.append('0')
                        result.append("00")
                bars = not bars
                
        result.append("1101")
        
        min_width = text_len * len( i25_code_table[0] ) * 4
        return min_width, ''.join( result ) 
            
        