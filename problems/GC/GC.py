"""Computing GC Content"""

from shared.constants import PROBLEM, SOLUTION


def gc_soln(filename: str) -> tuple[str]:
    with open(filename) as f:
        gc = {}
        current = None
        # get records
        for line in f.readlines():
            if line.startswith('>'):
                current = line[1:].rstrip()
                gc[current] = ''
            else:
                gc[current] += line.rstrip()
    # count percents
    for k, v in gc.items():
        gc[k] = (v.count('C')+v.count('G'))/len(v)*100
    id = max(gc, key=gc.get)
    return (id, f'{gc[id]:.6f}')

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
    solution = ' '.join(gc_soln(PROBLEM))
    with open(SOLUTION, 'w') as f:
        f.write(solution)
