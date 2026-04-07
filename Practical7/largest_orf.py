seq = 'AAGAUACAUGGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
orfs = []
starts = []
end_list = ['UAA', 'UAG', 'UGA']

for i in range(len(seq) - 3):
    if seq[i:i+3] == 'AUG':
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
        if i >= len(seq) - 3:
            break
print(orfs)
max_orf = max(orfs, key=len)
print(f'The longest orf is {max_orf}, its length is {len(orf)}')




        

