#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode 93
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog

from barcode import Barcode, BarcodeException
from barcode_common import check_numeric_only

c93_code_table = (
# character, value, encoding
("0", "0", "100010100" ),
("1", "1", "101001000" ),
("2", "2", "101000100" ),
("3", "3", "101000010" ),
("4",  "4", "100101000" ),
("5",  "5", "100100100" ),
("6",  "6", "100100010" ),
("7",  "7", "101010000" ),
("8",  "8", "100010010" ),
("9",  "9", "100001010" ),
("10", "A", "110101000" ),
("11", "B", "110100100" ),
("12", "C", "110100010" ),
("13", "D", "110010100" ),
("14", "E", "110010010" ),
("15", "F", "110001010" ),
("16", "G", "101101000" ),
("17", "H", "101100100" ),
("18", "I", "101100010" ),
("19", "J", "100110100" ),
("20", "K", "100011010" ),
("21", "L", "101011000" ),
("22", "M", "101001100" ),
("23", "N", "101000110" ),
("24", "O", "100101100" ),
("25", "P", "100010110" ),
("26", "Q", "110110100" ),
("27", "R", "110110010" ),
("28", "S", "110101100" ),
("29", "T", "110100110" ),
("30", "U", "110010110" ),
("31", "V", "110011010" ),
("32", "W", "101101100" ),
("33", "X", "101100110" ),
("34", "Y", "100110110" ),
("35", "Z", "100111010" ),
("36", "-", "100101110" ),
("37", ".", "111010100" ),
("38", " ", "111010010" ),
("39", "$", "111001010" ),
("40", "/", "101101110" ),
("41", "+", "101110110" ),
("42", "%", "110101110" ),
("43", "(", "110101110" ), #dont know what character actually goes here
("44", ")", "110101110" ), #dont know what character actually goes here
("45", "#", "110101110" ), #dont know what character actually goes here
("46", "@", "110101110" ), #dont know what character actually goes here
("-",  "*", "101011110" ),
)


class Code93(Barcode):
    
    name = 'CODE-11'
    
    def get_code_from_character(self, character):
        for code in c93_code_table:
            if code[0] == character:
                return code
                
    
    def get_code_from_value(self, value):
        for code in c93_code_table:
            if code[1] == value:
                return code
    
    def check_digits(self, text):
        ary_weight = [ 0 for i in text ]

        cur_weight = 1
        for i in range(len(text)-1, -1, -1):
            if cur_weight > 20:
                cur_weight = 1
            ary_weight[ i ] = cur_weight
            cur_weight += 1
        
        
        # populate the k weight
        ary_k_weight = [ 0 for i in text ]
        ary_k_weight.append( 0 )
        cur_weight = 1
        for i in range(len(text)-1, -1, -1):
            if cur_weight > 15:
                cur_weight = 1
            ary_k_weight[i] = cur_weight
            cur_weight += 1
        
        # calculate c checksum
        check_sum = []
        print ary_weight, 
        for index, weight in enumerate(ary_weight):
            check_sum.append( weight * int(self.get_code_from_character(text[i])[0]) ) 

        check_sum_value = sum(check_sum) % 47
        
        text += self.get_code_from_value( str(check_sum_value) )[0]
        
        # calculate k checksum
        check_sum = []
        for index, weight in enumerate(ary_k_weight):
            check_sum.append( weight * int(self.get_code_from_character(text[i])[0]) ) 
        check_sum_value = sum(check_sum) % 47
        
        text += self.get_code_from_value( str(check_sum_value) )[0]
        
    def encode_barcode(self,text):
        formatted_data = self.check_digits( text )
        
        result = []
        result.append( self.get_code_from_character("*")[2] )
        
        for c in formatted_data:
            try:
                result.append( self.get_code_from_character(c)[2] )
            except:
                raise BarcodeException("EC93-1: Invalid data.")
        
        result.append( self.get_code_from_character("*")[2] )
        result.append("1")
        
        return result        
            

def main():
    code93 = Code93()
    im = code93.make_barcode('12345', 350, 150, show_text = True )
    im.save("barcode-93.bmp", 'BMP')
    
if __name__ == '__main__':
    main()
