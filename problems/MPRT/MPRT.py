"""Finding a Protein Motif"""

import re
from typing import Pattern
import requests
from shared.solution import Solution


class MPRTSolution(Solution):

    @staticmethod
    def algorithm(ids: list[str], m: Pattern) -> dict[str, list[int]]:
        """
        Finds motifs in protein sequences obtained from UniProt.

        Args:
            ids (list[str]): List of UniProt IDs (e.g., accession numbers).
            m (Pattern): A compiled regular expression pattern to search for.

        Returns:
            dict[str, list[int]]: A dictionary where keys are UniProt IDs and values are lists of positions (1-based)
                                  where the motif is found in the protein sequence.
        """
        motifs = {}
        for id in ids:
            # Retrieve the data
            r = requests.get(
                f'https://rest.uniprot.org/uniprot/{id[:6]}.fasta')
            r.raise_for_status()

            # Parse the data
            # prot = ''.join(r.text.splitlines()[1:])
            prot = "".join(
                line.strip() for line in r.iter_lines(decode_unicode=True)
                if not line.startswith(">")
            )

            # Find matches of the motif
            matches = [
                i.start()+1 for i in re.finditer(f"(?={m.pattern})", prot)
            ]
            motifs[id] = matches
        return motifs

    def _parse(self) -> list[str]:
        with open(self._input_file) as f:
            print(f)
            ids = [id.strip() for id in f if id]
        return ids

    def _solve(self) -> str:
        glycosylation_motif = re.compile("N[^P][ST][^P]")
        motifs = self.algorithm(self._parsed_data, glycosylation_motif)
        result = ""
        for id, matches in motifs.items():
            if matches:
                matches = ' '.join(map(str, matches))
                result += f'{id}\n{matches}\n'
        return result.rstrip()


if __name__ == '__main__':
    MPRTSolution()
