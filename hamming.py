def distance(seq1, seq2):
    
    if len(seq1) is not len(seq2):
        hamming_dist = 0
    else:
        mismatches = [a for a, b in zip(seq1, seq2) if a is not b]
        hamming_dist = len(mismatches)
    return hamming_dist