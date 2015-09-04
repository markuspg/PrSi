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

import multiprocessing
import threading

class ManagerThread( threading.Thread ):
    def __init__( self, argHelperTuple ):
        super().__init__()
        self.bounds = argHelperTuple[ 0 ]
        self.heuristic = argHelperTuple[ 2 ]
        self.measure = argHelperTuple[ 1 ]
        self.problem = argHelperTuple[ 3 ]
        self.cpuCores = multiprocessing.cpu_count()
        print( "    Initializing ManagerThread to work on {0} cores".format( self.cpuCores ) )
    
    def run( self ):
        print( "    [MANAGER_THREAD {0} START] Running manager".format( self.name ) )
        print( "    [MANAGER_THREAD {0} FINISH] Finishing manager".format( self.name ) )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4