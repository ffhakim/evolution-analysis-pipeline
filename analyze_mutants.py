import sys
from Bio import SeqIO
from Bio.Seq import Seq

# CHECK ARGS
if len(sys.argv) < 2:
    print("Usage: python3 analyze_mutants.py <fasta_file>")
    sys.exit(1)

filename = sys.argv[1] # Take filename from the pipeline
print(f"--- Analyzing {filename} ---\n")

for record in SeqIO.parse(filename, "fasta"):
    
    # 1. CLEAN THE DATA
    # Math: If length is 53, 53 % 3 = 2. We substract 2 to get 51.
    remainder = len(record.seq) % 3
    if remainder > 0:
        # Slice off the extra letters at the end
        clean_seq = record.seq[: -remainder]
    else:
        clean_seq = record.seq

    # 2. TRANSLATE
    # We first translate to standard protein (Stops will be '*')
    standard_protein = clean_seq.translate()
    
    # 3. APPLY "NON-NATURAL" LOGIC (The PhD Logic)
    # We want to check: Was that '*' actually a 'TAG' (Amber)?
    
    final_protein = ""
    
    # We loop through the PROTEIN and the DNA simultaneously
    for i in range(len(standard_protein)):
        amino_acid = standard_protein[i]
        
        # Calculate which 3 DNA letters correspond to this amino acid
        codon_start = i * 3
        codon = clean_seq[codon_start : codon_start + 3]
        
        # THE LOGIC CHECK
        if amino_acid == "*":
            if codon == "TAG":
                # This is our target! Suppress the stop.
                final_protein += "Z" # Z = Non-Natural AA
            else:
                # This is a real stop (TAA or TGA)
                final_protein += "*" 
        else:
            final_protein += amino_acid

    # 4. REPORT
    print(f"Strain: {record.id}")
    print(f"DNA   : {clean_seq}")
    print(f"Result: {final_protein}")
    
    if "Z" in final_protein:
        print(">>> SUCCESS: Non-natural amino acid incorporated!")
    elif "*" in final_protein:
        print(">>> NOTE: Protein truncated by standard stop.")
        
    print("-" * 30)