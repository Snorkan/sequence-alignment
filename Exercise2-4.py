import sys
import ReadAndStore
import Alignment

queryfile = "queries.fasta"
fastafile = "exercise1.fasta"

# For use of fasta files, access to index, eg. seq_store[0]
seq_store = ReadAndStore.SequenceStore(fastafile).get()

queries = ReadAndStore.SequenceStore(queryfile).get()
fasta_object = ReadAndStore.OneFasta()
get_positions = Alignment.GetPositions()


# Takes a fasta file in format "GeneX\nSEQUENCE" and returns positions where the queries align
def exercise2(fasta):
    positions = []
    f = fasta_object.format(fasta)
    for query in queries:
        q = fasta_object.format(query)
        positions.append("%s: %s" % (q.gene, get_positions.forward_strand(f.sequence, q.sequence)))
    sys.stdout.write("Alignment Positions | %s: %s\n" % (f.gene, positions))


# Same as Ex2, but now we check alignment for the reverse strand as well
def exercise3(fasta):
    positions = []
    f = fasta_object.format(fasta)
    for query in queries:
        q = fasta_object.format(query)
        positions.append("%s: %s" % (q.gene, get_positions.both_strands(f.sequence, q.sequence)))
    sys.stdout.write("Alignment Positions | %s: %s\n" % (f.gene, positions))


# Same as Ex3 but allows up to two mismatches
def exercise4(fasta):
    positions = []
    f = fasta_object.format(fasta)
    for query in queries:
        q = fasta_object.format(query)
        positions.append("%s: %s" % (f.gene, get_positions.with_mismatch(f.sequence, q.sequence)))
    sys.stdout.write("Alignment Positions | %s: %s\n" % (f.gene, positions))

