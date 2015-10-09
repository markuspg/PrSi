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
    def __init__( self, argProblem ):
        print( "  Solver constructor" )
        self.problem = argProblem
        
        # The 'ManagerThread' is mandatory to control all other threads
        self.managerThread = ManagerThread( self.problem )
    
    def Solve( self ):
        print( "    Solving problem" )
        self.managerThread.start()
        print( "    Started managerThread" )
        # It is only separated for the reason of better clarity ...
        # of the real thread quantity, so block until this thread finishes
        self.managerThread.join()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4