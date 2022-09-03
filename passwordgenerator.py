import string
import random

user_entropy = int(input("Enter a number: "))

def make_password(user_entropy):
    ascii_characters = string.printable
    generated_result = ascii_characters * user_entropy
    result_listed = list(generated_result)
    random.shuffle(result_listed)
    return ''.join(result_listed)

final_password = make_password(user_entropy)
print(final_password)
quit()
