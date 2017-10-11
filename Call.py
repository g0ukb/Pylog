#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'brian'

class Call:
    def __init__(self,callsign):
        self.callsign=callsign.upper()



call=Call("g0ukb")
print (call.callsign)