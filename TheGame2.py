from random import *
import rate
from tkinter import *

ratings = []

no = 1


def getratings():
    global no
    if label["text"] == ("Batsman {}".format(no)):
        no += 1
        label["text"] = ("Batsman {}".format(no))
    rating = int(e.get())
    ratings.append(rating)
    if len(ratings) is 11:
        playWindow.destroy()


playWindow = Tk()

playWindow.title("Team 1")
label = Label(playWindow, text='Batsman {}'.format(no))
label.pack()
label1 = Label(playWindow, text="Use spinbox to enter ratings")
label1.pack()

e = Spinbox(playWindow, from_=1, to=10)
e.pack()
e.focus_set()

b = Button(playWindow, text='okay', command=getratings)
b.pack(side='bottom')
playWindow.mainloop()

no = 1


def geratings():
    global no
    if label2["text"] == ("Batsman {}".format(no)):
        no += 1
        label2["text"] = ("Batsman {}".format(no))
    rating = int(e1.get())
    ratings.append(rating)
    if len(ratings) is 22:
        playWindow1.destroy()


playWindow1 = Tk()

playWindow1.title("Team 2")
label2 = Label(playWindow1, text='Batsman {}'.format(no))
label2.pack()
label3 = Label(playWindow1, text="Use spinbox to enter ratings")
label3.pack()

e1 = Spinbox(playWindow1, from_=1, to=10)
e1.pack()
e1.focus_set()

b1 = Button(playWindow1, text='okay', command=geratings)
b1.pack(side='bottom')
playWindow1.mainloop()

mainWindow = Tk()
mainWindow.title("Team 1 vs Team 2")
mainWindow.geometry('1280x720')
mainWindow['padx'] = 8
resultWindow = Tk()
resultWindow.title("Result")
resultWindow.geometry('120x80')

for i in range(3):
    mainWindow.columnconfigure(i, weight=20)
for j in range(25):
    if (j == 11) or (j == 23):
        mainWindow.rowconfigure(j, weight=20)
    else:
        mainWindow.rowconfigure(j)
probability = []
for ratin in range(1, 23):
    probability.append(rate.putratings(ratings[ratin - 1]))

runs1 = 0
runs2 = 0
wickets1 = 0
wickets2 = 0
four = 0
six = 0
runs11 = 0
balls11 = 0
for i in range(1, 121):  # 1st innings starts from here
    rand = randint(0, 99)
    if probability[wickets1 - 1][rand] is 5:
        wickets1 += 1
        if wickets1 is 1:
            batsman11 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman11.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns11 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns11.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut11 = Label(mainWindow, text="out")
            batsmanOut11.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 2:
            batsman12 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman12.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns12 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns12.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut12 = Label(mainWindow, text="out")
            batsmanOut12.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 3:
            batsman13 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman13.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns13 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns13.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut13 = Label(mainWindow, text="out")
            batsmanOut13.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 4:
            batsman14 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman14.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns14 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns14.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut14 = Label(mainWindow, text="out")
            batsmanOut14.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 5:
            batsman15 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman15.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns15 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns15.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut15 = Label(mainWindow, text="out")
            batsmanOut15.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 6:
            batsman16 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman16.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns16 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns16.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut16 = Label(mainWindow, text="out")
            batsmanOut16.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 7:
            batsman17 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman17.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns17 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns17.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut17 = Label(mainWindow, text="out")
            batsmanOut17.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 8:
            batsman18 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman18.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns18 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns18.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut18 = Label(mainWindow, text="out")
            batsmanOut18.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 9:
            batsman19 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman19.grid(row=wickets1 - 1, column=0, sticky='w')
            batsmanRuns19 = Label(mainWindow, text='{}({})'.format(runs1 - runs11, i - balls11))
            batsmanRuns19.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut19 = Label(mainWindow, text="out")
            batsmanOut19.grid(row=wickets1 - 1, column=1)
        elif wickets1 is 10:
            batsman110 = Label(mainWindow, text="Batsman {} ({})".format(wickets1, ratings[wickets1 - 1]))
            batsman110.grid(row=wickets1 - 1, column=0, sticky='w')
            if (runs1 - runs11) is 0:
                bat = randint((runs1 - runs11) // 2, runs1 - runs11)
            else:
                bat = randint((runs1 - runs11) // 2, runs1 - runs11 - 1)
            if (i - balls11) is 0:
                bowl = randint((i - balls11) // 2, i - balls11)
            else:
                bowl = randint((i - balls11) // 2, i - balls11 - 1)
            batsmanRuns110 = Label(mainWindow, text='{}({})'.format(bat, bowl))
            batsmanRuns110.grid(row=wickets1 - 1, column=2, sticky='e')
            batsmanOut110 = Label(mainWindow, text="out")
            batsmanOut110.grid(row=wickets1 - 1, column=1)
            batsman111 = Label(mainWindow, text="Batsman {} ({})".format(wickets1 + 1, ratings[wickets1]))
            batsman111.grid(row=wickets1, column=0, sticky='w')
            batsmanRuns111 = Label(mainWindow,
                                   text='{}({})'.format(runs1 - runs11 - bat, i - balls11 - bowl))
            batsmanRuns111.grid(row=wickets1, column=2, sticky='e')
            break
        runs11 = runs1
        balls11 = i
    else:
        runs1 += probability[wickets1 - 1][rand]
        if probability[wickets1 - 1][rand] is 4:
            four += 1
        elif probability[wickets1 - 1][rand] is 6:
            six += 1
if wickets1 < 10:
    batsman112 = Label(mainWindow, text="Batsman {} ({})".format(wickets1 + 1, ratings[wickets1]))
    batsman112.grid(row=wickets1, column=0, sticky='w')
    if (runs1 - runs11) is 0:
        bat = randint((runs1 - runs11) // 2, runs1 - runs11)
    else:
        bat = randint((runs1 - runs11) // 2, runs1 - runs11 - 1)
    if (i - balls11) is 0:
        bowl = randint((i - balls11) // 2, i - balls11)
    else:
        bowl = randint((i - balls11) // 2, i - balls11 - 1)
    batsmanRuns112 = Label(mainWindow, text='{}({})'.format(bat, bowl))
    batsmanRuns112.grid(row=wickets1, column=2, sticky='e')
    batsman113 = Label(mainWindow, text="Batsman {} ({})".format(wickets1 + 2, ratings[wickets1 + 1]))
    batsman113.grid(row=wickets1 + 1, column=0, sticky='w')
    batsmanRuns113 = Label(mainWindow, text='{}({})'.format(runs1 - runs11 - bat, i - balls11 - bowl))
    batsmanRuns113.grid(row=wickets1 + 1, column=2, sticky='e')
runsScored = Label(mainWindow, text="{}/{}".format(runs1, wickets1))
runsScored.grid(row=11, column=2, sticky='e')
boundries1 = Label(mainWindow, text='Fours: {}\tSixes:{}\t Overs: {}.{}'.format(four, six, i // 6, i % 6))
boundries1.grid(row=11, column=1)

print(runs1, wickets1, i)
balls22 = 0
zero = one = two = three = four = six = 0
runs22 = 0
for j in range(1, 121):  # 2nd innings
    if runs2 > runs1:
        batsman212 = Label(mainWindow, text="Batsman {}({})".format(wickets2 + 1, ratings[11 + wickets2]))
        batsman212.grid(row=12 + wickets2, column=0, sticky='w')
        if (runs2 - runs22) is 0:
            bat = randint((runs2 - runs22) // 2, runs2 - runs22)
        else:
            bat = randint((runs2 - runs22) // 2, runs2 - runs22 - 1)
        if (j - balls22) is 0:
            bowl = randint((j - balls22) // 2, j - balls22)
        else:
            bowl = randint((j - balls22) // 2, j - balls22 - 1)
        batsmanRuns212 = Label(mainWindow, text='{}({})'.format(bat, bowl))
        batsmanRuns212.grid(row=12 + wickets2, column=2, sticky='e')
        batsman213 = Label(mainWindow, text="Batsman {}({})".format(wickets2 + 2, ratings[12 + wickets2]))
        batsman213.grid(row=13 + wickets2, column=0, sticky='w')
        batsmanRuns213 = Label(mainWindow, text='{}({})'.format(runs2 - runs22 - bat, j - balls22 - bowl))
        batsmanRuns213.grid(row=13 + wickets2, column=2, sticky='e')
        break
    else:
        rand = randint(0, 99)
        if probability[12 + wickets2][rand] is 5:
            wickets2 += 1
            if wickets2 is 1:
                batsman21 = Label(mainWindow, text="Batsman {} ({})".format(wickets2, ratings[10 + wickets2]))
                batsman21.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns21 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns21.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut21 = Label(mainWindow, text="out")
                batsmanOut21.grid(row=11 + wickets2, column=1)
            elif wickets2 is 2:
                batsman22 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman22.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns22 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns22.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut22 = Label(mainWindow, text="out")
                batsmanOut22.grid(row=11 + wickets2, column=1)
            elif wickets2 is 3:
                batsman23 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman23.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns23 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns23.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut23 = Label(mainWindow, text="out")
                batsmanOut23.grid(row=11 + wickets2, column=1)
            elif wickets2 is 4:
                batsman24 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman24.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns24 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns24.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut24 = Label(mainWindow, text="out")
                batsmanOut24.grid(row=11 + wickets2, column=1)
            elif wickets2 is 5:
                batsman25 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman25.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns25 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns25.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut25 = Label(mainWindow, text="out")
                batsmanOut25.grid(row=11 + wickets2, column=1)
            elif wickets2 is 6:
                batsman26 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman26.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns26 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns26.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut26 = Label(mainWindow, text="out")
                batsmanOut26.grid(row=11 + wickets2, column=1)
            elif wickets2 is 7:
                batsman27 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman27.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns27 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns27.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut27 = Label(mainWindow, text="out")
                batsmanOut27.grid(row=11 + wickets2, column=1)
            elif wickets2 is 8:
                batsman28 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman28.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns28 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns28.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut28 = Label(mainWindow, text="out")
                batsmanOut28.grid(row=11 + wickets2, column=1)
            elif wickets2 is 9:
                batsman29 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman29.grid(row=11 + wickets2, column=0, sticky='w')
                batsmanRuns29 = Label(mainWindow, text='{}({})'.format(runs2 - runs22, j - balls22))
                batsmanRuns29.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut29 = Label(mainWindow, text="out")
                batsmanOut29.grid(row=11 + wickets2, column=1)
            elif wickets2 is 10:
                batsman210 = Label(mainWindow, text="Batsman {}({})".format(wickets2, ratings[10 + wickets2]))
                batsman210.grid(row=11 + wickets2, column=0, sticky='w')
                if (runs2 - runs22) is 0:
                    bat = randint((runs2 - runs22) // 2, runs2 - runs22)
                else:
                    bat = randint((runs2 - runs22) // 2, runs2 - runs22 - 1)
                if (j - balls22) is 0:
                    bowl = randint((j - balls22) // 2, j - balls22)
                else:
                    bowl = randint((j - balls22) // 2, j - balls22 - 1)
                batsmanRuns210 = Label(mainWindow, text='{}({})'.format(bat, bowl))
                batsmanRuns210.grid(row=11 + wickets2, column=2, sticky='e')
                batsmanOut210 = Label(mainWindow, text="out")
                batsmanOut210.grid(row=11 + wickets2, column=1)
                batsman211 = Label(mainWindow, text="Batsman {}({})".format(wickets2 + 1, ratings[11 + wickets2]))
                batsman211.grid(row=12 + wickets2, column=0, sticky='w')
                batsmanRuns211 = Label(mainWindow,
                                       text='{}({})'.format(runs2 - runs22 - bat, j - balls22 - bowl))
                batsmanRuns211.grid(row=12 + wickets2, column=2, sticky='e')
                break
            runs22 = runs2
            balls22 = j
        else:
            runs2 += probability[12 + wickets2][rand]
            if probability[12 + wickets2][rand] is 4:
                four += 1
            elif probability[12 + wickets2][rand] is 6:
                six += 1
if (runs1 >= runs2) and (wickets2 != 10):
    batsman210 = Label(mainWindow, text="Batsman {}({})".format(wickets2 + 1, ratings[11 + wickets2]))
    batsman210.grid(row=11 + wickets2, column=0, sticky='w')
    if (runs2 - runs22) is 0:
        bat = randint((runs2 - runs22) // 2, runs2 - runs22)
    else:
        bat = randint((runs2 - runs22) // 2, runs2 - runs22 - 1)
    if (j - balls22) is 0:
        bowl = randint((j - balls22) // 2, j - balls22)
    else:
        bowl = randint((j - balls22) // 2, j - balls22 - 1)
    batsmanRuns210 = Label(mainWindow, text='{}({})'.format(bat, bowl))
    batsmanRuns210.grid(row=11 + wickets2, column=2, sticky='e')
    batsmanOut210 = Label(mainWindow, text="out")
    batsmanOut210.grid(row=11 + wickets2, column=1)
    batsman211 = Label(mainWindow, text="Batsman {}({})".format(wickets2 + 1, ratings[12 + wickets2]))
    batsman211.grid(row=12 + wickets2, column=0, sticky='w')
    batsmanRuns211 = Label(mainWindow, text='{}({})'.format(runs2 - runs22 - bat, j - balls22 - bowl))
    batsmanRuns211.grid(row=12 + wickets2, column=2, sticky='e')
runsScored2 = Label(mainWindow, text="{}/{}".format(runs2, wickets2))
runsScored2.grid(row=23, column=2, sticky='e')
boundries2 = Label(mainWindow, text='Fours: {}\tSixes: {}\tOvers: {}.{}'.format(four, six, j // 6, j % 6))
boundries2.grid(row=23, column=1)
print(runs2, wickets2, j)
if runs1 > runs2:
    print("Team 1 wins by", runs1 - runs2, "runs")
    result = Label(resultWindow, text='Team 1 wins by {} runs'.format(runs1 - runs2))
    resultWindow.configure(background='Red')
elif runs2 > runs1:
    print("Team 2 wins by", 10 - wickets2, "wickets and", 120 - j, "balls to spare")
    result = Label(resultWindow,
                   text='Team 2 wins by {} wickets and {} balls to spare'.format(10 - wickets2, 120 - j))
    resultWindow.configure(background='Blue')
else:
    print("TIE!!")
    result = Label(resultWindow, text="Match is TIED")
    resultWindow.configure(background='yellow')
result.pack()
mainWindow.mainloop()

resultWindow.mainloop()
