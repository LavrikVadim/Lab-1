import matplotlib.pyplot as plt
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

def flag():
    for i in range(9):
        if i < 3:
            print(f'{WHITE}{"  " * (4)}{BLUE}{"  " * (2)}{WHITE}{"  " * (10)}{END}')
        if 4 <= i <= 5:
            print(f'{BLUE}{"  " * 16}{END}')
        if i > 5:
            print(f'{WHITE}{"  " * (4)}{BLUE}{"  " * (2)}{WHITE}{"  " * (10)}{END}')
        

def pattern():
    for i in range(10):
        if i < 2:
            print(f'{WHITE}{"  " * 16}{END}')
        if i == 2:
            print(f'{WHITE}{"  " * 5}{RED}{"  "}{WHITE}{"  " * 4}{RED}{"  "}{WHITE}{"  " * 5}{END}')
        if i == 3:
            print(f'{WHITE}{"  " * 4}{RED}{"  " * 3}{WHITE}{"  " * 2}{RED}{"  " * 3}{WHITE}{"  " * 4}{END}')
        if i == 4:
            print(f'{WHITE}{"  " * 3}{RED}{"  " * 5}{RED}{"  " * 5}{WHITE}{"  " * 3}{END}')
        if i == 5:
            print(f'{WHITE}{"  " * 4}{RED}{"  " * 3}{WHITE}{"  " * 2}{RED}{"  " * 3}{WHITE}{"  " * 4}{END}')
        if i == 6:
            print(f'{WHITE}{"  " * 5}{RED}{"  "}{WHITE}{"  " * 4}{RED}{"  "}{WHITE}{"  " * 5}{END}')
        if 7 <= i < 9:
            print(f'{WHITE}{"  " * 16}{END}')


def chart():

    x = [0, 2, 4, 6, 8, 10]
    y = [0, 1, 2, 3, 4, 5]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = x / 2')
    plt.show()


def numbers():
    with open('sequence.txt') as f:
        a = []
        res = []
        for i in f:
            a.append(float(i))
        for j in a:
            if 5 <= j <= 10 or -10 <= j <= - 5:
                res.append(j)
        return(res)
    
if __name__ == '__main__':
    print(numbers())

flag()
pattern()
chart()
