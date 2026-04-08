
def predict_mass(seq):
    mass = 0
    amino_acid_mass = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
    }
    for amino_acid in seq:
        if amino_acid not in amino_acid_mass:
            print('Anino acid does not exist')
            mass = 0
            break
        else:
            mass += amino_acid_mass[amino_acid]
    return mass

#example
seq = 'EVNCAWHLIDGPKTMYSFRQ'
protein_mass = predict_mass(seq)
print(f'Protein mass is {protein_mass:.2f}')