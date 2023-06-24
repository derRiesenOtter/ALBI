from Sequence import Sequence

class CreateSequenceArray:

    # exercise 1

    @staticmethod
    def createSequenceArray():
        print('Give Filename: ')
        filename = input()
        data = open(filename).readlines()
        sequences = []
        i = 0
        while (i < (len(data))-1):
            sequences.append(Sequence(data[i], data[i+1]))
            i += 2
        return sequences