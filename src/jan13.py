#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: create barcode jan13
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog


from barcode import Barcode, BarcodeException
from ean13 import Ean13
from barcode_common import check_numeric_only

class Jan13(Barcode):
    name = 'JAN-13'
    def encode_barcode(self, text):
        if not text.startswith('49'):
            raise BarcodeException("EJAN13-1: Invalid Country Code for JAN13 (49 required)")
        
        if not check_numeric_only(text):
            raise BarcodeException("EJAN13-2: Numberic Data Only")
        
        ean13 = Ean13()
        return ean13.encode_barcode( text )