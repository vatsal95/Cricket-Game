from random import *


def putratings(r):
    probability1 = []
    if r is 1:
        zero = 34
        one = 24
        two = 4
        three = 1
        four = 8
        six = 6
        wicket = 23
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 2:
        zero = 34
        one = 25
        two = 4
        three = 1
        four = 9
        six = 7
        wicket = 20
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 3:
        zero = 34
        one = 23
        two = 7
        three = 1
        four = 9
        six = 7
        wicket = 19
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 4:
        zero = 31
        one = 23
        two = 11
        three = 2
        four = 10
        six = 7
        wicket = 16
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 5:
        zero = 29
        one = 23
        two = 14
        three = 2
        four = 11
        six = 8
        wicket = 13
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 6:
        zero = 28
        one = 23
        two = 15
        three = 3
        four = 13
        six = 8
        wicket = 10
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 7:
        zero = 27
        one = 23
        two = 15
        three = 3
        four = 15
        six = 9
        wicket = 8
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 8:
        zero = 25
        one = 23
        two = 17
        three = 3
        four = 16
        six = 9
        wicket = 7
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 9:
        zero = 21
        one = 24
        two = 19
        three = 3
        four = 17
        six = 10
        wicket = 6
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 10:
        zero = 17
        one = 25
        two = 20
        three = 4
        four = 18
        six = 10
        wicket = 6
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    return probability1
