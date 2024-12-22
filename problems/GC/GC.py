"""Computing GC Content"""

from shared.solution import Solution


class GCSolution(Solution):

    @staticmethod
    def algorithm(gc: dict[str, str]) -> tuple[str, str]:
        """
        Computes GC content for each DNA sequence and returns the ID of the sequence 
        with the highest GC content and its percentage.

        Args:
            gc (dict[str, str]): Dictionary of sequence IDs and DNA sequences.

        Returns:
            tuple[str, str]: Sequence ID with the highest GC content and its percentage.
        """
        for k, v in gc.items():
            gc[k] = (v.count('C')+v.count('G'))/len(v)*100
        id = max(gc, key=gc.get)
        return (id, f'{gc[id]:.6f}')

    def _parse(self) -> dict[str, str]:
        with open(self._input_file) as f:
            data = {}
            current = None
            # get records
            for line in f.readlines():
                if line.startswith('>'):
                    current = line[1:].rstrip()
                    data[current] = ''
                else:
                    data[current] += line.rstrip()
        return data

    def _solve(self) -> str:
        id, p = self.algorithm(self._parsed_data)
        return f'{id}\n{p}'

# def gc_soln(filename: str) -> tuple[str]:
#   with open(filename) as f:
#     s = f.read()
#   genes = s.split(">")[1:]
#   gc = []
#   for gene in genes:
#     a = gene.count("C") + gene.count("G")
#     b = gene.count("C") + gene.count("G") + gene.count("A") + gene.count("T")
#     gc.append(float(a)*100/b)
#   return (genes[gc.index(max(gc))][:13], f'{max(gc):.6f}')

# def gc_soln(filename: str) -> tuple:
#   gc = {}
#   for record in SeqIO.parse(filename, 'fasta'):
#     gc[record.id] = gc_fraction(record.seq)
#   id = max(gc, key=gc.get)
#   return (id, f'{gc[id]*100:.6f}')


if __name__ == '__main__':
    GCSolution()
