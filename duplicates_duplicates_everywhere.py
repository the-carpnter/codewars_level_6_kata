def remove_duplicate_ids(d):
    x = set()
    new = {i:[] for i in d}
    for key in sorted(list(d.keys()), key = int, reverse = True):
        for el in d[key]:
            if el not in x:
                x.add(el)
                new[key] += [el]
    return new
