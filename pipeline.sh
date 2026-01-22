#!/bin/bash

# This script automates the Evolution Analysis Pipeline

# 1. Define the Input ID
ACCESSION="SRR13253750"

echo "=================================="
echo "Starting Pipeline for $ACCESSION"
echo "=================================="

# 2. Activate the Python Environment
source venv/bin/activate

# 3. Download Data
echo "[1/3] Downloading Data..."
# This generates SRR13253750_1.fastq
fastq-dump -X 10000 --split-files $ACCESSION

# 4. Run QC
echo "[2/3] Running Quality Control..."
# UPDATE: Added _1 to the filename
INPUT_FILE="${ACCESSION}_1.fastq"

# Check if file exists before running
if [ -f "$INPUT_FILE" ]; then
    python3 filter_quality.py $INPUT_FILE
else
    echo "ERROR: File $INPUT_FILE not found."
    exit 1
fi

# 5. Run Analysis
echo "[3/3] Analyzing Mutations..."
# UPDATE: The python script appends _clean.fasta to the input name
# So SRR..._1.fastq becomes SRR..._1_clean.fasta
CLEAN_FILE="${ACCESSION}_1_clean.fasta"

python3 analyze_mutants.py $CLEAN_FILE > results_${ACCESSION}.txt

echo "Pipeline Complete. Check results_${ACCESSION}.txt"