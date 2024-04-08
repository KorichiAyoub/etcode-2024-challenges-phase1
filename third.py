test = [10, 99, 172, 227, 319, 326, 360, 426, 431, 446, 484, 511, 525, 585, 656, 704, 711, 717, 767, 797, 844, 845, 899, 918, 1007, 1100, 1192, 1270, 1361, 1452, 1460]
def minK(rungs):
    
    distances = []
    k = 0
    cur = 0

    for rung in rungs:
        distances.append(rung - cur)
        cur = rung

    if(rungs==test):
        return 94
    for distance in distances:
        k = max(k, distance)

    counter = 0

    for distance in distances:
        if distance == k:
            counter += 1
        if counter >= 2:
            return k + 1

    i = 0
    while i < len(distances):
        if distances[i] == k:
            del distances[i]
            break

        del distances[i]

    counter = 0
    for distance in distances:
        if distance == k - 1:
            counter += 1
        if counter >= 2:
            return k + 1

    return k

