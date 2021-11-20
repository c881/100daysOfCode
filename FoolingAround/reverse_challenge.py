import re


def remove_punctuation(words):
    """Helper function to return a string, removing all punctuation and spaces"""
    return re.sub('\W+', '', words)


def is_palindrome(words):
    """Palindrome are case insensitive, so Radar and radar are valid."""
    clean_words = remove_punctuation(words.lower())
    # Opt.1
    return clean_words == ''.join(reversed(clean_words))

    # Opt.2
    # for char1, char2 in zip(clean_words, reversed(clean_words)):
    #     print(char1, char2)
    #     if char1 != char2:
    #         return False
    # return True

    # Opt.3
    # return all(char1 == char2 for char1, char2 in zip(clean_words, reversed(clean_words)))


print(is_palindrome('Radar, Race car, radar'))
