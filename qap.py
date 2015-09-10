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

import os
import random

class QAP:
    def __init__( self, argBuilder ):
        print( "  QAP constructor" )
        self.problemName = argBuilder.problemName
        self.problemSize = argBuilder.problemSize
        # The matrices' rows represent the plants, the columns represent the locations
        self.distanceMatrix = argBuilder.distanceMatrix
        self.flowMatrix = argBuilder.flowMatrix
        print( "    Creating QAP '{0}' of size {1}".format( self.problemName, self.problemSize ) )
    
    def CalculateObjectiveValue( self, argSolution ):
        assert len( argSolution ) == self.problemSize, "The passed solution vector is of improper size"
        
        # argSolution[ i ] - 1 is the plant, i is the location
        return sum( [ self.distanceMatrix.GetValue( int( argSolution[ i ] ) - 1, i ) * self.flowMatrix.GetValue( int( argSolution[ i ] ) - 1, i ) for i in range( len( argSolution ) ) ] )
    
    def ConvertRandomKeysToSolution( self, argRandomKeys ):
        assert len( argRandomKeys ) == self.problemSize, "The random keys vector is of improper size and would not yield a valid solution"
        
        # Create the new solution vector
        solution = [ None ] * len( argRandomKeys )
        
        # Check solution vector length's-times for the smallest element
        for index in range( len( argRandomKeys ) ):
            # Add the real index of the smallest element to the solution vector
            solution[ argRandomKeys.index( min( argRandomKeys ) ) ] = index + 1
            # Make the smallest element really big, so it is not brought into consideration anymore
            argRandomKeys[ argRandomKeys.index( min( argRandomKeys ) ) ] = float( "+Infinity" )
        
        return solution
    
    def CreateRandomRandomKeys( self ):
        random.seed( os.urandom( 20 ) )
        
        # Create the new solution vector
        solution = [ random.random() for i in range( self.problemSize ) ]
        
        return solution

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4