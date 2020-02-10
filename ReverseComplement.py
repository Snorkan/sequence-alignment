class ReverseComplement:

    def get(self, sequence):
        return self.__rev_seq(sequence)

    def __find_complement(self, n):
        if n == "A" or n == "C" or n == "G" or n == "T":
            switch = {
                "A": "T",
                "T": "A",
                "C": "G",
                "G": "C"
            }
            return switch[n]
        return n

    def __rev_seq(self, sequence):
        return "".join([self.__find_complement(nucleotide) for nucleotide in sequence])[::-1]

