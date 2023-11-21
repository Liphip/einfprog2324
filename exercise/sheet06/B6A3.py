def is_in(tuple_1, tuple_2):
    """
    Checks if tuple_1 and tuple_2 have the first min(m, n) elements in common,
    where m and n are the lengths of tuple_1 and tuple_2 respectively.

    Parameters
    ----------
    tuple_1 : tuple
        The first tuple.
    tuple_2 : tuple
        The second tuple.

    Returns
    -------
    bool
        True if tuple_1 and tuple_2 have the first min(m, n) elements in common,
        where m and n are the lengths of tuple_1 and tuple_2 respectively.
        False otherwise.
    """
    # Get the length of the shorter tuple.
    min_len = min(len(tuple_1), len(tuple_2))

    # Check if the first min_len elements of tuple_1 and tuple_2 are equal.
    for i in range(min_len):
        if tuple_1[i] != tuple_2[i]:
            return False

    return True

def merge(tuple_1, tuple_2):
    """
    Merges the two input tuples into one tuple of length m + n, where m and n
    are the lengths of tuple_1 and tuple_2 respectively.

    Parameters
    ----------
    tuple_1 : tuple
        The first tuple.
    tuple_2 : tuple
        The second tuple.

    Returns
    -------
    tuple
        The merged tuple.
    """
    # Merge the two tuples.
    merged_tuple = tuple_1 + tuple_2

    return merged_tuple

def subtuples(tuple):
    """
    Prints all 1- and 2-element subtuples of the input tuple to the console.

    Parameters
    ----------
    tuple : tuple
        The input tuple.
    
    Returns
    -------
    None
    """
    # Print all 1-element subtuples.
    for i in range(len(tuple)):
        print(tuple[i])

    # Print all 2-element subtuples.
    for i in range(len(tuple) - 1):
        for j in range(i + 1, len(tuple)):
            print(tuple[i], tuple[j])

def main():
    tuple_1 = (1, 2, 3, 4, 5)
    tuple_2 = (1, 2, 3, 4, 5, 6, 7)
    tuple_3 = (6, 7, 8, 9, 10)

    print("tuple_1:", tuple_1)
    print("tuple_2:", tuple_2)
    print("tuple_3:", tuple_3)
    print("")

    print("is_in(tuple_1, tuple_2):", is_in(tuple_1, tuple_2))
    print("is_in(tuple_1, tuple_3):", is_in(tuple_1, tuple_3))
    print("")

    print("merge(tuple_1, tuple_2):", merge(tuple_1, tuple_2))
    print("merge(tuple_1, tuple_3):", merge(tuple_1, tuple_3))
    print("")

    print("subtuples(tuple_1):")
    subtuples(tuple_1)
    print("")
    print("subtuples(tuple_2):")
    subtuples(tuple_2)
    print("")
    print("subtuples(tuple_3):")
    subtuples(tuple_3)
    print("")

if __name__ == "__main__":
    main()