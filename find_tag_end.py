import sys


def check_sequence(gene_name, gene_sequence):
    if gene_name is None:
        assert len(gene_sequence) == 0
    else:
        assert len(gene_sequence) == 3
        if gene_sequence == 'TAG':
            print('Gene "%s" ends with "TAG"' % gene_name)


gene_name = None
gene_sequence = ''
with open(sys.argv[1]) as infile:
    for line in infile.readlines():
        if line[0] == '>':
            check_sequence(gene_name, gene_sequence)
            gene_name = line[1:].strip()
            gene_sequence = ''
        else:
            gene_sequence += line.strip()
            gene_sequence = gene_sequence[-3:]
check_sequence(gene_name, gene_sequence)
