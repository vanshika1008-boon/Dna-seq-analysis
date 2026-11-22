#%%
# computing percentage
seq = input('enter your seq:').upper()
def gc_content(seq):
    gc_count = 0

    for base in seq:
        if base == "G" or base == "C":
            gc_count += 1
    percentage = (gc_count/ len(seq))*100
    return percentage
gc = gc_content(seq)
print("gc% =", gc)
# %%
# project-1[reverse complement as function]
seq = input('enter your seq:').upper()
def rev_comp(seq):
    rev = seq[::-1]
    comp = ""

    for base in rev:
        if base == "A":
            comp += "T"
        elif base == "G":
            comp += "C"
        elif base == "T":
            comp += "A"
        elif base == "C":
            comp += "G"
        else:
            comp += "N"
    return comp
print('reverse complement seq:', rev_comp(seq))            

# %%
# project-2 [translate DNA to Protein]
seq = input('enter your seq:').upper()
def translate_dna(seq):
    codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            protein += codon_table.get(codon, "X")
    return protein
print('protein seq =',translate_dna(seq))
# %%
# assignment
seq = input('enter your dna seq:').upper()
def bases_count(seq):
    count_a = 0
    count_t = 0
    count_c = 0
    count_g = 0
    
    for base in seq:
        if base == "A":
            count_a += 1
        elif base == "T":
            count_t += 1
        elif base == "C":
            count_c += 1
        elif base == "G":
            count_g += 1
        else: 
            pass #ignore invalid characters
    result = {
        "A": count_a, "T": count_t, "C": count_c, "G": count_g
    }
    return result
print(bases_count(seq))
# %%
