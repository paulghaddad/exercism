DNA_TO_RNA = {
    'C': 'G',
    'G': 'C',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand):
    if not dna_strand:
        return ''

    rna_strand = [DNA_TO_RNA[nucleotide] for nucleotide in dna_strand]

    return ''.join(rna_strand)
