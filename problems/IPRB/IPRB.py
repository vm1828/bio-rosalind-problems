"""Mendel's First Law"""

import math
from shared.constants import PROBLEM, SOLUTION


def iprb_soln(filename: str) -> float:
    with open(filename) as f:
        AA, Aa, aa = (int(i) for i in f.read().strip().split())
    total = AA+Aa+aa
    total_pairs = total*(total-1)/2

    # favorable pairs
    AA_AA = math.comb(AA, 2) if AA >= 2 else 0
    AA_Aa = AA*Aa
    AA_aa = AA*aa
    Aa_Aa = (math.comb(Aa, 2) if Aa >= 2 else 0)*0.75
    Aa_aa = Aa*aa*0.5
    favorable_pairs = AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa

    return round(favorable_pairs/total_pairs, 5)

# def iprb_soln(filename: str) -> float:
#   # TODO
#   with open(filename) as f:
#     AA, Aa, aa = (int(i) for i in f.read().strip().split())
#   total = AA+Aa+aa
#   d = total*(total-1)

#   p_2HomoRecessive = aa*(aa-1)/d
#   p_2Hetero = Aa*(Aa-1)/d
#   p_1HomoRecessive_1Hetero = aa*Aa/d

#   p_homo_recessive_offspring = p_2HomoRecessive*1 + p_2Hetero*0.25 + p_1HomoRecessive_1Hetero*0.5
#   p = 1 - p_homo_recessive_offspring
#   return round(p, 5)


if __name__ == '__main__':
    solution = str(iprb_soln(PROBLEM))
    with open(SOLUTION, 'w') as f:
        f.write(solution)
