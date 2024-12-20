# script for creating template directories for problems

import os
import sys


def create_template_dir(id, title=False):
    """Create problem dir template"""
    directory = os.path.join('problems', id)

    if os.path.exists(directory):
        print(f"Directory '{directory}' already exists.")
        return

    # Create dir
    os.makedirs(directory)

    # Create files
    init_file = os.path.join(directory, '__init__.py')
    main_file = os.path.join(directory, f'{id}.py')
    test_file = os.path.join(directory, f'test_{id}.py')
    for file_path in [init_file, main_file, test_file]:
        open(file_path, 'a').close()

    # Write title to the main file
    func_name = f'{id.lower()}_soln'
    func_code = f"""\"""{title}\"""

from shared.constants import PROBLEM, SOLUTION
    
def {func_name}():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = {func_name}(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

"""

    test_code = f"""from problems.{id}.{id} import {func_name}

test_input = ""
test_output = ""

# def test_{func_name}():
#     assert {func_name}(test_input) == test_output

"""
    if title:
        with open(main_file, 'w') as f:
            f.write(func_code)
        with open(test_file, 'w') as f:
            f.write(test_code)

    print(
        f"Template directory'{directory}' with files '__init__.py', '{id}.py', and 'test_{id}.py' created.")


# if __name__ == "__main__":
#     # create single dir using cli
#     if len(sys.argv) != 2:
#         print("Usage: python3 ./shared/create_template_dir.py <id>")
#         sys.exit(1)

#     id = sys.argv[1]
#     create_template_dir(id)

if __name__ == "__main__":
    # batch create problem template directories
    problems = """DNA Counting DNA Nucleotides
RNA Transcribing DNA into RNA
REVC Complementing a Strand of DNA
FIB Rabbits and Recurrence Relations
GC Computing GC Content
HAMM Counting Point Mutations
IPRB Mendel's First Law
PROT Translating RNA into Protein
SUBS Finding a Motif in DNA
CONS Consensus and Profile
FIBD Mortal Fibonacci Rabbits
GRPH Overlap Graphs
IEV Calculating Expected Offspring
LCSM Finding a Shared Motif
LIA Independent Alleles
MPRT Finding a Protein Motif
MRNA Inferring mRNA from Protein
ORF Open Reading Frames
PERM Enumerating Gene Orders
PRTM Calculating Protein Mass
REVP Locating Restriction Sites
SPLC RNA Splicing
LEXF Enumerating k-mers Lexicographically
LGIS Longest Increasing Subsequence
LONG Genome Assembly as Shortest Superstring
PMCH Perfect Matchings and RNA Secondary Structures
PPER Partial Permutations
PROB Introduction to Random Strings
SIGN Enumerating Oriented Gene Orderings
SSEQ Finding a Spliced Motif
TRAN Transitions and Transversions
TREE Completing a Tree
KMER k-Mer Composition
LEXV Ordering Strings of Varying Length Lexicographically
CAT Catalan Numbers and RNA Secondary Structures
CORR Error Correction in Reads
INOD Counting Phylogenetic Ancestors
KMP Speeding Up Motif Finding
LCSQ Finding a Shared Spliced Motif
MMCH Maximum Matchings and RNA Secondary Structures
PDST Creating a Distance Matrix
REAR Reversal Distance
RSTR Matching Random Motifs
SSET Counting Subsets
ASPC Introduction to Alternative Splicing
EDIT Edit Distance
EVAL Expected Number of Restriction Sites
MOTZ Motzkin Numbers and RNA Secondary Structures
NWCK Distances in Trees
SCSP Interleaving Two Motifs
SETO Introduction to Set Operations
SORT Sorting by Reversals
SPEC Inferring Protein from Spectrum
TRIE Introduction to Pattern Matching
CONV Comparing Spectra with the Spectral Convolution
CTBL Creating a Character Table
DBRU Constructing a De Bruijn Graph
EDTA Edit Distance Alignment
FULL Inferring Peptide from Full Spectrum
INDC Independent Segregation of Chromosomes
ITWV Finding Disjoint Motifs in a Gene
LREP Finding the Longest Multiple Repeat
NKEW Newick Format with Edge Weights
RNAS Wobble Bonding and RNA Secondary Structures
AFRQ Counting Disease Carriers
CSTR Creating a Character Table from Genetic Strings
CTEA Counting Optimal Alignments
CUNR Counting Unrooted Binary Trees
GLOB Global Alignment with Scoring Matrix
PCOV Genome Assembly with Perfect Coverage
PRSM Matching a Spectrum to a Protein
QRT Quartets
SGRA Using the Spectrum Graph to Infer Peptides
SUFF Encoding Suffix Trees
CHBP Character-Based Phylogeny
CNTQ Counting Quartets
EUBT Enumerating Unrooted Binary Trees
GASM Genome Assembly Using Reads
GCON Global Alignment with Constant Gap Penalty
LING Linguistic Complexity of a Genome
LOCA Local Alignment with Scoring Matrix
MEND Inferring Genotype from a Pedigree
MGAP Maximizing the Gap Symbols of an Optimal Alignment
MREP Identifying Maximal Repeats
MULT Multiple Alignment
PDPL Creating a Restriction Map
ROOT Counting Rooted Binary Trees
SEXL Sex-Linked Inheritance
SPTD Phylogeny Comparison with Split Distance
WFMD The Wright-Fisher Model of Genetic Drift
ALPH Alignment-Based Phylogeny
ASMQ Assessing Assembly Quality with N50 and N75
CSET Fixing an Inconsistent Character Set
EBIN Wright-Fisher's Expected Behavior
FOUN The Founder Effect and Genetic Drift
GAFF Global Alignment with Scoring Matrix and Affine Gap Penalty
GREP Genome Assembly with Perfect Coverage and Repeats
OAP Overlap Alignment
QRTD Quartet Distance
SIMS Finding a Motif with Modifications
SMGB Semiglobal Alignment
KSIM Finding All Similar Motifs
LAFF Local Alignment with Affine Gap Penalty
OSYM Isolating Symbols in Alignments
RSUB Identifying Reversing Substitutions"""

    # Parse the data into tuples
    problems = [
        tuple(line.split(maxsplit=1)) for line in problems.strip().split("\n")
    ]

    # Print the result
    for problem in problems:
        create_template_dir(*problem)
