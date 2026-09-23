def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    counts={}
    if len(samples) == 0:
        return samples
    for i in samples:
        counts[i] = counts.get(i, 0) + 1

    result = []

    for v in sorted(counts):
        probability = counts[v] / len(samples)
        result.append((v, probability))

    return result