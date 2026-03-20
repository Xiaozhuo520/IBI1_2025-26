import matplotlib.pyplot as plt

genes = {'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3, 'ESR1':10.7}
genes['MYC'] = 1.16

gene = 'TP53' # user input

if gene in genes:
    print(genes[gene])
else:
    print('Gene does not exist')

plt.bar(genes.keys(), genes.values())
plt.title("Gene Expression Levels")
plt.xlabel("Genes")
plt.ylabel("Expression Value")
plt.show()

average_expression = sum(genes.values()) / len(genes.values())

print(f"Average gene expression level: {average_expression:.2f}")
