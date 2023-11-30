import string

direction = input('type "encode" or "decode": ')
text = input('type youe massage:\n ')
shift = int(input('how many shift? '))

# def encript(plain_text,shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = string.ascii_letters.index(letter)
#         new_position = position + shift_amount
#         new_letter = string.ascii_letters[new_position]
#         cipher_text += new_letter
#     print(f'the encoded text is {cipher_text}')

# def decrypt(cipher_text,shift_amount):
#     plain_text = ''
#     for letter in cipher_text:
#         position = string.ascii_letters.index(letter)
#         new_position = position - shift_amount
#         plain_text += string.ascii_letters[new_position]
#     print(f'the decoded text is {plain_text}')

# if direction == 'encode':
#     encript(text,shift)
# elif direction == 'decode':
#     decrypt(text,shift)

def caesar(start_text,shift_amount,cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
            shift_amount *= -1
            # 5 * -1 = -5
            #12 + -5
    for letter in start_text:
        position = string.ascii_letters.index(letter)
        new_position = position + shift_amount
        end_text += string.ascii_letters[new_position]
    print(f'the {cipher_direction}d text is {end_text}')


print(caesar(text,shift,direction))