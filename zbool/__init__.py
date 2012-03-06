#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A boolean object supporting Ternary logic aka undefined"""


class ZBool():
    def __init__(self,value):
        self._value = value
    def __set__(self, *a):
        print "%s" % a

    
    def __and__(self, other):
        _all = (self._value, other._value)
        if any( x is None for x in _all ):
            if all( x is None for x in _all ):
                return ZBool(None)
            else:
                if any( x is False for x in _all ):
                    return ZBool(False)
            return ZBool(None)

        return ZBool(self._value  & other._value)
    
    
    def __or__(self, other):
        _all = (self._value, other._value)
        if any( x is None for x in _all ):
            
            if any( x is True for x in _all ):
                return ZBool(True)

            return ZBool(None)

        return ZBool(self._value | other._value)
    


    def __not__(self):
        if self._value is None:
            return ZBool(None)
        return ZBool( self._value == False )

    def __str__(self):
        return "undef" if self._value is None else str(self._value)
if '__main__' == __name__:
    all_case =[ x for x in map( ZBool, ( True, False, None)) ]

    operation = dict( 
        OR = lambda x, y: x |y,
        AND = lambda x,y: x&y,
        XOR = lambda x, y : (x.__not__() & y) | ( y.__not__() & x ),
    )

    print "TESTING OPERATION NOT" 
    print "-" * 16
    print "\n".join( "%s\t|%s"%( str(y),str(y.__not__())) for y in all_case )
    


    for name, func in operation.items():
        print "*" * 40
        print "TESTING OPERATION %s" % name 

        print "\t%s" % "\t|".join(  str(x)  for x in all_case)
        for x in all_case:
            print "-" * 30
            print "%s\t|%s" % ( x, "\t|".join( str(func(x,y)) for y in all_case ))

