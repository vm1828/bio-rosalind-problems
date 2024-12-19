from shared.constants import PROBLEM, SOLUTION


def count_dna_nucleotides(s: str) -> tuple[int]:
    return (s.count('A'), s.count('C'), s.count('G'), s.count('T'))


if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = ' '.join([str(i) for i in count_dna_nucleotides(s)])
    with open(SOLUTION, 'w') as f:
        f.write(solution)
