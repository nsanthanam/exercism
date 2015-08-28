import re

def word_count(phrase=''):
    counts = {}
    
    for word in re.split('\s+', phrase):
        counts[word] = counts[word] + 1 if word in counts else 1

    return counts