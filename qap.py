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
        return sum( [ self.distanceMatrix[ int( argSolution[ i ] ) - 1][ i ] * self.flowMatrix[ int( argSolution[ i ] ) - 1][ i ] for i in range( len( argSolution ) ) ] )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4