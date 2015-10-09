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

from options import Options

import argparse
import multiprocessing
import sys

from analyzer import Analyzer

def main():
    parser = argparse.ArgumentParser( description = "An implementation and analyzer for parallized adaptive memory metaheuristics" )
    parser.add_argument( "problemFiles", help = "The file(s) containing the problem instances to be solved", metavar = "PROBLEM FILE", nargs = '+' )
    parser.add_argument( "--ga", choices = range( 0, 11 ), default = [ 0 ], help = "The number of cores to run the genetic algorithm", nargs = 1, type = int )
    parser.add_argument( "--ts", choices = range( 0, 11 ), default = [ 0 ], help = "The number of cores to run taboo search", nargs = 1, type = int )
    args = parser.parse_args()
    
    if args.ga == [ 0 ] and args.ts == [ 0 ]:
        raise RuntimeError( "There must either be specified a positive number of cores running genetic algorithm or of cores running a taboo search" )
    
    if args.ga[ 0 ] + args.ts[ 0 ] + 1 > multiprocessing.cpu_count():
        raise RuntimeError( "The number of requested cores '{0}' (+1 managing core) is bigger than the physically available quantity of '{1}' cores".format( args.ga + args.ts, multiprocessing.cpu_count() ) )
    
    print( "   <---- PrSi: Python reference Solver implementation ---->\n" )
    
    options = Options( args )
    
    # All loading, solving and analyzing work is done in 'Analyzer'
    for i in range( len( options.problemFiles ) ):
        analyzer = Analyzer( options )
        analyzer.Run()
    
    return 0

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4