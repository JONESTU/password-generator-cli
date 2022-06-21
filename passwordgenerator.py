import string
import random

user_length = int(input("Enter your password length: "))

def make_password(user_length):
    ascii_characters = string.printable
    generated_result = ascii_characters * user_length
    result_listed = list(generated_result)
    random.shuffle(result_listed)
    return ''.join(result_listed)

final_password = make_password(user_length)
print(final_password)
quit()
