import unittest
import numpy as np
import pandas as pd

def createAverageScoreProfile():
    testSequences = readInputSequences("Uebung2/TestSequences.txt")
    scoreMatrix = readScoreMatrix("Uebung2/BLOSUM62.txt")
    matrix = createMatrix(len(testSequences.columns))
    relativeFrequencyTable = calculateRelativeFrequencyTable(matrix, testSequences)
    averageScoreProfile = calculateAverageScoreProfile(relativeFrequencyTable, scoreMatrix)
    print(averageScoreProfile)
    return averageScoreProfile
    
def readInputSequences(dataPath):
    testSequences = pd.read_csv(dataPath, delim_whitespace= True)
    #print(testSequences)
    return testSequences

def readScoreMatrix(dataPath):
    scoreMatrix = pd.read_csv(dataPath, delim_whitespace = True)
    #print(scoreMatrix)
    return scoreMatrix

def createMatrix(length):
    matrixArray = np.zeros([21,length])
    matrix = pd.DataFrame(matrixArray, index = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', '-'])
    #for col in range (length):
    #    for row in range(21):
    #        matrix[col][row] = 1
    #print(matrix)
    return matrix

def calculateRelativeFrequencyTable(matrix, testSequences):
    relativeFrequencyTable = matrix
    for col in range (len(testSequences.columns)):
        for row in range (len(testSequences)):
            relativeFrequencyTable.at[(testSequences.iat[row,col]), col] += 1
    #print(relativeFrequencyTable)
    for col in range (len(relativeFrequencyTable.columns)):
        for row in range (len(relativeFrequencyTable)):
            relativeFrequencyTable.iat[row, col] /= len(testSequences)
    #print(relativeFrequencyTable)
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

createAverageScoreProfile()