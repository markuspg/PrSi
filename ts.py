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

import threading

class TabuSearchSolution:
    def __init__( self ):
        self.updatedFlag = None

class TabooSearch( threading.Thread ):
    def __init__( self, argAspirationCriterion, argGlobalReferenceSet, argID, argInitialSolution, argProblem, argStoppingCriterion, argTabuTenure ):
        super().__init__()
        self.aspirationCriterion = argAspirationCriterion
        self.assignedReferenceSetLocation = argGlobalReferenceSet[ argID ]
        self.globalReferenceSetIndex = argID
        self.globalReferenceSet = argGlobalReferenceSet
        self.iD = argID
        self.problem = argProblem
        self.solution = argInitialSolution
        self.stoppingCriterion = argStoppingCriterion
        self.tabuTenure = argTabuTenure
        print( "      Constructing TabooSearch instance with name '{0}' and initial solution {1}".format( self.name, self.solution ) )
    
    def run( self ):
        print( "    [TABOO_SEARCH_THREAD {0} START]".format( self.name ) )
        print( "    [TABOO_SEARCH_THREAD {0} FINISH]".format( self.name ) )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4