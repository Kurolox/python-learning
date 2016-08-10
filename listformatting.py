def organize(list):
    return ((", ".join(list[:-1])) + " and " + list[-1])


print(organize(["alpha", "beta", "gamma", "delta", "delta", "delta", "delta", "delta", "delta", "delta", "delta"]))
