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

from manager_thread import ManagerThread

class Solver:
    def __init__( self, argHelperTuple ):
        print( "  Solver constructor" )
        self.bounds = argHelperTuple[ 0 ]
        self.heuristicQuantities = argHelperTuple[ 2 ]
        self.measure = argHelperTuple[ 1 ]
        self.problem = argHelperTuple[ 3 ]
        
        # The 'ManagerThread' is mandatory to control all other threads
        self.managerThread = ManagerThread( argHelperTuple )
        self.managerThread.start()
        print( "    Started managerThread" )
        # It is only separated for the reason of better clarity ...
        # of the real thread quantity, so block until this thread finishes
        self.managerThread.join()
    
    def Solve( self ):
        print( "    Solving problem using '{0}'".format( self.heuristicQuantities ) )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4