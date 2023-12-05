# Philip Laskowicz


def tupel_konv(string: str) -> tuple:
    """
    Checks if the given string has two commas.
    If it does, it returns the string as a 3-tuple.
    Otherwise it returns None.

    Parameters
    ----------
    string : str
        The string to check.

    Returns
    -------
    tuple
        The string as a 3-tuple if it has three commas, None otherwise.
    """
    # Check if the string has three commas.
    if string.count(",") != 2:
        return None

    # Split the string at the commas.
    split_string = string.split(",")

    # Return the string as a 3-tuple.
    return tuple(split_string)


def tupel_perm(tupel: tuple) -> None:
    """
    Checks if the given tuple has the three elements.
    If it does, it prints all permutations of the tuple.

    Parameters
    ----------
    tupel : tuple
        The tuple to check.

    Returns
    -------
    None
    """
    # TODO: Clarify if the function should print all permutations or just all distinct permutations.
    #       Since it was not specified, I will assume that the function should print all permutations.

    # Recursive function to print all permutations of the tuple.
    def print_permutations(
        tupel: tuple, current_perm: tuple, remaining_elements: tuple = None
    ) -> None:
        """
        Prints all permutations of the given tuple.

        Parameters
        ----------
        tupel : tuple
            The tuple to print permutations of.
        current_perm : tuple
            The current permutation.
        remaining_elements : tuple
            The remaining elements to be added to the current permutation.
            If None, the function will assume that all elements are remaining.

        Returns
        -------
        None
        """
        # If remaining_elements is None, assume all elements are remaining.
        if remaining_elements is None:
            remaining_elements = tupel

        # If the current permutation has the same length as the input tuple, print it.
        if len(current_perm) == len(tupel):
            print(current_perm)
            return

        # For each element in the remaining elements, add it to the current permutation and call the function recursively.
        for element in remaining_elements:
            # Remove the current element from the remaining elements.
            remaining_elements_copy = list(remaining_elements)
            remaining_elements_copy.remove(element)

            # Add the current element to the current permutation.
            current_perm_copy = list(current_perm)
            current_perm_copy.append(element)

            # Call the function recursively.
            print_permutations(
                tupel, tuple(current_perm_copy), tuple(remaining_elements_copy)
            )

    # Check if the tuple has three elements.
    if len(tupel) != 3:
        return

    # Print all permutations of the tuple.
    print_permutations(tupel, ())


def main():
    # Get input string from user.
    input_str = input("Please enter a string: ")

    # Check if the input string has three commas.
    tupel = tupel_konv(input_str)

    # Print the tuple.
    print(f"Tuple: {tupel}")

    # Print all permutations of the tuple.
    tupel_perm(tupel)


if __name__ == "__main__":
    main()
