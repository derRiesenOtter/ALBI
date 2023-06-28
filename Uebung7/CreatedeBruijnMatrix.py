import pandas as pd
import numpy as np
from Sequence import Sequence

class CreatedeBruijnMatrix:

    def __init__(self, sequences, k):
        indices = []
        # save the identifiers as indices for the matrix
        for i in range (len(sequences)):
            indices.append(sequences[i].identifier)
        # create a df in the neede size with fitting column and row names
        dataframe = pd.DataFrame(np.zeros((int(len(sequences)), int(len(sequences)))), index= indices, columns= indices)
        # traverse the whole dataset
        for i in range (len(dataframe.columns)):
            for j in range (len(dataframe.index)):
                # assemblies with the same read are not allowed
                if i != j:
                    # counter is a value smaller than k and is used to define the length of the strings to assemble
                    counter = 0
                    # score shows the length of the assembly
                    score = 0
                    while (counter < k and score == 0): 
                        # as long as counter is smaller than k and no assembly was foun (score == 0)
                        # (parts of) the prefix and suffix are compared
                        if (sequences[i].prefix(k)[0:len(sequences[i].prefix(k))-counter] == 
                            sequences[j].suffix(k)[counter:len(sequences[j].prefix(k))]):
                            score = k-counter
                        counter += 1
                    # the scores are safed in the dataframe
                    dataframe[indices[i]][indices[j]] = score
                    # the dataframe has to be read as described in following example:
                    # row r1 (TAAA), column r2 (AATT)
                    # The last 2 (value in the df) letters of the prefix of r1 (AA) 
                    # are equal to the first two letters of the suffix of r2 (AA)
        self.matrix = dataframe
        print('de-Bruijn Matrix: ')
        print (self)
        print("")

    def __str__(self):
        pd.set_option("display.precision", 0)
        return self.matrix.to_string()

        