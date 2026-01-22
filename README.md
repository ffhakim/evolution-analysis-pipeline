# Non-Natural Amino Acid Analysis Pipeline

## Overview
This pipeline automates the analysis of NGS data for the Continuous Evolution project.
It filters low-quality reads and detects the incorporation of non-natural amino acids (represented as 'Z').

## Requirements
- Python 3.10+
- Biopython
- SRA-Toolkit (for downloading data)

## Usage
1. Activate the environment:
   `source venv/bin/activate`

2. Run the pipeline with a specific Accession ID:
   `./pipeline.sh`

## Output
- `results_ID.txt`: Protein translation sequences.
- `results_ID.png`: Graph showing success rates.