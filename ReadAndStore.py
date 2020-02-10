class SequenceStore:
    list_contents = []

    def __init__(self, file):
        with open(file, "r") as f:
            file_contents = f.read().rsplit(">")
            self.list_contents = list(filter(lambda x: x != "", file_contents))

    def get(self):
        return self.list_contents


class OneFasta(object):
    gene = ""
    sequence = ""

    def format(self, fasta):
        i = fasta.find('\n')
        one = OneFasta()
        one.gene = fasta[0:i]
        one.sequence = fasta[i:].replace("\n", "").upper()
        return one




