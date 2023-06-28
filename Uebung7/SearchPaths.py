from Sequence import Sequence
import pandas as pd
from CreatedeBruijnMatrix import CreatedeBruijnMatrix

class SearchPaths: 
    
    @staticmethod
    def searchPaths(matrix):
        # create a list, that stores all paths
        allPaths = []
        # traverse through the whole dataset
        for row in range(len(matrix.matrix.index)):
            for column in range(len(matrix.matrix.columns)):
                # for all sequences, that have a number higher 0
                if (matrix.matrix.iat[row, column] > 0):
                    currentPath = [0, matrix.matrix.index[row]]
                    visited = []
                    for i in range(len(matrix.matrix.index)):
                        visited.append(False)
                    visited[row] = True
                    allPaths.append(SearchPaths.sPaths(matrix, column, row, currentPath, visited))
        return SearchPaths.cleanUpPaths(allPaths)
        
    def sPaths(matrix, previousColumn, previousRow, previousPath, visited):
        returnedPaths = []
        previousPath.append(matrix.matrix.index[previousColumn])
        previousPath[0] += matrix.matrix.iat[previousRow, previousColumn]
        visited[previousColumn] = True
        returnedPaths.append(previousPath)
        for currentColumn in range(len(matrix.matrix.columns)):
            if (matrix.matrix.iat[previousColumn, currentColumn] > 0 and visited[currentColumn] == False):
                returnedPaths.append(SearchPaths.sPaths(matrix, currentColumn, previousColumn, previousPath.copy(), visited.copy()))
        return returnedPaths
    
    def cleanUpPaths(allPaths):
        newPath = []
        for i in range(len(allPaths)):
            SearchPaths.cUpPaths(newPath, allPaths[i])
        return (newPath)

    def cUpPaths(newPath, path):
        if (isinstance (path[0], list) == False):
            newPath.append(path)
        else:
            for i in range(len(path)):
                SearchPaths.cUpPaths(newPath, path[i])

    @staticmethod
    def lenHigher3(path, matrix, sequences):
        counter = 0
        for i in range(len(path)):
            if (len(path[i]) > 3):
                counter += 1
                # print(SearchPaths.superString(path[i], matrix, sequences))
        print('Number of assemblies with more than 3 sequences: ')
        return counter
    
    @staticmethod
    def superString(seq, matrix, sequences):
        superString = ''
        for i in range(1, len(seq)-1):
            superString += (sequences[int(seq[i][1:])-1].sequence[:-1 + int(-matrix.matrix[seq[i+1]][seq[i]])])
        superString += (sequences[int(seq[len(seq)-1][1:])-1].sequence[:-1])
        while(len(superString) < 24):
            superString += ' '
        superString += '\t score: ' + str(seq[0]) + '\tsequences: '
        for i in range(1, len(seq)-1):
            superString += seq[i] + ', '
        superString +=  seq[len(seq)-1]
        return superString
    
    def bestsuperStrings(paths, matrix, sequences):
        best = []
        maximum = 0
        for i in range(len(paths)):
            if (paths[i][0] > maximum):
                maximum = paths[i][0]
                best = []
            if (paths[i][0] == maximum):
                best.append(paths[i])
        for i in range(len(best)):
            print(SearchPaths.superString(best[i], matrix, sequences))

    # def eliminateDuplicates(paths):
    #     newPath = []
    #     for i in range (len(paths)):
    #         equal = False
    #         j = 0
    #         while (j < (len(newPath)) and equal == False):
    #             if (SearchPaths.equal(paths[i], newPath[j])):
    #                 equal = True
    #             j += 1
    #         if (equal == False):
    #             newPath.append(paths[i])
    #     return newPath

    # @staticmethod
    # def equal(path1, path2):
    #     if (len(path1) == len(path2)):
    #         for i in range(len(path1)):
    #             if path1[i] != path2[i]:
    #                 return False
    #         return True
    #     else: 
    #         return False


    # @staticmethod
    # def searchPaths(matrix):
    #     # create a list, that stores all paths
    #     allPaths = []
    #     # traverse through the whole dataset
    #     for row in range(len(matrix.matrix.index)):
    #         for column in range(len(matrix.matrix.columns)):
    #             # for all sequences, that have a number higher 0
    #             if (matrix.matrix.iat[row, column] > 0):
    #                 currentPath = [0]
    #                 visited = []
    #                 for i in range(len(matrix.matrix.index)):
    #                     visited.append(False)
    #                 allPaths.append(SearchPaths.sPaths(matrix, column, row, currentPath, visited))
    #     return (allPaths)
    # #SearchPaths.cleanUpPaths

    # def sPaths(matrix, previousColumn, previousRow, previousPath, visited):
    #     returnedPaths = []
    #     previousPath.append(matrix.matrix.index[previousRow])
    #     previousPath[0] += matrix.matrix.iat[previousRow, previousColumn]
    #     visited[previousRow] = True
    #     returnedPaths.append(previousPath)
    #     for currentColumn in range(len(matrix.matrix.columns)):
    #         if (matrix.matrix.iat[previousColumn, currentColumn] > 0 and visited[currentColumn] == False):
    #             returnedPaths.append(SearchPaths.sPaths(matrix, currentColumn, previousColumn, previousPath.copy(), visited.copy()))
    #     return returnedPaths
    
    # def cleanUpPaths(allPaths):
    #     newPath = []


        
        
                
        
    # return matrix.matrix[matrix.matrix.columns[0]][matrix.matrix.index[1]]
    # @staticmethod
    # def searchPaths(matrix):
    #     paths = []
    #     indices = matrix.matrix.columns
    #     for i in range (len(indices)):
    #         for j in range (len(indices)):
    #             if (matrix.matrix[indices[j]][indices[i]] > 0):
    #                 currentPath = [indices[i]]
    #                 visited = []
    #                 for k in range (len(indices)):
    #                     visited.append(False)
    #                 visited[i] = True
    #                 paths.append(currentPath)
    #                 done = False
    #                 while (not done):

                    
    #     return paths

    # @staticmethod
    # def searchPaths(matrix):
    #     paths = []
    #     visited = []
    #     indices = matrix.matrix.columns
    #     for i in range (len(indices)):
    #         visited.append(False)
    #     for column in range (len(indices)):
    #         score = 0
    #         if (matrix.matrix[indices[column]][indices[0]] > 0):
    #             currentPath = (matrix.matrix[indices[0]])
    #             visited[0] = True
    #             score += matrix.matrix[indices[column]][indices[0]]
    #             paths.append(SearchPaths.sPaths(currentPath, paths, matrix, indices, visited.copy(), 0, column, 0))
    #     return paths

    # @staticmethod
    # def sPaths(currentPath, paths, matrix, indices, visited, row, column, score):
    #     if (matrix.matrix[indices[column]][indices[row]] == 0 or visited[row] == True):
    #         return
    #     currentPath.append((matrix.matrix[indices[row]]))
    #     visited[row] = True
    #     for i in range(len(indices)):
    #         currentPath.append(SearchPaths.sPaths(matrix, indices, visited.copy(), 0, i, 0))
    #         paths.append(currentPath)
        
        
        


    
    # def createSuperString(paths, matrix):
    #     superString = []
    #     return superString