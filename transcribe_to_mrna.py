"""
Transcribe to mRNA by Timothy Eden
Date Last Modified: June 27, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/McZF4JRhPus5DtRA4
"""


def dna_to_rna(dna):
    rna = ''
    for base in dna:
        if base == 'A':
            rna += 'U'
        elif base == 'T':
            rna += 'A'
        elif base == 'G':
            rna += 'C'
        elif base == 'C':
            rna += 'G'
    return rna


def main():
    assert dna_to_rna("GCGTAC") == "CGCAUG"
    assert dna_to_rna("ATTAGCGCGATATACGCGTAC") == "UAAUCGCGCUAUAUGCGCAUG"
    assert dna_to_rna("CAGTATGCTGCAT") == "GUCAUACGACGUA"
    assert dna_to_rna("CGATATA") == "GCUAUAU"


if __name__ == '__main__':
    main()
