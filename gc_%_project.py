#%%
# gc precentage project
seq = input('enter your dna seq:').upper()
def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    total = len(seq)
    gc_percentage = ((g + c)/ total ) * 100
    return gc_percentage
result = gc_content(seq)
print('gc content', result)
# %%
#all nucleotide counts + GC% in one result
seq = input("enter your seq:").upper()
def dna_analyzer(seq):
    g = seq.count('G')
    c = seq.count('C')
    t = seq.count('T')
    a = seq.count('A')
    total = len(seq)
    gc_percent = ((g + c) / total) * 100
    return a, t , g, c, gc_percent#mutiple return
result = dna_analyzer(seq)#i forgot this
print("A:", result[0])
print('T:', result[1])
print('G:', result[2])
print ('c:', result[3])
print("gc%:", result[4])
# %%
