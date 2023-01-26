import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return (name)


def main():
    name = welcome_user()
    string = ['*', '+', '-']
    k = 1

    print('What is the result of the expression?')

    while k <= 3:
        k += 1
        z = random.choice(string)
        x = random.randint(1, 40)
        y = random.randint(1, 20)
        print(f'Quetion: {x} {z} {y}')
        answer = prompt.string('Your answer: ')
        if z == '*':
            rez = x * y
        elif z == '+':
            rez = x + y
        else:
            rez = x - y

        if rez == int(answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{rez}'.")
            return print(f"Let's try again, {name}!")

    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
