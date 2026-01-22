# The Genetic Code Dictionary (RNA -> Amino Acid)
codon_table = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'Z', # Stop codons marked as '_'
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
}

# Your RNA Sequence (from previous task)
rna_sequence = "AGCUUUUCAUUCUGACUGCAAUAGGCAAUAUGUCUCUGUGGAUUAAAAAAGAGUGUCGAUAGCAGC"

protein_sequence = ""

# THE RIBOSOME LOOP
# We step through the sequence 3 letters at a time
# range(start, stop, step_size)
for i in range(0, len(rna_sequence), 3):
    # Slice the string to get the codon (e.g., "AGC")
    codon = rna_sequence[i:i+3]
    
    # Check if the chunk is actually 3 letters (to avoid errors at the end)
    if len(codon) == 3:
        amino_acid = codon_table[codon]
        protein_sequence += amino_acid

print("RNA Sequence:", rna_sequence)
print("Protein Seq: ", protein_sequence)