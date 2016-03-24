from collections import Counter

with open('cipher.txt', 'r') as file:
    cipher_text = file.read()

# Finds the most common letters
#
# letters = Counter(cipher_text)
# print letters

# print ord('/') - ord(' ')
# print ord('t') - ord('e')

def shift(c, n):
    newpos = ord(c) + n
    return chr(newpos)

message_chars = [shift(c, -15) for c in cipher_text]

message = "".join(message_chars)

print message