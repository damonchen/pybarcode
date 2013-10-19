#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode 128
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
import Image, ImageDraw
from string import digits

code128_value_table = {
"0": "11011001100" ,
"1": "11001101100" ,
"2": "11001100110" ,
"3": "10010011000" ,
"4": "10010001100" ,
"5": "10001001100" ,
"6": "10011001000" ,
"7": "10011000100" ,
"8": "10001100100" ,
"9": "11001001000" ,
"10": "11001000100" ,
"11": "11000100100" ,
"12": "10110011100" ,
"13": "10011011100" ,
"14": "10011001110" ,
"15": "10111001100" ,
"16": "10011101100" ,
"17": "10011100110" ,
"18": "11001110010" ,
"19": "11001011100" ,
"20": "11001001110" ,
"21": "11011100100" ,
"22": "11001110100" ,
"23": "11101101110" ,
"24": "11101001100" ,
"25": "11100101100" ,
"26": "11100100110" ,
"27": "11101100100" ,
"28": "11100110100" ,
"29": "11100110010" ,
"30": "11011011000" ,
"31": "11011000110" ,
"32": "11000110110" ,
"33": "10100011000" ,
"34": "10001011000" ,
"35": "10001000110" ,
"36": "10110001000" ,
"37": "10001101000" ,
"38": "10001100010" ,
"39": "11010001000" ,
"40": "11000101000" ,
"41": "11000100010" ,
"42": "10110111000" ,
"43": "10110001110" ,
"44": "10001101110" ,
"45": "10111011000" ,
"46": "10111000110" ,
"47": "10001110110" ,
"48": "11101110110" ,
"49": "11010001110" ,
"50": "11000101110" ,
"51": "11011101000" ,
"52": "11011100010" ,
"53": "11011101110" ,
"54": "11101011000" ,
"55": "11101000110" ,
"56": "11100010110" ,
"57": "11101101000" ,
"58": "11101100010" ,
"59": "11100011010" ,
"60": "11101111010" ,
"61": "11001000010" ,
"62": "11110001010" ,
"63": "10100110000" ,
"64": "10100001100" ,
"65": "10010110000" ,
"66": "10010000110" ,
"67": "10000101100" ,
"68": "10000100110" ,
"69": "10110010000" ,
"70": "10110000100" ,
"71": "10011010000" ,
"72": "10011000010" ,
"73": "10000110100" ,
"74": "10000110010" ,
"75": "11000010010" ,
"76": "11001010000" ,
"77": "11110111010" ,
"78": "11000010100" ,
"79": "10001111010" ,
"80": "10100111100" ,
"81": "10010111100" ,
"82": "10010011110" ,
"83": "10111100100" ,
"84": "10011110100" ,
"85": "10011110010" ,
"86": "11110100100" ,
"87": "11110010100" ,
"88": "11110010010" ,
"89": "11011011110" ,
"90": "11011110110" ,
"91": "11110110110" ,
"92": "10101111000" ,
"93": "10100011110" ,
"94": "10001011110" ,
"95": "10111101000" ,
"96": "10111100010" ,
"97": "11110101000" ,
"98": "11110100010" ,
"99": "10111011110" ,
"100": "10111101110" ,
"101": "11101011110" ,
"102": "11110101110" ,
"103" : "11010000100" ,
"104" : "11010010000" ,
"105" : "11010011100" ,
"106" : "11000111010" 
}

code128_A_table = (
" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", 
"*","+", ",", "=", ".", "/", "0", "1", "2", "3", 
"4","5", "6", "7", "8", "9", ":", ";", "<", "=",
">", "?","@", "A", "B", "C", "D", "E", "F", "G",
"H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
"R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
"\\","]", "^", "_", "\0", chr(1), chr(2), chr(3), chr(4), chr(5),
chr(6), chr(7), chr(8), chr(9), chr(10),chr(11), chr(12), chr(13), chr(14), chr(15),
chr(16), chr(17), chr(18), chr(19), chr(20),chr(21), chr(22), chr(23), chr(24), chr(25),
chr(26), chr(27), chr(28), chr(29), chr(30),chr(31), chr(202), chr(201), "SHIFT", "CODE_C", 
"CODE_B", chr(203), chr(200), "START_A", "START_B", "START_C", "STOP"
)

code128_B_table = (
" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", 
"*","+", ",", "=", ".", "/", "0", "1", "2", "3", 
"4","5", "6", "7", "8", "9", ":", ";", "<", "=",
">", "?","@", "A", "B", "C", "D", "E", "F", "G",
"H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
"R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
"\\","]", "^", "_", "`", "a", "b", "c", "d", "e",
"f","g", "h", "i", "j", "k", "l", "m", "n", "o",
"p","q", "r", "s", "t", "u", "v", "w", "x", "y",
"z", "{", "|", "}", "~", chr(127), chr(202), chr(201),
"SHIFT", "CODE_C", chr(203), "CODE_A", chr(200), "START_A", "START_B", "START_C", "STOP"
)


code128_C_table = (
"00", "01", "02", "03", "04", "05", "06", "07", "08", "09", 
"10", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
"20", "21", "22", "23", "24", "25", "26", "27", "28", "29", 
"30", "31", "32", "33", "34", "35", "36", "37", "38", "39",  
"40", "41", "42", "43", "44", "45", "46", "47", "48", "49", 
"50", "51", "52", "53", "54", "55", "56", "57", "58", "59", 
"60", "61", "62", "63", "64", "65", "66", "67", "68", "69",
"70", "71", "72", "73", "74", "75", "76", "77", "78", "79", 
"80", "81", "82", "83", "84", "85", "86", "87", "88", "89", 
"90", "91", "92", "93", "94", "95", "96", "97", "98", "99", 
"CODE_B", "CODE_A", chr(200), "START_A", "START_B", "START_C", "STOP"
)

class TYPES(object):
    DYNAMIC = 0,
    A = 1,
    B = 2,
    C = 3
    
def int_sorted(list, comp=None):
    if comp is None:
        comp = lambda v1, v2: cmp( int(v1), int(v2) )
    return sorted( list, comp )

class Code128(Barcode):
    name = 'CODE-128'
    def __init__(self, type = TYPES.DYNAMIC):
        self.start_character = None
        self.formatted_data = []
        self.raw_data = []
        self.encoded_data = []
        self.type = type
        self.code_init()
        
    def code_init(self):
        self.code_a = {}
        for index,code_a in enumerate(code128_A_table):
            self.code_a[code_a] = str(index)
        
        self.code_b = {}
        for index, code_b in enumerate(code128_B_table):
            self.code_b[code_b] = str(index)
            
        self.code_c = {}
        for index, code_c in enumerate(code128_C_table):
            self.code_c[ code_c] = str(index)
        
    
    def encode_barcode(self,text):
        self.raw_data = text
        
        max_width = len(text) * len( code128_value_table['0'] ) * 2
        
        # break up data for encoding
        self.break_up_data_for_encoding()
        
        print self.formatted_data

        # insert the start characters
        self.insert_startand_code_characters()
        
        check_digit = self.calculate_check_digit()

        encoded_data = []

        for s in self.formatted_data:
            s = s.replace("'", "''")
            if self.type == TYPES.A:
                row = self.get_code_128_set( self.code_a[s] )
            elif self.type == TYPES.B:
                row = self.get_code_128_set( self.code_b[s] )
            elif self.type == TYPES.C:
                row = self.get_code_128_set( self.code_c[s] )
            elif self.type == TYPES.DYNAMIC:
                row = self.get_code_128_set( self.code_a.get(s,[]) )
                if len(row) <= 0:
                    row = self.get_code_128_set( self.code_b.get(s,[]) )
                if len(row) <= 0:
                    row = self.get_code_128_set( self.code_c.get(s,[]) )
            else:
                row = None
            
            if row is None or len( row ) <= 0:
                raise BarcodeException("EC128-5: Could not find encoding value( %s ) in C128 type" %self.type )
            print row[3]
            self.encoded_data.append( row[3] )
            
        #add the check digit
        self.encoded_data.append( self.calculate_check_digit() )

        # add the stop character
        self.encoded_data.append( code128_value_table[ self.code_a['STOP'] ] )

        # add the termination bars
        self.encoded_data.append('11')

        return max_width, ''.join(self.encoded_data)

    def calculate_check_digit(self):
        check_sum = 0
        for index,data in enumerate(self.formatted_data):
            s = data.replace("'", "''")
            print s,
            rows = self.code_a.get(s, None)
            if rows is None:
                rows = self.code_b.get(s, None)
            
            if rows is None:
                rows = self.code_c.get(s, None)
            print rows
            value = int( rows )
            if index == 0:
                addition = value
            else:
                addition = value * index
            check_sum += addition
        remainder = check_sum % 103
        print remainder
        return code128_value_table[ str(remainder) ]
    
    def break_up_data_for_encoding(self):
        temp_raw_data = self.raw_data
        if self.type == TYPES.A or self.type == TYPES.B:
            for c in self.raw_data:
                self.formatted_data.append( c )
            return 
        if self.type == TYPES.C:
            if not self.is_numeric( self.raw_data):
                raise BarcodeException("EC128-6: Only numeric values can be encoded with C128-C.")
            
            if len(self.raw_data) % 2 > 0:
                temp_raw_data = "0" + self.raw_data
                
        temp = ""
        for c in temp_raw_data:
            if c in digits:
                if temp == "":
                    temp += c
                else:
                    temp += c
                    self.formatted_data.append( temp )
                    temp = ""
            else:
                if temp != "":
                    self.formatted_data.append( temp )
                    temp = ""
                self.formatted_data.append( c )
        if temp != "":
            self.formatted_data.append( temp )
            temp = ""
            
    def insert_startand_code_characters(self):
        current_code_string = ""
        if self.type != TYPES.DYNAMIC:
            if self.type == TYPES.A:
                self.formatted_data.insert(0, 'START_A')
            elif self.type == TYPES.B:
                self.formatted_data.insert(0, 'START_B')
            elif self.type == TYPES.C:
                self.formatted_data.insert(0, 'START_C')
            else:
                raise BarcodeException('EC128-4: Unknown start type in fixed type encoding.')
        else:
            try:
                for index, data in enumerate( self.formatted_data ):
                    col, temp_start_chars = self.find_startor_code_character(data)
                    same_code_set = False
                    
                    for row in temp_start_chars:
                        if row[0].endswith( current_code_string ) or row[1].endswith( current_code_string ) or row[2].endswith( current_code_string ):
                            same_code_set = True
                            break
                        

                    if current_code_string == "" or not same_code_set:
                        current_code_set = temp_start_chars[0]

                        error = True
                        while error:
                            try:
                                current_code_string = current_code_set[col].split('_')[1]
                                error = False
                            except :
                                error = True
                                col += 1
                                if col > len(current_code_set):
                                    raise BarcodeException("No start character found in current code set.")
                        
                        self.formatted_data.insert(index, str(current_code_set[col]) )
            except Exception, e:
                raise BarcodeException("EC128-3: Could not insert start and code characters.\n Message: %s" %e.message )                
            
    def is_numeric(self, input):
        for c in input:
            if not c in digits:
                return False
        return True
    
    def get_code_128_set(self, index):
        set = []
        
        try:
            i = int(index)
            set.append( code128_A_table[i] )
            set.append( code128_B_table[i] )
            set.append( code128_C_table[i] )
            set.append( code128_value_table[index] )
        except Exception:
            set = []
                
        return set
        
    
    def find_startor_code_character(self,text):
        # if two chars are number then START_C or CODE_C    
        text_len = len(text)
        rows = []
        if text_len > 1 and text[0] in digits and text[1] in digits :
            if self.start_character is None:
                self.start_character = self.get_code_128_set( self.code_a['START_C']  )
                rows.append( self.start_character )
            else:
                rows.append( self.get_code_128_set( self.code_a['CODE_C']  ) )
                
            col = 1
        else:
            a_found = False
            b_found = False
            
            for index, row in enumerate(int_sorted(code128_value_table.keys())):
                try:
                    if not a_found and text == code128_A_table[index]:
                        a_found = True
                        col = 2
                        if self.start_character is None:
                            self.start_character = self.get_code_128_set( self.code_a['START_A'] )
                            rows.append( self.start_character )
                        else:
                            rows.append( self.get_code_128_set( self.code_b['CODE_A'] ) )
                    elif not b_found and text == code128_B_table[index]:
                        b_found = True
                        col = 1
                        
                        if self.start_character is None:
                            self.start_character = self.get_code_128_set( self.code_a['START_B']  )
                            rows.append( self.start_character )
                        else:
                            rows.append( self.get_code_128_set( self.code_a['CODE_B'] ) )
                    elif a_found and b_found:
                        break
                except Exception,e:
                    raise BarcodeException('EC128-1: %s' %e.message )
                
            if len(rows) <= 0:
                raise BarcodeException("EC128-2:Could not determine start character.")
        return col, rows
    
class Code128A(Code128):
    def __init__(self):
        Code128.__init__(self, TYPES.A )
        
class Code128B(Code128):
    def __init__(self):
        Code128.__init__(self, TYPES.B )

class Code128C(Code128):
    def __init__(self):
        Code128.__init__(self, TYPES.C )

def main():
    code128 = Code128()
    im = code128.make_barcode('1234', 350, 150, show_text = True )
    im.save("barcode-128.bmp", 'BMP')
    
if __name__ == '__main__':
    main()
