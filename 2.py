from random import *


class Lottery:
    def __init__(self):
        self.w = []
        self.t = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 'a', 'b', 'c', 'p', 'z']

    def win(self):
        i = 0
        w = []
        while i < 4:
            w.append(choice(self.t))
            i += 1
        self.w = w

    def return_code(self):
        return self.w


if __name__ == '__main__':
    my_ticket = [1, 2, 3, 4]
    attempt = 1
    my_lottery = Lottery()
    my_lottery.win()
    while my_lottery.return_code() != my_ticket:
        attempt += 1
        my_lottery.win()
    print(attempt, " попыток до победы!")