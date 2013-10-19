#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode 39
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog

from barcode import Barcode

code39_table = {
'0': "101001101101",
'1': "110100101011",
'2': "101100101011",
'3': "110110010101",
'4': "101001101011",
'5': "110100110101",
'6': "101100110101",
'7': "101001011011",
'8': "110100101101",
'9': "101100101101",
'A': "110101001011",
'B': "101101001011",
'C': "110110100101",
'D': "101011001011",
'E': "110101100101",
'F': "101101100101",
'G': "101010011011",
'H': "110101001101",
'I': "101101001101",
'J': "101011001101",
'K': "110101010011",
'L': "101101010011",
'M': "110110101001",
'N': "101011010011",
'O': "110101101001",
'P': "101101101001",
'Q': "101010110011",
'R': "110101011001",
'S': "101101011001",
'T': "101011011001",
'U': "110010101011",
'V': "100110101011",
'W': "110011010101",
'X': "100101101011",
'Y': "110010110101",
'Z': "100110110101",
'-': "100101011011",
'.': "110010101101",
' ': "100110101101",
'$': "100100100101",
'/': "100100101001",
'+': "100101001001",
'%': "101001001001",
'*': "100101101101",
}

class Code39(Barcode):
    name = 'CODE-39'
    def encode_barcode(self, text):
        text = '*%s*' %text.replace('*', "")
        text = text.upper()
        result = []
        for c in text:
            result.append(code39_table[c])
        value = '0'.join(result)
        
        max_width = len(text) * len(code39_table['0']) * 2
        
        
        print value
        
        return max_width, value
    

def main():
    code39 = Code39()
    data = raw_input(u"请输入条形码值：".encode("gbk"))
    width = int(raw_input(u"条形码宽度：".encode("gbk")))
    height = int(raw_input(u"条形码高度:".encode("gbk")))
    im = code39.make_barcode('encode', width, height )
    im.save("barcode.bmp", 'BMP')
    
if __name__ == '__main__':
    main()
    

        
        
