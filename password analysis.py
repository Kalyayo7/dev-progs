def is_very_long(password):
    return len(password) > 11


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_lower_letters(password):
    return any(character.islower() for character in password)


def has_upper_letters(password):
    return any(character.isupper() for character in password)


def has_symbols(password):
    return any((not(character.isdigit()) and not(character.isalpha())) for character in password)


def evaluate_password(password):
    checks = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_symbols
    ]
    
    score = 0
    for check in checks:
        if check(password):
            score += 2
    return score


def main():
    password = input("Введите пароль: ")
    score = evaluate_password(password)
    print("Рейтинг пароля:", score)


if __name__ == '__main__':
    main()





