import sys
from Bio import SeqIO

# Check if the user actually provided a filename
if len(sys.argv) < 2:
    print("Usage: python3 filter_quality.py <your_fastq_file>")
    sys.exit(1) # Exit with error code

# The first argument (index 1) is the filename you type in the terminal
input_file = sys.argv[1]

# Let's auto-name the output (e.g., input.fastq -> input_clean.fasta)
output_file = input_file.replace(".fastq", "") + "_clean.fasta"

print(f"Processing: {input_file}")
print(f"Output to : {output_file}")

print(f"Filtering {input_file}...")

# We will create a list to hold only the good sequences
good_reads = []

# Parse the FASTQ file
for record in SeqIO.parse(input_file, "fastq"):
    
    # Biopython stores quality scores as a list of numbers in record.letter_annotations
    # Let's get the average score of this read
    quality_scores = record.letter_annotations["phred_quality"]
    
    # Calculate Average AND Minimum
    avg_score = sum(quality_scores) / len(quality_scores)
    min_score = min(quality_scores) # The lowest score in the list
    
    print(f"ID: {record.id} | Avg: {avg_score:.2f} | Min: {min_score}")
    
    # NEW RULE: The Chain is only as strong as its weakest link.
    # If any base is below Q20 (99% accuracy), trash the whole read.
    if min_score >= 20:
        print(" -> KEEP")
        good_reads.append(record)
    else:
        print(" -> TRASH (Contains low quality region)")

print("-" * 20)
print(f"Original reads: 3")
print(f"Good reads    : {len(good_reads)}")

# Save the good ones to a new FASTA file
if good_reads:
    SeqIO.write(good_reads, output_file, "fasta")
    print(f"Saved clean sequences to {output_file}")