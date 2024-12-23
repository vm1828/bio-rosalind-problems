"""Models for sequencing data"""

from dataclasses import dataclass


@dataclass
class FastaRecord:
    id: str
    seq: str
