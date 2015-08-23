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

from builder import Builder
from qap import QAP

def main():
    # Check for correct building of matrices
    builder = Builder( "test|3|1;2;3;4;5;6;7;8;9|1;10;100;1000;10000;1000;100;10;1", "QAP" )
    assert builder.flowMatrix == [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    assert builder.distanceMatrix == [ [ 1, 10, 100 ], [ 1000, 10000, 1000 ], [ 100, 10, 1 ] ]
    print( "[CHECK] Matrices were successfully constructed" )
    
    # Check if builder fails if an unknown problem was encountered
    try:
        builder = Builder( "test|3|1;2;3;4;5;6;7;8;9|1;10;100;1000;10000;1000;100;10;1", "FAP" )
    except ValueError:
        print( "[CHECK] Unknown problem was successfully caught" )
        
    # Check for correct creation of QAP
    builder = Builder( "test|3|1;2;3;4;5;6;7;8;9|1;10;100;1000;10000;1000;100;10;1", "QAP" )
    qap = QAP( builder )
    assert qap.problemName == "test"
    assert qap.problemSize == 3
    assert qap.flowMatrix == [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    assert qap.distanceMatrix == [ [ 1, 10, 100 ], [ 1000, 10000, 1000 ], [ 100, 10, 1 ] ]
    print( "[CHECK] QAP was successfully constructed" )
    
    return 0

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
