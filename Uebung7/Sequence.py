class Sequence:
    """
    A class used to save sequences

    Attributes
    ----------
    identifier : str
        the identifier of the sequence
    sequence : str
        the sequence itself

    Methods
    -------
    createSequenceArray(file)
        creates a list of sequences from a given fasta file
    
    prefix(k = 2)
        returns the first k letters of the seuquence. 

    suffix(k = 2)
        returns the last k letters of the sequence.
    """

    ##### exercise 1 #####

    def __init__(self, name, sequence):
        """
        Parameters
        ----------
        identifier : str
            the identifier of the sequence
        sequence : str
            the sequence itself
        """

        self.identifier = name[1:-1]
        self.sequence = sequence

    def __str__(self):
        return 'Identifier: ' + self.identifier + ' Sequence: ' + self.sequence
    
    @staticmethod
    def createSequenceList():
        """
        creates a list of sequences from a given fasta file and prints it

        Parameters
        ----------
        filename : str
            filename of the .fasta file

        Returns
        -------
        sequences : list 
            list containing Sequence objects

        Raises
        ------
        FileNotFoundError
            if no readable file is given via input
        """
        
        while True:
            try:
                data = open(input("\nEnter filename: ")).readlines()
                break
            except FileNotFoundError:
                print("Oops!  That was no valid filename.  Try again...") 
        sequences = []
        i = 0
        # seperates identifier and sequence only by their line
        # if the sequences are longer a different separation method has to be used
        while (i < (len(data))-1):
            sequences.append(Sequence(data[i], data[i+1]))
            i += 2
        print("")
        for i in range(len(sequences)):
            print(sequences[i])
        return sequences
    
    ##### exercise 2 #####

    def prefix(self, k = 2):
        """
        returns the first k letters of the sequence
        
        if k is not set, the default value of 2 is used

        Parameters
        ----------
        k : int, optional
            sets the length of the returned string

        Returns
        -------
        str
            the first k letters of the sequence
        """

        return self.sequence[0:k]

    def suffix(self, k = 2): 
        """
        returns the last k letters of the sequence
        
        if k is not set, the default value of 2 is used

        Parameters
        ----------
        k : int, optional
            sets the length of the returned string

        Returns
        -------
        str
            the last k letters of the sequence
        """

        return self.sequence[len(self.sequence) - (k+1) :]
    
