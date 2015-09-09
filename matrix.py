##############################################################################
##
## Copyright 2015 Markus Prasser
##
## This file is part of PrSi.
##
##  PrSi is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  PrSi is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with PrSi.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

class Matrix:
    def __init__( self, argMatrix ):
        # print( "Matrix constructor" )
        self.matrix = argMatrix
    
    def __repr__( self ):
        stringRepr = '['
        for row in self.matrix:
            stringRepr = stringRepr + str( row ) + ','
        stringRepr = stringRepr.rstrip( ',' )
        stringRepr = stringRepr + ']'
        return stringRepr
    
    def __str__( self ):
        stringRepr = str()
        for row in self.matrix:
            stringRepr = stringRepr + str( row ) + '\n'
        stringRepr = stringRepr.rstrip()
        return stringRepr
    
    @classmethod
    def FromParameters( cls, argDefaultValue, argNRows, argNColumns ):
        # print( "Creating matrix with {0} rows and {1} columns".format( argNRows, argNColumns ) )
        return cls( [ [ argDefaultValue for x in range( argNColumns ) ] for y in range( argNRows ) ] )
    
    def GetMinimumValue( self ):
        mins = [ ( min( row ), row.index( min( row ) ) ) for row in self.matrix ]
        # print( mins )
        sortedMins = sorted( mins, key = lambda item: item[ 0 ] )
        # print( sortedMins )
        return ( sortedMins[ 0 ][ 0 ], mins.index( sortedMins[ 0 ] ), sortedMins[ 0 ][ 1 ] )
    
    def GetValue( self, argRowIndex, argColumnIndex ):
        return self.matrix[ argRowIndex ][ argColumnIndex ]
    
    def SetValue( self, argRowIndex, argColumnIndex, argValue ):
        self.matrix[ argRowIndex ][ argColumnIndex ] = argValue

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4