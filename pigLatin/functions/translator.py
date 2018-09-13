# ================================================================= #
#                      PIGLATIN TRANSLATION
# ================================================================= #
def vowel_transformation(word):
    char_list = list(word)
    char_list.append("way")

    return "".join(char_list)


def consonant_transformation(word):
    # takes the first letter and send to last string position

    char_list = list(word)  # split chars into a list
    first_letter = char_list[0]
    char_list.remove(char_list[0])  # removes first char
    char_list.append(first_letter.lower())  # append to end

    char_list.append('ay')

    # and then adds an ay

    return "".join(char_list)


def translatePhrase(phrase):
    phrase = phrase.strip(' ')
    phraseList = phrase.split(" ")
    result = []

    for word in phraseList:

        if word[0].isalpha():
            # Checks if first letter is a vowel
            if word[0] in "aeiouAEIOU":
                result.append(vowel_transformation(word))
            else:
                result.append(consonant_transformation(word))

    return " ".join(result)
