import string

ALPHABET = list(string.ascii_letters)
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL_CHARS = ["!", "@", "#", "$", "%", "^", "&", "*","(", ")", "_", "+"]
CIPHER_KEY = 3


def cipher(password, chars=ALPHABET, nums=NUMBERS, special=SPECIAL_CHARS, key=CIPHER_KEY):
    """
    allows the storing user passwords as ciphered value

    :param password: user entered value for theirs password
    :param chars: list of all letters(A-Za-z)
    :param nums: list of all numbers for 0-10
    :param special: list of special keys
    :param key: way on how user entered value will be ciphered
    :return: crypted value of user entered value
    """
    ciphered_password = ""

    for char in password:
        if char in chars:
            idx = chars.index(char) + key
            if idx > 49:
                idx = idx - len(chars)
            ciphered_password = ciphered_password + chars[idx]
        elif char in nums:
            idx = nums.index(char) + key
            if idx > 7:
                idx = idx - len(nums)
            ciphered_password = ciphered_password + nums[idx]
        elif char in special:
            idx = special.index(char) + key
            if idx > 9:
                idx = idx - len(special)
            ciphered_password = ciphered_password + special[idx]
        else:
            ciphered_password = "Non valid password"

    return ciphered_password




