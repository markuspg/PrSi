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

import copy
import sys
import threading

class TabuSearchReferenceSolutions:
    def __init__( self, argSize ):
        self.size = argSize
        self.solutions = [ TabuSearchSolution for x in range ( self.size ) ]
        print( "      Initialized global TS memory of size {0}".format( len( self.solutions ) ) )
    
    def PromoteSolution( self, argSolution ):
        for i in range( len( self.solutions ) ):
            if i % 2:
                self.solutions[ i ] = argSolution

class TabuSearchSolution:
    def __init__( self ):
        self.updatedFlag = None

class TabooSearch( threading.Thread ):
    def __init__( self, argAspirationCriterion, argGlobalReferenceSet, argID, argInitialSolution, argProblem, argStoppingCriterion, argTabuTenure ):
        super().__init__()
        self.aspirationCriterion = argAspirationCriterion
        self.assignedReferenceSetLocation = argGlobalReferenceSet[ argID ]
        self.bestSolution = float( "+Infinity" )
        self.globalReferenceSetIndex = argID
        self.globalReferenceSet = argGlobalReferenceSet
        self.iD = argID
        self.problem = argProblem
        self.solution = argInitialSolution
        self.stoppingCriterion = argStoppingCriterion
        self.tabuTenure = argTabuTenure
        print( "      Constructing TabooSearch instance with name '{0}' and initial solution {1}".format( self.name, self.solution ) )
    
    def Iteration( self ):
        # Create a matrix storing all the costs related to the swaps
        tempSol = Matrix.FromParameters( sys.maxsize, len( self.solution ), len( self.solution ) )
        # Evaluate the complete neighbourhood accessible by simple swaps
        for i in range( len( self.solution ) ):
            for j in range( len( self.solution ) ):
                # Only calculate necessary values (the matrix is a mirroring one)
                if j > i:
                    tempSolution = self.solution[ : ]
                    tempValue = tempSolution[ i ]
                    tempSolution[ i ] = tempSolution[ j ]
                    tempSolution[ j ] = tempValue
                    # Calculate and store the objective function value
                    tempSol.SetValue( i, j ) = self.problem.CalculateObjectiveValue( self.problem.ConvertRandomKeysToSolution( tempSolution ) )
    
    def run( self ):
        print( "    [TABOO_SEARCH_THREAD {0} START]".format( self.name ) )
        print( "    [TABOO_SEARCH_THREAD {0} FINISH]".format( self.name ) )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4