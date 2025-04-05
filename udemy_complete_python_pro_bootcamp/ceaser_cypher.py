'''
Input:
- shift
- word
- encode or decode
Output:
- encoded or decoded word

'''

# shift character, also check if out of range: 'a' to 'z', in that case shift around
def shift_character(character, shift):
    ascii_value_after_shift = ord(character) + shift
    if ascii_value_after_shift > ord('z'):
        return chr(ord('a') + ascii_value_after_shift - ord('z') - 1)
    elif ascii_value_after_shift < ord('a'):
        return chr(ord('z') - ord('a') + ascii_value_after_shift + 1)
    else:
        return chr(ascii_value_after_shift)


def process(word, shift):
    new_word = ''
    for character in word:
        if ord(character) == ord(' '):
            new_word += character
            continue
        # not a letter
        if ord(character) > ord('z') or ord(character) < ord('a'):
            continue
        shifted_character = shift_character(character, shift)
        new_word += shifted_character
    return new_word


# main
while True:
    word = input('Input a word: ').lower()
    shift = int(input("Input shift value: "))
    command = input('\'encode\' or \'decode\': ')
    
    if command == 'encode':
        print(process(word, shift))
    elif command == 'decode':
        print(process(word, -shift))
    else:
        print('Error: invalid input.')

    done = input('Continue? \'y\' or \'n\' ')
    if done == 'y':
        continue
    else:
        break
