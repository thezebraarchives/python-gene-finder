# python-gene-finder
This is a simple Python program that finds possible genes in a 5' to 3' DNA sequence by locating open reading frames (ORFs). An ORF starts with a start codon (ATG) and ends with a stop codon (TAA, TAG, or TGA), and must be in frame (the length between start and stop codons must be a multiple of 3).

## what it does:

- Asks the user to input a DNA sequence (A, T, C, G).
- Finds gene regions that:
  - Start with the codon `"ATG"`
  - End with any of the stop codons: `"TAA"`, `"TAG"`, or `"TGA"`
  - Are in-frame (the number of nucleotides between start and stop is a multiple of 3)
- Outputs all detected gene sequences.

## Example Usage

python3 main_gene_identifier.py

Enter a DNA sequence: ATGAAATAGATGTTTTAA

Genes found:
ATGAAATAG
ATGTTTTAA
