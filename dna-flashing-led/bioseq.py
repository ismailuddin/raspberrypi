def parse_FASTA(filename):
    """Parse all entries in FASTA file into a dictionary"""

    import collections

    file = open(filename, 'r')
    entry_id = ''
    sequence = ''
    entries = collections.OrderedDict()
    for line in file:
        if line[0] == '>':
            sequence = ''
            entry_id = ''
            s = line[1:].rstrip()
            entry_id += s
        elif line[0] != '>':
            d = line.rstrip().upper()
            sequence += d
            entries[entry_id] = sequence
        elif line == '':
            file.close()
    return entries