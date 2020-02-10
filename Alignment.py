import ReverseComplement


class GetPositions:

    def __find_alignment(self, sequence, pattern, p, positions):
        while p < len(sequence):
            p = sequence.find(pattern, p)
            if p == -1:
                break
            positions.append(p)
            return self.__find_alignment(sequence, pattern, p + 1, positions)
        return positions

    def forward_strand(self, sequence, query):
        m = self.__find_alignment(sequence, query, 0, [])
        return m

    # Functions to align both forward and reverse strand
    def __align_both(self, sequence, pattern):
        return self.__find_alignment(sequence, pattern, 0, [])

    def both_strands(self, sequence, query):
        rev_seq = ReverseComplement.ReverseComplement().get(sequence)
        m = self.__align_both(sequence, query) + self.__align_both(rev_seq, query)
        return m

    # Functions to allow up to two mismatches
    def __hamming_distance(self, str1, str2):
        count = 0
        for a, b in zip(str1, str2):
            if a != b:
                count += 1
        return count

    def __check_hamming(self, sequence, pattern):
        positions = []
        for p in range(len(sequence) - len(pattern) + 1):
            hd = self.__hamming_distance(pattern, sequence[p:p + len(pattern)])
            if hd <= 2:
                positions.append(p)
        return positions

    def with_mismatch(self, sequence, query):
        rev_seq = ReverseComplement.ReverseComplement().get(sequence)
        m = self.__check_hamming(sequence, query) + self.__check_hamming(rev_seq, query)
        return m










