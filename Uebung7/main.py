from Sequence import Sequence 
import pandas as pd
from CreatedeBruijnMatrix import CreatedeBruijnMatrix 
from SearchPaths import SearchPaths

def main():
    ######################
    print('')
    # set k to 2
    # give following filename ALBI_SS23_7_Uebung.fasta
    
    ######################

    # exercise 1 and 2 see Sequence and createSequenceArray
    print("Set k value:")
    k = int(input())
    sequences = Sequence.createSequenceArray()
    # print(sequences)

    ######################

    # exercise 3 see CreateddeBruijnMatrix
    matrix = CreatedeBruijnMatrix(sequences, k)
    print('')
    print('de-Bruijn Matrix: ')
    print (matrix)
    print('')

    ######################

    # exercise 4 see SearchPaths
    paths = SearchPaths.searchPaths(matrix)
    # file = open('paths.txt', 'w')
    # for i in range (len(paths)):
    #     for j in range (len(paths[i])):
    #         file.write(str(paths[i][j]))
    #     file.write("\n")

    ######################

    #4a und b und c
    print (SearchPaths.lenHigher3(paths, matrix, sequences))
    print('')
    ######################

    #4b
    print('Best assemblies: ')
    SearchPaths.bestsuperStrings(paths, matrix, sequences)
    print('')

    ######################
    


if __name__ == "__main__":
    main()

