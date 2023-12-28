# Philip Lasowicz

if __name__ == "__main__":
    # Please do not name your variables like this. Use camelCase or snake_case instead of PascalCase.
    # Also, dont use single letter variables. Use descriptive names instead.
    # Had to be done like this due to the exercise.
    w = input("Enter a string: ").replace(" ", "")
    
    # Count the number of occurences of each character.
    counts_list = []
    added_chars = []
    for char in w:
        if char in added_chars:
            continue
        added_chars.append(char)
        counts_list.append((char, w.count(char)))
    
    # Please do not use print statements like this. Use f-strings with a descriptive output instead.
    print(counts_list)