def turnOver(number):
    '''
    Returns a list of all digits of this number in reverse order
    :return: list of digits
    NOTE: output 0 if the number is not a natural number
    '''

    if number < 1 or type(number) is not int:
        return 0

    digits = []
    remainder = number
    while remainder > 0:
        digits.append(remainder % 10)
        remainder //= 10

    return digits

if __name__ == '__main__':
    assert turnOver(123) == [3, 2, 1]
    assert turnOver(12.3) == 0
    assert turnOver(-123) == 0
    assert turnOver(0) == 0
