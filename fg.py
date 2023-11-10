def dec_to_binary(num):
    if num > 1:
        dec_to_binary(num // 2)
    print(num % 2, end='')