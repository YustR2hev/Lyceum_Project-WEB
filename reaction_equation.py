import sympy
import re

ELEMENT_CLAUSE = re.compile("([A-Z][a-z]?)([0-9]*)")


def parse_compound(compound):
    return {el: (int(num) if num else 1) for el, num in ELEMENT_CLAUSE.findall(compound)}


def main(data):
    in_ = data
    left_half_strings = in_.replace(' ', '').split('=')[0].split('+')
    left_half_compounds = [parse_compound(compound) for compound in left_half_strings]

    right_half_strings = in_.replace(' ', '').split('=')[1].split('+')
    right_half_compounds = [parse_compound(compound) for compound in right_half_strings]

    els = sorted(set().union(*left_half_compounds, *right_half_compounds))
    els_index = dict(zip(els, range(len(els))))

    w = len(left_half_compounds) + len(right_half_compounds)
    h = len(els)
    pre_res = [[0] * w for _ in range(h)]
    for col, compound in enumerate(left_half_compounds):
        for el, num in compound.items():
            row = els_index[el]
            pre_res[row][col] = num
    for col, compound in enumerate(right_half_compounds, len(left_half_compounds)):
        for el, num in compound.items():
            row = els_index[el]
            pre_res[row][col] = -num

    pre_res = sympy.Matrix(pre_res)
    ratio = pre_res.nullspace()[0]
    ratio *= sympy.lcm([term.q for term in ratio])

    left_half = " + ".join(["{} {}".format(ratio[i], s) for i, s in enumerate(left_half_strings)])
    right_half = " + ".join(["{} {}".format(ratio[i], s) for i, s in enumerate(right_half_strings, len(left_half_strings))])
    return f"{left_half} -> {right_half}"


if __name__ == "__main__":
    pass
