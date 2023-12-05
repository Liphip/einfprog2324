# Philip Laskowicz


def modify_str(string: str, func: callable) -> str:
    """
    Applies the given function to the given string.

    Parameters
    ----------
    string : str
        The string to modify.
    func : callable
        The function to apply to the string.

    Returns
    -------
    str
        The modified string.
    """
    # Apply the given function to the given string and return the result.
    return func(string)


def main():
    # Get input string from user.
    input_str = input("Please enter a string: ")

    # Functions to be applied to the input string.
    functions = [len, bool]

    # Apply the functions to the input string.
    for func in functions:
        print(modify_str(input_str, func))


if __name__ == "__main__":
    main()
