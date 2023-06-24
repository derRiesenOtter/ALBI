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
    