def is_narcissistic(n: int) -> bool:
    digits = [int(n) for n in list(str(n))]
    n_digits = len(digits)
    return sum([digit ** n_digits for digit in digits]) == n

if __name__ == '__main__':
    assert is_narcissistic(153)
    assert not is_narcissistic(154)
    assert not is_narcissistic(152)

    number_to_find = 50
    n_found = 0
    i = 1
    while True:
        if is_narcissistic(i):
            n_found += 1
            print('{:2}: {:6}'.format(n_found, i))
        if n_found == number_to_find:
            break
        i += 1

