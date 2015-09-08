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
    def __init__( self, argDefaultValue, argNRows, argNColumns ):
        print( "  Matrix constructor" )
        self.matrix = [ [ argDefaultValue for x in range( argNColumns ) ] for y in range( argNRows ) ]
        print( "    Creating matrix with {0} rows and {1} columns".format( len( self.matrix ), len( self.matrix[ 0 ] ) ) )
    
    def GetValue( self, argRowIndex, argColumnIndex ):
        return self.matrix[ argRowIndex ][ argColumnIndex ]
    
    def SetValue( self, argRowIndex, argColumnIndex, argValue ):
        self.matrix[ argRowIndex ][ argColumnIndex ] = argValue

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4