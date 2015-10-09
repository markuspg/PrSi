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

class Options:
    def __init__( self, argCommandLineArgumentsDict ):
        self.cpuCores = multiprocessing.cpu_count()
        self.currentProblemFile = str()
        self.currentProblemType = str()
        self.gaThreadsQuantity = argCommandLineArgumentsDict.ga[ 0 ]
        self.nMaxIterations = 1000000
        self.problemFiles = argCommandLineArgumentsDict.problemFiles
        self.tsThreadsQuantity = argCommandLineArgumentsDict.ts[ 0 ]
        print( "  Options constructor. The following settings will be used:" )
        print( "    gaThreadsQuantity:\t{0}".format( self.gaThreadsQuantity ) )
        print( "    problemFiles:\t{0}".format( self.problemFiles ) )
        print( "    tsThreadsQuantity:\t{0}".format( self.tsThreadsQuantity ) )
    
    def GetProblem( self ):
        assert self.problemFiles, "'Options.GetProblem()' may not be called if no problem files are available"
        temp = self.problemFiles[ 0 ]
        del self.problemFiles[ 0 ]
        return temp

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4