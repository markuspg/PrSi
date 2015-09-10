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
from matrix import Matrix
from qap import QAP

def main():
    # Check for correct building of matrices
    builder = Builder( "test|3|1;2;3;4;5;6;7;8;9|1;10;100;1000;10000;1000;100;10;1", "QAP" )
    assert builder.flowMatrix.matrix == [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    assert builder.distanceMatrix.matrix == [ [ 1, 10, 100 ], [ 1000, 10000, 1000 ], [ 100, 10, 1 ] ]
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
    assert qap.flowMatrix.matrix == [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    assert qap.distanceMatrix.matrix == [ [ 1, 10, 100 ], [ 1000, 10000, 1000 ], [ 100, 10, 1 ] ]
    print( "[CHECK] QAP was successfully constructed" )
    
    # Check for correct objective function value calculation
    assert qap.CalculateObjectiveValue( [ 1, 2, 3 ] ) == 50010, "Objective value calculation failed for assignment '[ 1, 2, 3 ]'"
    assert qap.CalculateObjectiveValue( [ 3, 2, 1 ] ) == 51000, "Objective value calculation failed for assignment '[ 3, 2, 1 ]'"
    assert qap.CalculateObjectiveValue( [ 1, 3, 2 ] ) == 6081, "Objective value calculation failed for assignment '[ 1, 3, 2 ]'"
    print( "[CHECK] All QAP objective value calculations where correct" )
    
    assert qap.ConvertRandomKeysToSolution( [ 0.05, 0.91, 0.95 ] ) == [ 1, 2, 3 ], "Random key conversion failed for an equivalent of '[ 1, 2, 3 ]'"
    assert qap.ConvertRandomKeysToSolution( [ 0.05, 0.66, 0.65 ] ) == [ 1, 3, 2 ], "Random key conversion failed for an equivalent of '[ 1, 3, 2 ]'"
    assert qap.ConvertRandomKeysToSolution( [ 0.99, 0.5, 0.0001 ] ) == [ 3, 2, 1 ], "Random key conversion failed for an equivalent of '[ 3, 2, 1 ]'"
    assert qap.ConvertRandomKeysToSolution( [ 0.5, 0.5, 0.0001 ] ) == [ 2, 3, 1 ], "Random key conversion failed for an equivalent of '[ 2, 3, 1 ]'"
    print( "[CHECK] Converting QAP random keys to solutions yielded valid results" )
    
    testRandomKeysSolution = qap.CreateRandomRandomKeys()
    assert len( testRandomKeysSolution ) == qap.problemSize, "Random random keys solution vector has an invalid size"
    for item in testRandomKeysSolution:
        assert isinstance( item, float ), "Wrong type of element in random random keys solution vector"
    
    # Test the Matrix class using the construction method from parameters
    testmatrix = Matrix.FromParameters( None, 3, 5 )
    # Check the amount of rows
    assert len( testmatrix.matrix ) == 3, "Wrong quantity of rows"
    # Check the amount of columns
    assert len( testmatrix.matrix[ 0 ] ) == 5, "Wrong quantity of columns"
    # Test the Matrix class using the construction method from semicolon separated values
    testmatrix = Matrix.FromSSV( "1;2;3;4;5;6;7;8;9;10;11;12", 3, 4 )
    # Check the amount of rows
    assert len( testmatrix.matrix ) == 3, "Wrong quantity of rows"
    # Check the amount of columns
    assert len( testmatrix.matrix[ 0 ] ) == 4, "Wrong quantity of columns"
    assert testmatrix.GetValue( 1, 0 ) == 5, "Wrong value in matrix"
    assert testmatrix.GetValue( 2, 3 ) == 12, "Wrong value in matrix"
    # Test the Matrix class using the standard constructor
    testmatrix = Matrix( [ [ 10, 8, 31 ], [ 14, 25, 6 ], [ 72, 85, 19 ], [ 10, 10, 12 ] ] )
    # Re-check the amount of rows
    assert len( testmatrix.matrix ) == 4, "Wrong quantity of rows"
    # Re-check the amount of columns
    assert len( testmatrix.matrix[ 0 ] ) == 3, "Wrong quantity of columns"
    assert testmatrix.GetValue( 0, 0 ) == 10
    assert testmatrix.GetValue( 2, 1 ) == 85
    # print( testmatrix )
    testmatrix.SetValue( 1, 2, 48 )
    # print( testmatrix )
    assert testmatrix.GetValue( 1, 2 ) == 48
    assert testmatrix.GetMinimumValue() == ( 8, 0, 1 )
    print( "[CHECK] Matrix tests completed successfully" )
    
    return 0

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
