password = input("Введите пароль: ")

score = 0

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


func = [
    is_very_long(password),
    has_digit(password),
    has_lower_letters(password),
    has_upper_letters(password),
    has_symbols(password)
]


def main(score):

    for i in func:
        if i:
            score+=2
    print("Рейтинг пароля:", score)

if __name__ == '__main__':
    main(score)





