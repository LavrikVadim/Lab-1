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




# plot_list = [[0 for i in range(10)] for i in range(10)]
# result = [0 for i in range(10)]

# for i in range(10):
#     result[i] = i ** 3

# step = round(abs(result[0] - result[9]) / 9, 2)
# print(step)

# for i in range(10):
#     for j in range(10):
#         if j == 0:
#             plot_list[i][j] = step * (8-i) + step

# for i in range(9):
#     for j in range(10):
#         if abs(plot_list[i][0] - result[9 - j]) < step:
#             for k in range(9):
#                 if 8 - k == j:
#                     plot_list[i][k+1] = 1

# for i in range(9):
#     line = ''
#     for j in range(10):
#         if j == 0:
#             line += '\t' + str(int(plot_list[i][j])) + '\t'
#         if plot_list[i][j] == 0:
#             line += '--'
#         if plot_list[i][j] == 1:
#             line += '!!'
#     print(line)
# print('\t0\t1 2 3 4 5 6 7 8 9')

# for i in range(10):
#     #print(plot_list[i])
#     pass

# file = open('sequence.txt', 'r')
# list = []
# for number in file:
#     list.append(float(number))
# file.close()
# print(list)

def numbers():
    with open('sequence.txt') as f:
        a = []
        res = []
        for i in f:
            a.append(float(i))
        for j in a:
            if 5 <= j <= 10 or -10 <= j <= - 5:
                res.append(j)
        print(res)

