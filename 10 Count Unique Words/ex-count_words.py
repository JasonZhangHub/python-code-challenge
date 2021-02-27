from collections import Counter
import re

def count_words(file):
    f = open(file, "r")
    words = re.findall(r"[0-9a-zA-Z-']+", f.read())
    words = [i.lower() for i in words]
    
    print('Total number of words: {count}'.format(count=len(words)))
    
    counts = Counter()
    for i in words:
        counts[i] += 1
    
    print('TOP 20 words\tCount')
    for k, v in counts.most_common(20):
        print('{}\t\t{}'.format(k, v))
    
    f.close()

file = 'shakespeare.txt'
count_words(file)