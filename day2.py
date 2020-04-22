
def sockMerchant(n, ar):
    arset = set(ar)
    counts = []
    for i in arset:
        v=0
        for j in ar:
            if j == i:
                v+=1
        counts.append(v)

    pairs = 0
    for i in counts:
        y = i//2
        pairs+=y
    return pairs
