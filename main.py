def decode_email(data_string):
    email = ""
    r = int(data_string[:2], 16)
    i = 2
    while len(data_string)-i:
        char = int(data_string[i:i+2], 16) ^ r
        email += chr(char)
        i += 2
    return email

code = "275e464946404e4346534855526754464a464e4b0944484a"
print(decode_email(code))
