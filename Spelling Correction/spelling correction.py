"""This is a Levenshtein spelling corrector"""


def corrector_interface():
    """This function implements the interface of the spelling corrector"""
    # Read the dictionary
    dictionary = read_dictionary("/Users/dp/Downloads/IDS 703/ass2/dictionary.txt")
    # Ask the user for a word
    word = input("Enter a word: ")
    # Spell check the word
    closest_word = Levenshtein_spelling_corrector(word, dictionary)
    # Print the closest word
    print("Did you mean {}?".format(closest_word))


# read the dictionary
def read_dictionary(filename):
    dictionary = {}
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            tokens = line.split("\t")
            # considering the computing time and the frequency of vocabulary use
            if int(tokens[1]) > 1000000:
                dictionary[tokens[0]] = tokens[1]
    return dictionary


def Levenshtein_spelling_corrector(word, dictionary):
    """This function returns the word in the dictionary that is closest to the word passed as argument"""
    # Initialize the minimum distance to the maximum possible value
    min_distance = len(word) + len(dictionary)
    # Initialize the closest word to the first word in the dictionary
    closest_word = list(dictionary.keys())[0]
    # Iterate over the words in the dictionary
    for key in dictionary.keys():
        # Compute the distance between the word and the current word in the dictionary
        distance = Levenshtein_distance(word, key)
        # If the distance is smaller than the minimum distance, update the minimum distance and the closest word
        if distance < min_distance:
            min_distance = distance
            closest_word = key
    # Return the closest word
    return closest_word


def Levenshtein_distance(word1, word2):
    """This function returns the Levenshtein distance between two words"""
    # Initialize the matrix
    matrix = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    # Initialize the first row
    for i in range(len(word2) + 1):
        matrix[0][i] = i
    # Initialize the first column
    for i in range(len(word1) + 1):
        matrix[i][0] = i
    # Iterate over the rows
    for i in range(1, len(word1) + 1):
        # Iterate over the columns
        for j in range(1, len(word2) + 1):
            # Compute the cost
            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1
            # Update the matrix
            matrix[i][j] = min(
                matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost
            )
    # Return the last element of the matrix
    return matrix[-1][-1]


if __name__ == "__main__":
    corrector_interface()
