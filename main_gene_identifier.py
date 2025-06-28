# Function to extract open reading frames (ORFs) from a DNA sequence
def find_genes(dna):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    genes = []

    i = 0
    while i < len(dna):
        codon = dna[i:i+3]
        if codon == start_codon:
            j = i + 3
            while j < len(dna):
                stop = dna[j:j+3]
                if stop in stop_codons and (j - i) % 3 == 0:
                    gene = dna[i:j+3]
                    genes.append(gene)
                    break
                j += 3
            i = j
        else:
            i += 1
    return genes


# get sequence input
dna_input = input("enter a DNA sequence (5' to 3'): ")
dna_input = dna_input.upper()  # make sure it's in uppercase

print("scanning...", dna_input)  # debug print

found_genes = find_genes(dna_input)

if len(found_genes) > 0:
    print("genes found:")
    count = 1
    for g in found_genes:
        print("gene", count, ":", g)
        count += 1
else:
    print("no genes found")

