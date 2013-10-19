#! /usr/bin/env python
#coding=utf-8

# author: ubunoon
# date : 2011-1-27
# email: netubu@gmail.com
# project: base implement
# Copyright (C) 2010, 2011 Qiantangren Stduio
# homepage: http://www.qtrstudio.com
# blog: http://www.cnblogs.com/ubunoon  or http://www.qtrstudio.com/blog

from code39 import Code39
from code128 import Code128
from ean8 import Ean8
from ean13 import Ean13
from isbn import ISBN
from barcode import BarcodeException

# author information
__version__ = "0.0.1a"
__author__ = "Damon"
__date__ = "2010-12-2"
__homepage__ = "http://qtrstudio.com/blog"
__blog__ = "http://www.cnblogs.com/ubunoon/"
__mail__ = "netubu@gmail.com"

# support list
__dict__ = ["Code39", "Code128", "Ean3", "Ean13", "ISBN"]


__code_type__ = {
"code39": Code39,
"code128": Code128,
"ean8": Ean8,
"ean13" : Ean13,
}

def get_barcode_class(code_type):
    code_class = __code_type__.get(code_type, None)
    if code_class is None:
        raise BarcodeException("not found the barcode type %s" %code_type)
    return code_class
    
    
