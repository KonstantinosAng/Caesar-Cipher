import string


def caesar(sentence, n_rotate):
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


# Example
print(caesar('Hello World', 3))
