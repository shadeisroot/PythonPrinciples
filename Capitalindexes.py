def capital_indexes(d):
    return [i for i, c in enumerate(d) if c.isupper()]
capital_indexes("HeLlO")

