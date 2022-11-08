def f9(pairs):
    return [{"sum": p[0] + p[1],
             "prod": p[0]*p[1],
             "pow": p[0]**p[1]} for p in pairs]


print(f9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
