def has_digit(password):
    rate = 0
    if any(c.isdigit() for c in password):
        rate = 2
    return rate


def has_upper_letters(password):
    rate = 0
    if any(c.isupper() for c in password):
        rate = 2
    return rate


def has_lower_letters(password):
    rate = 0
    if any(c.islower() for c in password):
        rate = 2
    return rate


def is_very_long(password):
    rate = 0
    lenth = len(password)
    if lenth > 12:
        rate = 2
    return rate


def has_symbols(password):
    rate = 0
    if any(not c.isalnum() for c in password):
        rate = 2
    return rate


def main():
    cheks = [
            has_digit,
            is_very_long,
            has_upper_letters,
            has_lower_letters,
            has_symbols
    ]

    password = input('Введите пароль: ')
    password_rate = 0

    for func in cheks:
        result = func(password)
        password_rate += result

    print('Рейтинг пароля: ' + str(password_rate))


if __name__ == '__main__':
    main()
