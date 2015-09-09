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

from matrix import Matrix

class Builder:
    def __init__( self, argProblemString, argProblemType ):
        # First load data common to all problems
        print( "  Builder constructor" )
        self.problemItems = argProblemString.rstrip( '\n' ).split( '|' )
        # print( self.problemItems )
        self.problemName = self.problemItems[0].rpartition( '/' )[ -1 ]
        self.problemType = argProblemType
        print( "    Building {0}-problem: {1}".format( self.problemType, self.problemName ) )
        
        # Then load problem specific data or fail, if an unknown problem was given
        if self.problemType == "QAP":
            assert len( self.problemItems ) == 4
            self.problemSize = int( self.problemItems[ 1 ] )
            self.flowMatrix = Matrix.FromSSV( self.problemItems[ 2 ], self.problemSize, self.problemSize )
            # print( self.flowMatrix )
            self.distanceMatrix = Matrix.FromSSV( self.problemItems[ 3 ], self.problemSize, self.problemSize )
            # print( self.distanceMatrix )
        else:
            raise ValueError( "Invalid problem type encountered in 'Builder'" )
        print( "      Problem size: {0}".format( self.problemSize ) )
    
    def LoadMatrix( self, argList, argXSize, argYSize ):
        matrixItems = argList.split( ';' )
        assert len( matrixItems ) == argXSize * argYSize
        matrix = list()
        for i in range( argXSize ):
            matrix.append( [ int( x ) for x in matrixItems[ i * argXSize : ( i * argXSize ) + argXSize ] ] )
        return matrix

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4