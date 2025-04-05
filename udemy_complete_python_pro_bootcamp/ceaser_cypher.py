'''
Input:
- shift
- word
- encode or decode
Output:
- encoded or decoded word

'''

def shift_character(character, shift):
    ascii_value_after_shift = ord(character) + shift
    if ascii_value_after_shift > ord('z'):
        return chr(ord('a') + ascii_value_after_shift - ord('z') - 1)
    elif ascii_value_after_shift < ord('a'):
        return chr(ord('z') - ord('a') + ascii_value_after_shift + 1)
    else:
        return chr(ascii_value_after_shift)


def encode(word, shift):
    encoded_word = ''
    for character in word:
        if ord(character) == ord(' '):
            encoded_word += character
            continue
        if ord(character) > ord('z') or ord(character) < ord('a'):
            continue
        shifted_character = shift_character(character, shift)
        encoded_word += shifted_character
    return encoded_word

def decode(word, shift):
    decoded_word = ''
    for character in word:
        if ord(character) == ord(' '):
            decoded_word += character
            continue
        if ord(character) > ord('z') or ord(character) < ord('a'):
            continue
        shifted_character = shift_character(character, shift)
        decoded_word += shifted_character
    return decoded_word

# main
while True:
    word = input('Input a word: ').lower()
    shift = int(input("Input shift value: "))
    command = input('\'encode\' or \'decode\': ')
    
    if command == 'encode':
        print(encode(word, shift))
    elif command == 'decode':
        print(decode(word, -shift))
    else:
        print('Error: invalid input.')

    done = input('Continue? \'y\' or \'n\' ')
    if done == 'y':
        continue
    else:
        break
