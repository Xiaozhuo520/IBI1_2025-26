file = open('Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

def find_orfs(seq):
    orfs = []
    starts = []
    end_list = ['TAA', 'TAG', 'TGA']

    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            starts.append(i)

    for start in starts:
        i = start
        orf = ''
        while True:
            orf += seq[i:i+3]
            if seq[i:i+3] in end_list:
                orfs.append(orf)
                break
            i += 3
            if i >= len(seq) - 2:
                break
    return orfs

file = open('Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

genes = {}
for line in file:
    line = line.rstrip('\n')
    if line[0] == '>':
        gene = ''
        for i in line:
            if i == ' ':
                break
            gene += i
        genes[gene] = ''
    elif line:
        genes[gene] += line

genes_with_end_codons = {}
for gene in genes:
    orfs = find_orfs(genes[gene])
    if orfs:
        genes_with_end_codons[gene] = set()
        for orf in orfs:
            genes_with_end_codons[gene].add(orf[-3:])

print(genes_with_end_codons)

with open('Practical7/stop_genes.fa', 'w') as file:
    for gene in genes_with_end_codons:
        file.write(f'{gene};{','.join(genes_with_end_codons[gene])}\n')
        i = 0
        while i <= len(genes[gene]) - 150:
            file.write(genes[gene][i:i+150] + '\n')
            i += 150
        if genes[gene][i:]:
            file.write(genes[gene][i:] + '\n')
        

            