def has_digit(password):
    return any(c.isdigit() for c in password)


def has_upper_letters(password):
    return any(c.isupper() for c in password)


def has_lower_letters(password):
    return any(c.islower() for c in password)


def is_very_long(password):
    lenth = len(password)
    return lenth > 12


def has_symbols(password):
    return any(not c.isalnum() for c in password)


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
        password_rate += 2 if func(password) else 0

    print('Рейтинг пароля: ' + str(password_rate))


if __name__ == '__main__':
    main()
