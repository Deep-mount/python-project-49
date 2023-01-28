import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return (name)


def nod(n_1, n_2):
    k = n_1
    while k > 0:
        if (n_2 % k == 0) and (n_1 % k == 0):
            return k
        k -= 1


def main():
    name = welcome_user()
    lim_x = 20
    lim_y = 20
    k = 1
    print('Find the greatest common divisor of given numbers.')

    while k <= 5:
        x = random.randint(1, lim_x)
        y = random.randint(1, lim_y)
        print(f'Question: {x} {y}')
        answer = prompt.string('Your answer: ')
        rez = nod(x, y)

        if rez == int(answer):
            print('Correct!')
            k += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{rez}'.")
            return print(f"Let's try again, {name}!")

    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
