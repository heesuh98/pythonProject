a = 'GGTTTAACGGAAATTATGATCCACTCAACTAATGCGTAGTAGGGACCTAATTAGAGGAACTTTCCAGACTTATCCAGTGCTGCCATCCTTTTGCTATCCCCGATCGCTTGCCATGAGCCAAATTGCCGGGATAGACAAGATGAACGCGGGATCGCGTCTATTTCGATGATGGCCCAAACCAAAGCAAGCCAAATTCTACCTTAATTGCCCTACCCCGATATAACCCATTAACTAGACTGGTGTACTCCGGCCGCTGCGCTTAGGCACGTTCGACCACAGGCCGCTCCTGGGGCATGTACACCGCTTGCTTGGTATTTTACCCTACTCCTGCGCAGGTGCAATGATCAACGGTCCTAGAGTAAACGTAGCCACGTGTGTCGTTGGACTCCATAGATCATCCCAGCTATACTCATCAGAATTTTTAGGGGTTAGTTCAGTAGACAGAGAGCAGACATTAGCTTTTCGACGATCACCACTCAATGGTTTCGACCCGCGGGGTCGGGAGGGGGACCCGCGCGAAATATCTTGCAAAACGCTCCTTAGCGGTTATGGGTACCATTATCACCAATCGGGACTCATCGCTGTAACCACATCTTGCCACCGGGCAGTATCGTACGATCTATCCTTGACACCATACACTTCAGTCGCTTAACAGCAGAACTTTTCATGTTGGCCCGATACTACTGTGGTTGGTTCCCACATACAGACGGAGTGAAGTGGAACCGAAAACCATCATCTAATGCCGTATGGCATTGAACCCCCTTCATTATCAAACCGTCGATTCGGGGGAGGGATCGTGGGCAGCACCCCTCCCGGCATATTCCGCACGGTTATTCAGGGGCCAATGAAGGCGAAGTTGGCATCCACTACCTGTAGTGCCTATAGGATACCCCTCTAATGTCGGCCCGGACCGGCAGTGCAAGAATGTGATTCGAGTTCCAGCGAAGATCGGTGAGGGCAAGATCCAT'
re_a = a[::-1]

result = re_a.replace('A','t'). replace('T','a'). replace('C','g'). replace('G','c').upper()

print(result)

