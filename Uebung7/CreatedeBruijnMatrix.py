import pandas as pd
import numpy as np
from Sequence import Sequence

class CreatedeBruijnMatrix:

    def __init__(self, sequences, k):
        indices = []
        for i in range (len(sequences)):
            indices.append(sequences[i].identifier)
        dataframe = pd.DataFrame(np.zeros((int(len(sequences)), int(len(sequences)))), index= indices, columns= indices)
        for i in range (len(dataframe.columns)):
            for j in range (len(dataframe.index)):
                if i != j:
                    counter = 0
                    score = 0
                    while (counter < k and score == 0): 
                        if (sequences[i].prefix(k)[0:len(sequences[i].prefix(k))-counter] == sequences[j].suffix(k)[counter:len(sequences[j].prefix(k))]):
                            score = k-counter
                        counter += 1
                    dataframe[indices[i]][indices[j]] = score
        self.matrix = dataframe

    def __str__(self):
        pd.set_option("display.precision", 0)
        return self.matrix.to_string()

        