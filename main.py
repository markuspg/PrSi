#!/usr/bin/env python3

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

import sys

from analyzer import Analyzer

def main():
    print( "   <---- PrSi: Python reference Solver implementation ---->\n" )
    
    if len( sys.argv ) < 3:
        print( "Too few arguments given. Please pass the metaheuristic to use (AC|GA|TS) and the file(s) containing the problems." )
        return 0
    
    # All loading, solving and analyzing work is done in 'Analyzer'
    for i in range( len ( sys.argv ) - 2 ):
        analyzer = Analyzer( sys.argv[ 1 ], sys.argv[ i + 2 ] )
        analyzer.Run()
    
    return 0

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4