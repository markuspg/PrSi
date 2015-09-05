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

from bounds import Bounds
from builder import Builder
from measure import Measure
from problem import Problem
from qap import QAP
from solver import Solver

class Analyzer:
    def __init__( self, argMetaheuristicQuantities, argProblemsFileName ):
        self.metaheuristicQuantities = argMetaheuristicQuantities
        self.problemsFileName = argProblemsFileName
        self.problemType = argProblemsFileName.rpartition( '.' )[ -1 ].upper()
        print( "Will analyze problems of type '{0}' loaded from '{1}' using '{2}'".format( self.problemType, self.problemsFileName, self.metaheuristicQuantities ) )
    
    def LoadProblem( self, argBuilder ):
        if argBuilder.problemType == "QAP":
            # print( "  Trying to construct a QAP instance" )
            return QAP( argBuilder )
        else:
            raise ValueError( "Invalid problem type encountered in 'LoadProblem' of 'Analyzer'" )
    
    def Run( self ):
        print( "Analyzing problems" )
        with open( self.problemsFileName, 'rt' ) as problemsFile:
            problemIndex = 0
            for line in problemsFile:
                problemIndex = problemIndex + 1
                print( "\n=> Problem #" + str( problemIndex ) + " will be analyzed" )
                builder = Builder( line, self.problemType )
                problem = self.LoadProblem( builder )
                measure = Measure( problem )
                bounds = Bounds( measure, problem )
                bounds.CalculateBounds()
                helperTuple = bounds, measure, self.metaheuristicQuantities, problem
                solver = Solver( helperTuple )
                solver.Solve()
                measure.Write()
        print( "Finished analyzer run" )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4