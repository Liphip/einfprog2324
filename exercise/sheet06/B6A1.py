import random

def is_valid(w,k):
    """
    Checks if the input string w consists of blocks of digits,
    seperated by commas. The number of digits in each block should
    be k.

    Parameters
    ----------
    w : str
        The input string to check.
    k : int
        The number of digits in each block.

    Returns
    -------
    bool
        True if the string is valid, False otherwise.
    """
    # Split w into blocks.
    w_blocks = w.split(",")

    # Check if each block has k digits.
    for block in w_blocks:
        if len(block) != k:
            return False

    return True

def length(w,k):
    """
    Calculates the number of k-digit blocks in the input string w.

    Parameters
    ----------
    w : str
        The input for which to calculate the number of k-digit blocks.
    k : int
        The number of digits in each block.

    Returns
    -------
    int
        The number of k-digit blocks in w.
    """
    # Split w into blocks.
    w_blocks = w.split(",")

    # Count the number of blocks with k digits.
    num_k_digit_blocks = 0
    for block in w_blocks:
        if len(block) == k:
            num_k_digit_blocks += 1

    return num_k_digit_blocks

def replace(w,i,a):
    """
    Replaces the i-th character in the input string w with the character a.

    Parameters
    ----------
    w : str
        The input string to modify.
    i : int
        The index of the character to replace.
    a : str
        The character to replace the i-th character with.

    Returns
    -------
    str
        The modified string.
    """
    # Convert w to a list, replace the i-th character with a, and convert
    # the list back to a string.
    w_list = list(w)
    w_list[i] = a
    return "".join(w_list)

def swap(w,i,j):
    """
    Swaps the i-th and j-th character in the input string w.

    Parameters
    ----------
    w : str
        The input string to modify.
    i : int
        The index of the first character to swap.
    j : int
        The index of the second character to swap.

    Returns
    -------
    str
        The modified string.
    """
    # Convert w to a list, swap the i-th and j-th character, and convert
    # the list back to a string.
    w_list = list(w)
    w_list[i], w_list[j] = w_list[j], w_list[i]
    return "".join(w_list)

def numswap(w,i,j,k):
    """
    Swaps the i-th and j-th k-digit blocks in the input string w.

    Parameters
    ----------
    w : str
        The input string to modify.
    i : int
        The index of the first block to swap.
    j : int
        The index of the second block to swap.
    k : int
        The number of digits in each block.

    Returns
    -------
    str
        The modified string.
    """
    # Split w into blocks.
    w_blocks = w.split(",")

    # Swap the i-th and j-th block.
    w_blocks[i], w_blocks[j] = w_blocks[j], w_blocks[i]

    # Convert the list of blocks back to a string.
    return ",".join(w_blocks)

def sort(w,k,f):
    """
    Sorts the k-digit blocks in the input string w based on the function f.
    The algorithm used is bubble sort.

    Parameters
    ----------
    w : str
        The input string to modify.
    k : int
        The number of digits in each block.
    f : function
        The function to use for sorting. Must take two integers as input and
        return a boolean value. If f(a,b) is True, then a comes before b in
        the sorted list.

    Returns
    -------
    str
        The modified string.
    """
    # Split w into blocks.
    w_blocks = w.split(",")
    num_blocks = len(w_blocks)

    # Sort the blocks using bubble sort.
    for i in range(num_blocks):
        for j in range(num_blocks - i - 1):
            if f(int(w_blocks[j]), int(w_blocks[j+1])):
                w_blocks[j], w_blocks[j+1] = w_blocks[j+1], w_blocks[j]
    
    # Convert the list of blocks back to a string.
    return ",".join(w_blocks)

def main():
    w = input("Please enter a string of characters: ")
    k = int(input("Please enter a number of digits: "))
    print("")

    # Check if w is valid.
    if not is_valid(w,k):
        print("Invalid input.")
        return

    # Print the number of k-digit blocks in w.
    print("Number of k-digit blocks:", length(w,k))

    # Print the string with the i-th character replaced by a.
    i = random.randint(0, len(w) - 1)
    a = str(random.randint(0, 9))
    print(f"String with the {i}-th character replaced by {a}:", replace(w,i,a))

    # Print the string with the i-th and j-th character swapped.
    i = random.randint(0, len(w) - 1)
    j = random.randint(0, len(w) - 1)
    print(f"String with the {i}-th and {j}-th character swapped:", swap(w,i,j))

    # Print the string with the i-th and j-th k-digit blocks swapped.
    i = random.randint(0, length(w,k) - 1)
    j = random.randint(0, length(w,k) - 1)
    print(f"String with the {i}-th and {j}-th {k}-digit blocks swapped:", numswap(w,i,j,k))

    # Print the string with the k-digit blocks sorted using different functions.
    print("String with the k-digit blocks sorted using different functions:")
    print("\t'>':", sort(w,k,lambda a,b: a > b))
    print("\t'<':", sort(w,k,lambda a,b: a < b))
    print("\t'digitsum':", sort(w,k,lambda a,b: sum(map(int, str(a))) > sum(map(int, str(b)))))
    print("\t'delta':", sort(w,k,lambda a,b: abs(a - b) > 0))
    print("\t'random':", sort(w,k,lambda a,b: random.randint(0, 9) > random.randint(0, 9)))

if __name__ == "__main__":
    main()