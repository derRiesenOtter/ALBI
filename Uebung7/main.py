from Sequence import Sequence 
import pandas as pd
from CreatedeBruijnMatrix import CreatedeBruijnMatrix 
from SearchPaths import SearchPaths
import unittest

# set k to 2
# give following filename ALBI_SS23_7_Uebung.fasta

def main():

    ##### set k value #####
    while True:
        try:
            k = int(input("\nSet k value: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    # Exercise 1 and 2 #
    #------------------#
    sequences = Sequence.createSequenceList()

    # Exercise 3 #
    #------------#
    deBruijin = CreatedeBruijnMatrix(sequences, k)

    # Exercise 4 #
    #------------#
    paths = SearchPaths.searchPaths(deBruijin)

    # Exercise 4a #
    #-------------# 
    print (SearchPaths.lenHigher3(paths, deBruijin, sequences))
    print('')
    ######################

    # Exercise 4b #
    #-------------# 
    print('Best assemblies: ')
    SearchPaths.bestsuperStrings(paths, deBruijin, sequences)
    print('')
 
# Testing <3 #
#-------------#

class TestEverything(unittest.TestCase):
    def test_sequences(self):
        self.assertEqual (Sequence.createSequenceList()[1].identifier,  "r2"), "result should be r2"
        self.assertEqual (Sequence.createSequenceList()[2].sequence,  "TTT\n"), "result should be TTT"
        self.assertEqual (Sequence.createSequenceList()[3].prefix(), "TT"), "result should be TT"
        self.assertEqual (Sequence.createSequenceList()[3].suffix(), "CT\n"), "result should be TT"
    def test_deBruijn(self):
        self.assertEqual (CreatedeBruijnMatrix(Sequence.createSequenceList(), 2).matrix.iat[0, 1], 2.0)
    def test_searchPaths(self):
        self.assertEqual (SearchPaths.bestsuperStrings(SearchPaths.searchPaths(CreatedeBruijnMatrix(Sequence.createSequenceList(), 2)), CreatedeBruijnMatrix(Sequence.createSequenceList(), 2), Sequence.createSequenceList())[:20], "TAAATTTCTCCTCCTCTGGT")

if __name__ == "__main__":
    main()
    #unittest.main()

