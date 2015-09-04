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

import argparse
import sys

from analyzer import Analyzer

def main():
    parser = argparse.ArgumentParser( description = "An implementation and analyzer for parallized adaptive memory metaheuristics" )
    parser.add_argument( "problemFiles", help = "The file(s) containing the problem instances to be solved", metavar = "PROBLEM FILE(S)", nargs = '+' )
    parser.add_argument( "--ga", choices = range( 1, 11 ), help = "The number of cores to run the genetic algorithm", nargs = 1, type = int )
    parser.add_argument( "--ts", choices = range( 1, 11 ), help = "The number of cores to run taboo search", nargs = 1, type = int )
    args = parser.parse_args()
    
    if not args.ga and not args.ts:
        raise RuntimeError( "There must either be specified a positive number of cores running genetic algorithm or of cores running a taboo search" )
    
    algorithmInstanceQuantities = { "ga": args.ga, "ts": args.ts }
    problemInstances = args.problemFiles
    
    print( "   <---- PrSi: Python reference Solver implementation ---->\n" )
    
    # All loading, solving and analyzing work is done in 'Analyzer'
    for problemInstancesFilePath in problemInstances:
        analyzer = Analyzer( algorithmInstanceQuantities, problemInstancesFilePath )
        analyzer.Run()
    
    return 0

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4