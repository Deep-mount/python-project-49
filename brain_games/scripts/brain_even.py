import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return (name)


number = [15, 6, 7]


def even(x):
    if (x % 2) == 0:
        return 'yes'
    elif (x % 2) == 1:
        return 'no'


def proverka(x, answer):
    if even(x) == 'yes' and answer == 'yes':
        return 'yes'
    elif even(x) == 'no' and answer == 'no':
        return 'no'
    else:
        return 'false'


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for k in number:
        print(f'Question: {k}')
        answer = prompt.string('Your answer: ')
        if proverka(k, answer) == 'false':
            return print(f'"{answer}" is wrong answer ;(.'
                         f' Correct answer was "{even(k)}".')
        else:
            print('Correct!')

    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
