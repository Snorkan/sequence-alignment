import sys
import ReverseComplement
import ReadAndStore

file = "exercise1.fasta"


def exercise1(file):
    seqs = ReadAndStore.SequenceStore(file).get()
    for seq in seqs:
        rev_gene = seq.gene + "_REVCOMP"
        s = ReverseComplement.ReverseComplement().get(seq.sequence)
        sys.stdout.write("%s: %s\n" % (rev_gene, s))


