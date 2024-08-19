from collections import defaultdict
def record_indices(col, indices):
    for element in enumerate (col):
        print (indices[element[0]])
        indices[element[0]] = element
    print (indices)
names = ["Patrick", "Steven", "Ben", "Karl"]
indices = defaultdict(lambda: 0)
record_indices (names, indices)