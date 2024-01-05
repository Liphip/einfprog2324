def get_max_word(words: list, key: function = len) -> str:
    """
    Returns the maximum word in the given list of words according to the given key function.
    Default key function is len.

    Parameters:
    ----------
        words (list): List of words.
        key (function): Key function.
            default: len

    Returns:
    -------
        str: The maximum word in the given list of words according to the given key function.
    """
    return max(words, key=key)


def filter_words(words: list, filter: function) -> list:
    """
    Returns a list of words filtered by the given filter function.

    Parameters:
    ----------
        words (list): List of words.
        filter (function): Filter function.
            type: (str)->bool (returns True if the word should be included in the result list)

    Returns:
    -------
        list: List of words filtered by the given filter function.
    """
    return list(filter(words))


if __name__ == "__main__":
    w = input("Enter a list of words: ")
    wordlist = w.split()

    # Get longest word in w
    longest_word = get_max_word(wordlist)

    # Filter words starting with upper case
    upper_words = filter_words(wordlist, lambda x: x[0].isupper())

    # Filter words starting with lower case
    lower_words = filter_words(wordlist, lambda x: x[0].islower())

    # Print results

    # Number of words
    print(len(wordlist))

    # Longest word
    print(longest_word)

    # Length of longest word
    print(len(longest_word))

    # Words starting with upper case
    print(upper_words)

    # Words starting with lower case
    print(lower_words)

    # All words
    print(wordlist)
