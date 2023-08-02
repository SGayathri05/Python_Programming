def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    c = set(a).union(b)
    return sorted(c)
