def to_rna(dna_strand):
    DNAtoRNA = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
    return "".join(DNAtoRNA[x] for x in dna_strand if x in DNAtoRNA)
