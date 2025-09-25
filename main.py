"""
Black Jack for NUMWORKS
2025 - Lulutoulouse31

Code update 25/09/25
License update 18/09/25

This software is licensed under the GNU AGPL-3.0 License
"""

import math
import time
import random
import kandinsky
import ion

def printLogoScreen():
    logoScreen = 'BnkkkltBpnPmlFxiiipNvivHeabbaapAhePheFxddajNuasHeiCgbAheCtlEsihmBheBrmtDcjBpirCwnhjtAuasAvmpyCeiCkbAheBpaadxBoaddacyheAoahyDcjAqaaawAvdaeaapuasvdctDeaffealAheAnaaaabwvaiyAunyhepaiyEcjAnaaatAjcuBmvuaodctEecffeahAhetaaaaaadpawEhaaaxFcjqbaaabwbkEuabalFeiCnavhepaaaaaabpawEhagajFcjeaaaaakbjEuacfawEehBynavheycadeaalxahBsnAhdylaswmuAsanhaaaaamiatAxlvuaqxaeEeabbbajAheBunbvuBoaadafxheBdbxbadafxykeaimyycaccaouasApapDnkkkksBpmByposDtkioxArpBwouymimxCniqDnijuAxowBpo'
    logoScreen = "".join([(ord(val) - 64)*"z" if ord(val) <= 90 else val for val in logoScreen])
    kandinsky.fill_rect(0, 0, 320, 222, (255, 255, 255))

    #PRINT NAME
    t = "Made by lulutoulouse31"
    x = 8
    for i, txt in enumerate(t):
        for char in txt:
            if char != " ":
                printMicroTxt(char, x, 211, (0, 0, 0))
            x += 4

    #PRINT LOGO
    for i, color in enumerate(logoScreen):
        time.sleep(1/999)
        color = (ord(color) - 97) * 10
        if color != "z":
            x = (i-(math.floor(i/64)*64))*5
            y = (math.floor(i/64))*5
            kandinsky.fill_rect(x, y+75, 5, 5, (color, color, color))

def printBackground():
    for i in range(15):
        color = (0, math.floor(60 + ((80 / 15) * i)), math.floor(10 + ((40 / 15) * i)))
        kandinsky.fill_rect(0, 222-(i*16), 320, 16, color)

def shuffleCard():
    c = []
    card = []
    for color in ["R", "R", "B", "B"]*2:
        for i in range(2, 11):
            c.append(str(i) + color)
        for head in ["K", "Q", "J", "A"]:
            c.append(head + color)
    for i in range(len(c)):
        r = random.randint(0, len(c) - 1)
        card.append(c[r])
        c.pop(r)
    return card

def printCover(x, y, x2, y2):
    for h in range(y, y2 + 1):
        kandinsky.fill_rect(x, h, x2 - x, 1, kandinsky.get_pixel(x, h))

def printMoneyInfo(info, value):
    if isinstance(value, int):
        v = "{:,}".format(value).replace(",", " ")
    elif isinstance(value, list):
        v = value.copy()
        v.reverse()
        v = ["{:,}".format(int(val)).replace(",", " ") for val in v]
        v = " / ".join(v)

    if info == 0:
        info = "Balance: " + v
        x = 280 - 4 * len(v)
    else:
        printCover(0, 0, 160, 10)
        x = 5
        info = "Bet: " + v

    y = 5
    for char in info:
        if char != " ":
            printMicroTxt(char, x, y, (255, 255, 255))
        x += 4

def printMicroTxt(char, x, y, color):
    ref = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!.,:;%+-*/=<>'_→[](){}"
    font = "2jg02oN06Fd07AE04l907dE07dl079907gl07h906lj06kl03aZ06jk07dd07da03bh05lj07IN079h05kj04ad05zj01li03jk06la06jwG6kj03YE07II05jl05jg05jz05gj05gI07Ad003l04cl003d01Bl007p03ca003lE4cj026N0119g4br04aZ007z006j007l006la03l907a003M04dZ005l005g005?005L005hE07AO7A202I200020002W0220022W5Ab00NG007000ge01AKW0uu01KH04HK02G00000u4NK03IJ06IM01IH04IK03MJ06JM0"
    for seq in range(4):
        v = ref.index(font[(ref.index(char) * 4) + seq])
        b = 32
        for i in range(6):
            if v >= b:
                kandinsky.set_pixel(i % 3 + x, i // 3 + (2 * seq) + y, color)
                v -= b
            b = b // 2

def printActionKey(key):
    t = [val + " " * 10 for val in ["UP: Stand", "DOWN: Hit", "LEFT: Double", "RIGHT: Split"]]
    x = 15
    for i, txt in enumerate(t):
        color = (255, 255, 255) if key[i] else (0, 45, 10)
        for char in txt:
            if char != " ":
                printMicroTxt(char, x, 211, color)
            x += 4

def movAvailable(deck, nbDeck, balance, bet, origBet):
    b = bet[0] + bet[1] if len(bet) == 2 else bet[0]
    mov = [True, True, False, False]
    d = [val[:-1].replace("K", "10").replace("Q", "10").replace("J", "10") for val in deck]
    if len(d) == 2 and b + origBet <= balance:
        mov[2] = True
        if d[0] == d[1] and nbDeck == 1:
            mov[3] = True
    return mov

def waitForMove(move):
    while True:
        m = ["S", "H", "DD", "SP"]
        for i, k in enumerate([ion.KEY_UP, ion.KEY_DOWN, ion.KEY_LEFT, ion.KEY_RIGHT]):
            if ion.keydown(k) and move[i]:
                while ion.keydown(k):
                    time.sleep(1/100)
                return m[i]
        time.sleep(1/100)

def printCard(x, y, card, offsetColor=0):
    color = (255 + offsetColor, 0, 0) if "R" in card else (0, 0, 0)
    c = (245+offsetColor, 245+offsetColor, 245+offsetColor) if card != "back" else (160, 19, 162)
    kandinsky.fill_rect(x, y + 2, 1, 41, c)
    kandinsky.fill_rect(x+30, y+2, 1, 41, c)
    kandinsky.fill_rect(x + 1, y + 1, 1, 43, c)
    kandinsky.fill_rect(x+29, y+1, 1, 43, c)
    kandinsky.fill_rect(x + 2, y, 27, 45, c)
    if card != "back":
        ch = card[:-1]
    else:
        ch = "$$"
        color = (81, 0, 81)
    offsetX = -5 if len(ch) == 2 else 0
    kandinsky.draw_string(ch, x+10+offsetX, y+13, color, c)

def printNewCard(player, deck, number, pos=0, offsetColor=0):
    n = number
    offsetX = 0 if pos == 0 else 60 if pos == 1 else -60
    x = 143 + offsetX
    y = 130 if player == "p" else 25
    for val in deck:
        printCard(x-n*20, y-n*5, val, -7*(n%2)+offsetColor)
        n += 1

def printNumber(player, deck, pos=0):
    offsetX = 0 if pos == 0 else 60 if pos == 1 else -60
    x = 149
    y = 179 if player == "p" else 73
    d = [val[:-1] if val[:-1] not in ["K", "Q", "J"] else "10" for val in deck]

    #CALC SUM
    sum = 0
    for val in d:
        val = 11 if val == "A" else val
        sum += int(val)

    #CHECK FOR OVERSHOT SOFT
    for i in range(d.count("A")):
        if sum > 21:
            sum -= 10
        else:
            break
    offsetX += 6 if len(str(sum)) == 1 else 0
    bc = (200, 0, 0) if sum > 21 else (0, 120, 180) if sum == 21 else (0, 30, 0)
    kandinsky.draw_string(str(sum), x+offsetX, y, (255, 255, 255), bc)
    return sum

def printMoneySel(value, number, sel, first):
    b = "{:,}".format(number).replace(",", " ")
    c = (255, 255, 255)
    bc = (90, 90, 90)
    if value == 0:
        printCover(60, 60, 260, 100)
        if sel:
            kandinsky.draw_string("> Balance: " + b + " <", 83-3*len(b), 70, c, bc)
        else:
            kandinsky.draw_string("Balance: " + b, 100 - 3 * len(b), 70, c, bc)
    else:
        offsetY = 0 if first else -20
        printCover(80, 100+offsetY, 250, 130+offsetY)
        if sel:
            kandinsky.draw_string("> Bet: " + b + " <", 103 - 3 * len(b), 110+offsetY, c, bc)
        else:
            kandinsky.draw_string("Bet: " + b, 122 - 3 * len(b), 110+offsetY, c, bc)

def betScreen(first, balance, bet):
    printBackground()

    #PRINT INFO TEXT
    t = [val + " " * 16 for val in ["LEFT: Lower", "RIGHT: Higher", "OK: Start"]]
    x = 25
    for txt in t:
        for char in txt:
            if char != " ":
                printMicroTxt(char, x, 211, (255, 255, 255))
            x += 4

    sel = 1
    if bet > balance:
        bet = math.floor(balance/500)*500
    if first:
        sel = 0
        printMoneySel(0, balance, True if sel == 0 else False, first)
    else:
        printMoneyInfo(0, balance)
    printMoneySel(1, bet, True if sel == 1 else False, first)

    #SELECT VALUE
    loop = True
    while loop:
        for i, k in enumerate([ion.KEY_UP, ion.KEY_DOWN, ion.KEY_LEFT, ion.KEY_RIGHT, ion.KEY_OK]):
            if ion.keydown(k):
                for j in range(2):
                    if i == j and first and sel == (j+1)%2:
                        sel = j
                        printMoneySel(0, balance, True if j == 0 else False, first)
                        printMoneySel(1, bet, True if j == 1 else False, first)

                if i == 2:
                    if sel == 0 and balance > 1_000 and (balance-1000) >= bet:
                        balance += -1000
                        printMoneySel(0, balance, True, first)
                    elif sel == 1 and bet > 500:
                        bet += -500
                        printMoneySel(1, bet, True, first)

                elif i == 3:
                    if sel == 0 and balance < 1_000_000:
                        balance += 1000
                        printMoneySel(0, balance, True, first)
                    elif sel == 1 and bet < 1_000_000 and (bet+500) <= balance:
                        bet += 500
                        printMoneySel(1, bet, True, first)

                elif i == 4:
                    loop = False

                time.sleep(1 / 10)
        time.sleep(1 / 100)

    return balance, bet

def game(balance, bet):
    printBackground()
    card = shuffleCard()
    origBet = bet
    bet = [bet]

    player = [[card[0], card[1]]]
    dealer = [card[2]]
    for i in range(3):
        card.pop(0)

    printNewCard("p", player[0], 0)
    printNewCard("d", ["back"] + dealer, 0)

    sum = [printNumber("p", player[0])]
    printNumber("d", dealer)

    printMoneyInfo(0, balance)
    printMoneyInfo(1, bet[0])

    #PLAYER PLAY
    while True:
        if sum[0] >= 21:
            break

        m = movAvailable(player[0], 1, balance, bet, origBet)
        printActionKey(m)

        move = waitForMove(m)

        if move == "S":
            break
        elif move in ["H", "DD"]:
            printNewCard("p", [card[0]], len(player[0]))
            player[0].append(card[0])
            card.pop(0)
            sum[0] = printNumber("p", player[0])
            if move == "DD":
                bet[0] *=2
                printMoneyInfo(1, bet[0])
                printActionKey([False, False, False, False])
                break
        elif move == "SP":
            bet = [bet[0], bet[0]]
            player = [[player[0][0], card[0]], [player[0][1], card[1]]]
            for i in range(2):
                card.pop(0)

            printCover(120, 120, 177, 200)

            sum = [printNumber("p", player[0], 1), printNumber("p", player[1], 2)]

            currentDeck = 1 if sum[0] >= 21 and sum[1] != 21 else 0

            for i in range(2):
                printNewCard("p", player[i], 0, i+1, -170 if currentDeck == (i+1)%2 else 0)

            printMoneyInfo(1, bet)

            if sum == [21, 21]:
                break

            loop2 = True
            while loop2:
                loop = True
                while loop:

                    m = movAvailable(player[currentDeck], 2, balance, bet, origBet)
                    printActionKey(m)

                    move = waitForMove(m)

                    if move == "S":
                        loop = False
                    elif move in ["H", "DD"]:
                        printNewCard("p", [card[0]], len(player[currentDeck]), currentDeck+1)
                        player[currentDeck].append(card[0])
                        card.pop(0)
                        sum[currentDeck] = printNumber("p", player[currentDeck], currentDeck+1)
                        if move == "DD":
                            bet[currentDeck] *= 2
                            printMoneyInfo(1, bet)
                            loop = False
                    if sum[currentDeck] >= 21:
                        loop = False
                if currentDeck == 0 and sum[1] < 21:
                    currentDeck = 1
                    for i in range(2):
                        printNewCard("p", player[i], 0, i+1, -170 if i == 0 else 0)
                else:
                    for i in range(2):
                        printNewCard("p", player[i], 0, i+1)
                    loop2 = False
            break
    printActionKey([False, False, False, False])

    #DEALER PLAY
    dsum = 0
    while dsum < 17:
        time.sleep(1)
        if len(dealer) > 1:
            dealer.append(card[0])
        else:
            dealer.insert(0, card[0])
        card.pop(0)
        printNewCard("d", dealer if len(dealer) == 2 else [dealer[-1]], 0 if len(dealer) == 2 else len(dealer)-1)
        dsum = printNumber("d", dealer)
        if len(sum) == 1:
            if sum[0] > 21 or (sum[0] == 21 and len(player[0]) == 2):
                break
        elif (sum[0] > 21 and sum[1] > 21) or (sum[0] == 21 and len(player[0]) == 2 and sum[1] == 21 and len(player[1]) == 2):
            break

    time.sleep(1)

    #CALC RESULT
    win = 0
    for i in len(sum):
        if dsum == 21 and len(dealer) == 2 and len(player[i]) != 2:
            win -= bet[i]
        elif sum[i] == 21 and len(player[i]) == 2 and not (len(dealer) == 2 and dsum == 21):
            win += int(1.5*bet[i])
        elif sum[i] > 21:
            win -= bet[i]
        elif sum[i] > dsum or dsum > 21:
            win += bet[i]
        elif sum[i] < dsum:
            win -= bet[i]

    bc = (200, 0, 0) if win < 0 else (88, 88, 88) if win == 0 else (0, 178, 50)
    winTxt = "{:,}".format(int(win)).replace(",", " ")
    txt = "Money earned: +" + str(winTxt) if win >= 0 else "Money lost: " + str(winTxt)
    if win == 0:
        txt = txt.replace("+", "")
    kandinsky.draw_string(txt, 175-6*len(txt), 90, (255, 255, 255), bc)
    kandinsky.draw_string("Press OK to continue", 60, 120, (255, 255, 255), (90, 90, 90))

    while not ion.keydown(ion.KEY_OK):
        time.sleep(1/100)
    while ion.keydown(ion.KEY_OK):
        time.sleep(1/100)

    balance += win
    return balance

def printLoseScreen(gameNumber):
    printBackground()
    kandinsky.draw_string("Game played: " + str(gameNumber), 95-6*len(str(gameNumber)), 70, (255, 255, 255), (90, 90, 90))
    kandinsky.draw_string("Press OK to continue", 60, 100,(255, 255, 255), (90, 90, 90))

    while not ion.keydown(ion.KEY_OK):
        pass
    while ion.keydown(ion.KEY_OK):
        pass

def play():
    printLogoScreen()
    time.sleep(2)

    while True:
        first = True
        gameNumber = 0
        balance = 50_000
        bet = 5_000

        loop = True
        while loop:
            balance, bet = betScreen(first, balance, bet)
            first = False if first else first
            balance = game(balance, bet)
            gameNumber += 1
            if balance < 500:
                loop = False

        printLoseScreen(gameNumber)

play()
