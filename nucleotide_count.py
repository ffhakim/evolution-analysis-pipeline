# My first bioinformatics script
# DNA sequence from a hypothetical experiment

sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGGATTAAAAAAGAGTGTCGATAGCAGC"

# Count the nucleotides
count_a = sequence.count('A')
count_c = sequence.count('C')
count_g = sequence.count('G')
count_t = sequence.count('T')

# Print the results
print("Sequence Length:", len(sequence))
print("Adenine (A):", count_a)
print("Cytosine (C):", count_c)
print("Guanine (G):", count_g)
print("Thymine (T):", count_t)


# TRANSCRIPTION: Convert DNA to RNA
# Replace every 'T' with 'U'
rna_sequence = sequence.replace('T', 'U')

print("-" * 20) # Prints a divider line
print("Original DNA:", sequence)
print("Transcribed RNA", rna_sequence)

# Check if it worked: There should be NO 'T' in the RNA.
if 'T' not in rna_sequence:
    print("SUCCESS: Transcription complete.")
else:
    print("ERROR: Thymine found in RNA.")