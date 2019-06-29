# roulette : a win is worth 36 dollars, it's a dollar to play
# ------------------------------------------------- good luck !

import matplotlib.pyplot as plt
import random


money = 100
wheel = [0, 00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19,
         20, 21, 22, 23, 24, 25, 26, 27, 28,
         29, 30, 31, 32, 33, 34, 35, 36]

# spin n times
# bet on a number
def spin(n, bet):
    track = []
    dollars = money
    win = 0
    loss = 0

    for i in range(n):
        if dollars > 0:
            dollars -= 1
            x = random.choice(wheel)
            
            if bet == x:
                win += 1
                dollars += 36
            else:
                loss += 1

            track.append(dollars)

    print("|| Wins: {}  ||  Losses: {} ||".format(win, loss))
    
    if dollars == 0:
        print("[!] You are broke [!]")
    elif dollars > money:
        print("\n[$$] You actually won ${:.2f} [$$]".format(dollars - money))
    else:
        print("[!] You lost ${:.2f}".format(money - dollars))

    plt.plot(track)
    plt.ylabel('Money')
    plt.xlabel('Spins')
    plt.title("Roulette: {} spins - bet is #{}".format(n, bet))
    plt.show()

spin(10000, 18)
spin(1000, 33)
spin(100, 1)
spin(10, 20)
