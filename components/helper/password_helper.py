import string
import random
import array
import re
from decouple import config


def get_random_password(max_len):
    digits = string.digits
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase
    symbols = string.punctuation

    # combines all the character arrays above to form one array
    combined_list = digits + uppercase_characters + lowercase_characters + symbols

    # randomly select at least one character from each character set above
    rand_digit = random.choice(digits)
    rand_upper = random.choice(uppercase_characters)
    rand_lower = random.choice(lowercase_characters)
    rand_symbol = random.choice(symbols)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    temp_pass_list = list()
    for x in range(max_len - 4):
        temp_pass = temp_pass + random.choice(combined_list)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for pass_list in temp_pass_list:
        password += pass_list

    if re.match(config('PASSWORD_POLICY_REGEX'), password):
        return password
    else:
        print('Password Not Match!')
