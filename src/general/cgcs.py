def calculate_cgcs(*components):
    components = [max(0.0, min(1.0, float(c))) for c in components]

    if not components:
        return 0.0

    product = 1.0
    for c in components:
        product *= c

    return product ** (1.0 / len(components))
