import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return (name)


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    k = 1
    while k <= 3:
        k += 1
        long_l = random.randint(5, 10)
        n_xl = random.randint(2, long_l)
        step = random.randint(1, 10)
        start = random.randint(1, 10)
        line = str(start)
        n = 2
        while n <= (long_l):
            if n_xl == n:
                xl = start + step * (n - 1)
                line = line + ' ' + '..'
            else:
                line = line + ' ' + str(start + step * (n - 1))
            n += 1

        print(f'Question: {line}')
        answer = prompt.string('Your answer: ')

        if str(xl) == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{xl}'.")
            return print(f"Let's try again, {name}!")

    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
