#-*- coding: utf-8 -*-
import re
def html_filter (html):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html)
    return dd
