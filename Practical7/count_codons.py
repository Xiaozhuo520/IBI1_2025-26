import matplotlib.pyplot as plt

def find_specific_orfs(seq,end_codon):
    orfs = []
    starts = []
    end_codons = ('TAA', 'TAG', 'TGA')
    specific_orfs = []

    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            starts.append(i)

    for start in starts:
        i = start
        orf = ''
        while True:
            orf += seq[i:i+3]
            if seq[i:i+3] in end_codons:
                    orfs.append(orf)
                    break
            i += 3
            if i >= len(seq) - 2:
                break
    for orf in orfs:
        if orf[-3:] == end_codon:
            specific_orfs.append(orf)

    return specific_orfs

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

while True:
    end_codon = input('Please input one of three possible stop codons (TAA, TAG, TGA): ')
    if end_codon not in ('TAA', 'TAG', 'TGA'):
        print('Incorrect codon, please try again')
    else:
        break

longest_specific_orfs = []
for gene in genes:
    specific_orfs = find_specific_orfs(genes[gene], end_codon)
    if specific_orfs:
        longest_orf = max(specific_orfs, key=len)
        longest_specific_orfs.append(longest_orf)

counter = {}
for orf in longest_specific_orfs:
    upstream_orfs = orf[:-3]
    upstream_codons = [upstream_orfs[i:i+3] for i in range(0, len(upstream_orfs), 3)]
    for codon in upstream_codons:
        if codon in counter:
            counter[codon] += 1
        else:
            counter[codon] = 1

counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

labels = list(counter.keys())
sizes = list(counter.values())
plt.close('all')

plt.figure(figsize=(12, 12))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 8})
plt.title('Codon Frequencies')
plt.tight_layout()
plt.savefig('codon_chart.png', dpi=300, bbox_inches='tight')
plt.show()