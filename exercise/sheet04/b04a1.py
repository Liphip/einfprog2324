# Please do not name your variables like this. Use camelCase or snake_case instead of PascalCase.
# Also, dont use single letter variables. Use descriptive names instead.
# Had to be done like this due to the exercise.
w = input("Please enter a string of characters: ")

# Split w into words.
w_words = w.split()

# Get highest number of consecutive consonants in w.
word_map = {}
for word in w_words:
    word_map[word] = 0

    consecutive_consonants = 0
    for char in word.upper():
        if char not in "AEIOU":
            consecutive_consonants += 1
        else:
            consecutive_consonants = 0

        if consecutive_consonants > word_map[word]:
            word_map[word] = consecutive_consonants

    print(word, word_map[word])