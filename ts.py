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
        self.assignedReferenceSetLocation = argGlobalReferenceSet.solutions[ argID - 1 ]
        self.bestSolution = float( "+Infinity" )
        self.globalReferenceSetIndex = argID - 1
        self.globalReferenceSet = argGlobalReferenceSet
        self.iD = argID
        self.iterationCount = 0
        self.maxFailures = 5
        self.problem = argProblem
        self.solution = argInitialSolution
        self.stoppingCriterion = argStoppingCriterion
        self.tabuDurations = Matrix.FromParameters( 0, len( self.solution ), len( self.solution ) )
        self.tabuTenure = argTabuTenure
        print( "      Constructing TabooSearch instance with name '{0}' and initial solution {1}".format( self.name, self.solution ) )
    
    def Iteration( self ):
        self.iterationCount = self.iterationCount + 1
        print( "        Iteration {0}".format( self.iterationCount ) )
        # Create a matrix storing all the costs related to the swaps
        tempSol = Matrix.FromParameters( sys.maxsize, len( self.solution ), len( self.solution ) )
        # Evaluate the complete neighbourhood accessible by simple swaps
        for i in range( len( self.solution ) ):
            for j in range( len( self.solution ) ):
                # Only calculate necessary values (the matrix is a mirroring one)
                if j > i:
                    print( self.solution )
                    tempSolution = self.solution[ : ]
                    tempValue = tempSolution[ i ]
                    tempSolution[ i ] = tempSolution[ j ]
                    tempSolution[ j ] = tempValue
                    print( tempSolution )
                    # Calculate and store the objective function value
                    tempSol.SetValue( i, j, self.problem.CalculateObjectiveValue( self.problem.ConvertRandomKeysToSolution( tempSolution ) ) )
        
        bestSwap = tempSol.GetMinimumValue()
        # Find the best possible move
        while True:
            # Check if the best swap yields an improvement at all
            if bestSwap[ 0 ] >= self.bestSolution:
                break
            
            # Check, if the swap is allowed concerning the taboo duration
            if self.tabuDurations.GetValue( bestSwap[ 1 ], bestSwap[ 2 ] ) >= self.iterationCount:
                tempSol.SetValue( bestSwap[ 1 ], bestSwap[ 2 ], sys.maxsize )
                tempSol.SetValue( bestSwap[ 2 ], bestSwap[ 1 ], sys.maxsize )
                bestSwap = tempSol.GetMinimumValue()
                continue
            
            # Break, if a best possible swap was found
            break
        
        # Return the swap found in this iteration
        return bestSwap
    
    def run( self ):
        print( "    [TABOO_SEARCH_THREAD {0} START]".format( self.name ) )
        numFailures = 0
        lastIterationValue = sys.maxsize
        while numFailures <= self.maxFailures:
            suggestedSwap = self.Iteration()
            if lastIterationValue <= suggestedSwap[ 0 ]:
                numFailures = numFailures + 1
                # Check this behaviour later!!!
                continue
            Swap( suggestedSwap[ 1 ], suggestedSwap[ 2 ] )
            lastIterationValue = suggestedSwap[ 0 ]
        print( "    [TABOO_SEARCH_THREAD {0} FINISH]".format( self.name ) )
    
    def Swap( self, argI, argJ ):
        # Do the swap
        tempValue = self.solution[ argI ]
        self.solution[ argI ] = self.solution[ argJ ]
        self.solution[ argJ ] = tempValue
        
        # Set the taboo durations
        randomizedTabooDuration = self.iterationCount + random.randint( int( 0.9 * self.tabuTenure ), int( 1.1 * self.tabuTenure ) )
        self.tabuDurations.SetValue( argI, argJ, randomizedTabooDuration )
        self.tabuDurations.SetValue( argJ, argI, randomizedTabooDuration )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4