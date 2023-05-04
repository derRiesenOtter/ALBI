import numpy as np
import pandas as pd

def createAverageScoreProfile():
    msa = pd.read_csv("Uebung2/TestSequences.txt", delim_whitespace= True) 
    scoreMatrix = pd.read_csv("Uebung2/BLOSUM62.txt", delim_whitespace = True)
    matrix = pd.DataFrame(np.zeros([21,len(msa.columns)]), index = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', '-'])
    relativeFrequencyTable = calculateRelativeFrequencyTable(matrix, msa)
    averageScoreProfile = calculateAverageScoreProfile(relativeFrequencyTable, scoreMatrix)
    print(averageScoreProfile)
    return averageScoreProfile

def calculateRelativeFrequencyTable(matrix, testSequences):
    relativeFrequencyTable = matrix.copy()
    for col in range (len(testSequences.columns)):
        for row in range (len(testSequences)):
            relativeFrequencyTable.at[(testSequences.iat[row,col]), col] += 1
    for col in range (len(relativeFrequencyTable.columns)):
        for row in range (len(relativeFrequencyTable)):
            relativeFrequencyTable.iat[row, col] /= len(testSequences)
    return relativeFrequencyTable
    
def calculateAverageScoreProfile(relativeFrequencyTable, scoreMatrix):
    resultMatrix = relativeFrequencyTable.copy()
    for col in range (len(resultMatrix.columns)):
        for row in range (len(resultMatrix)):
            resultMatrix.iat[row, col] = 0
    for col in range (len(resultMatrix.columns)):
        for row in range (len(resultMatrix)):
            for row2 in range (len(resultMatrix)):
                resultMatrix.iat[row, col] += relativeFrequencyTable.iat[row2, col] * scoreMatrix.at[relativeFrequencyTable.index.tolist()[row], relativeFrequencyTable.index.tolist()[row2]]
    return resultMatrix
#language server protocol
createAverageScoreProfile()