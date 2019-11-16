import string


def cipher(sentence, n_rotate):
    """
    Cipher string with Caesar algorithm ( Anything else than letters stays the same. )
    :param sentence: String containing sentence/sentences/word/words.
    :param n_rotate: number to translate letters
    :return: string with ciphered words
    """
    upper = [char for char in string.ascii_uppercase]  # Uppercase Letters
    lower = [char for char in string.ascii_lowercase]  # Lowercase Letters
    string_ = [char for char in sentence]  # String to cipher
    for i in range(len(string_)):
        transl = 0
        # Cipher Uppercase Letters
        if string_[i] in upper:
            for j in range(len(upper)):
                if string_[i] == upper[j]:
                    transl = j+n_rotate
                    while transl >= len(upper):
                        transl = transl - len(upper)
                    string_[i] = upper[transl]
                    break
        # Cipher Lowercase Letters
        elif string_[i] in lower:
            for j in range(len(lower)):
                if string_[i] == lower[j]:
                    transl = j + n_rotate
                    while transl >= len(lower):
                        transl = transl - len(lower)
                    string_[i] = lower[transl]
                    break
    # Return Cipher sentence
    return ''.join(string_)


def decipher(sentence, n_rotate):
    """
    Decipher string ciphered with Caesar algorithm ( Anything else than letters stays the same. )
    :param sentence: String containing sentence/sentences/word/words.
    :param n_rotate: number to translate letters
    :return: string with deciphered words
    """
    upper = [char for char in string.ascii_uppercase]  # Uppercase Letters
    lower = [char for char in string.ascii_lowercase]  # Lowercase Letters
    string_ = [char for char in sentence]  # String to cipher
    for i in range(len(string_)):
        transl = 0
        # Cipher Uppercase Letters
        if string_[i] in upper:
            for j in range(len(upper)):
                if string_[i] == upper[j]:
                    transl = j-n_rotate
                    while transl < 0:
                        transl = transl + len(upper)
                    string_[i] = upper[transl]
                    break
        # Cipher Lowercase Letters
        elif string_[i] in lower:
            for j in range(len(lower)):
                if string_[i] == lower[j]:
                    transl = j - n_rotate
                    while transl < 0:
                        transl = transl + len(lower)
                    string_[i] = lower[transl]
                    break
    return ''.join(string_)


# Example with Hello World
ciphers = []
sentence = 'Hello World'

print('\nSentence: ' + sentence)
print('\n    Ciphering ')
print('+--------------+')

# Cipher
for number in range(10):
    ciphers.append(cipher(sentence, number))
    print(number, '|', cipher(sentence, number))

print('\n   Deciphering ')
print('+--------------+')

for number in range(10):
    print(number, '|', decipher(ciphers[number], number))
