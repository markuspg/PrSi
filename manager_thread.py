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

import ga
import multiprocessing
import threading
import ts

class ManagerThread( threading.Thread ):
    def __init__( self, argHelperTuple ):
        super().__init__()
        self.bounds = argHelperTuple[ 0 ]
        self.gaInstances = int( argHelperTuple[ 2 ][ "ga" ][ 0 ] )
        self.gaThreads = list()
        self.heuristicQuantities = argHelperTuple[ 2 ]
        self.nMaxIterations = 1000000
        self.tsInstances = int( argHelperTuple[ 2 ][ "ts" ][ 0 ] )
        self.tsGlobalMemory = ts.TabuSearchReferenceSolutions( self.tsInstances )
        self.tsThreads = list()
        self.measure = argHelperTuple[ 1 ]
        self.problem = argHelperTuple[ 3 ]
        self.cpuCores = multiprocessing.cpu_count()
        print( "    Initializing ManagerThread to work on {0} cores".format( self.cpuCores ) )
    
    def CreateRandomPopulation( self ):
        population = list()
        for i in range( ga.GeneticAlgorithm.populationSize ):
            population.append( self.problem.CreateRandomRandomKeys() )
            # print( population[ -1 ] )
        
        # print( "      Created a random population of size {0}".format( len( population ) ) )
        return population
    
    def run( self ):
        print( "    [MANAGER_THREAD {0} START] Running manager".format( self.name ) )
        # Initialize
        for i in range( self.gaInstances ):
            self.gaThreads.append( ga.GeneticAlgorithm( self.CreateRandomPopulation(), self.problem ) )
        for i in range( self.tsInstances ):
            self.tsThreads.append( ts.TabooSearch( self.problem.CreateRandomRandomKeys(), self.problem ) )
        for thread in self.gaThreads:
            thread.start()
        for thread in self.tsThreads:
            thread.start()
        
        # Start search
        print( "    [MANAGER_THREAD {0} FINISH] Finishing manager".format( self.name ) )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
