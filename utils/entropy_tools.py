from collections import Counter
import math

def entropy(s):
    probs = [v / len(s) for v in Counter(s).values()]
    return -sum(p * math.log2(p) for p in probs)
