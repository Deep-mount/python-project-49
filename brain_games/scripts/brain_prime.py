import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return (name)


def prime(x):
    k = 0
    for j in range(2, x):
        if x % j == 0:
            k += 1
    if k == 0:
        return 'yes'
    else:
        return 'no'


def main():
    name = welcome_user()
    lim_x = 100
    k = 1
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while k <= 3:
        x = random.randint(2, lim_x)
        print(f'Question: {x}')
        answer = prompt.string('Your answer: ')
        rez = prime(x)

        if rez == answer:
            print('Correct!')
            k += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{rez}'.")
            return print(f"Let's try again, {name}!")

    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
