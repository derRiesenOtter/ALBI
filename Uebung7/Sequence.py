class Sequence:

    # exercise 1
    def __init__(self, name, sequence):
        self.identifier = name[1:-1]
        self.sequence = sequence

    def __str__(self):
        return 'Identifier: ' + self.identifier + 'Sequence: ' + self.sequence
    
    # exercise 2
    def prefix(self, k = 2):
        return self.sequence[0:k]

    def suffix(self, k = 2): 
        return self.sequence[len(self.sequence) - (k+1) : len(self.sequence)]
    
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