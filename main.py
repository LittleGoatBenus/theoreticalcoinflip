import random
import time

headtails = "heads","tails"

#rand0m = random.choice(headtails)
#print(rand0m)
speed = int(input("""

Number of flips

1: 1000
2: 10000
3: 100000
4: 1000000
5: own choice


"""))
counth = 0
countt = 0


if speed == 1:
    for i in range(1000):
        rand0m = random.choice(headtails)

        print(rand0m)

        if rand0m == "heads":
            counth += 1

        if rand0m == "tails":
            countt += 1

        counthper = (counth / 1000) * 100
        counttper = (countt / 1000) * 100

if speed == 2:
    for i in range(10000):
        rand0m = random.choice(headtails)

        print(rand0m)

        if rand0m == "heads":
            counth += 1

        if rand0m == "tails":
            countt += 1

        counthper = (counth / 10000) * 100
        counttper = (countt / 10000) * 100

if speed == 3:
    for i in range(100000):
        rand0m = random.choice(headtails)

        print(rand0m)

        if rand0m == "heads":
            counth += 1

        if rand0m == "tails":
            countt += 1

        counthper = (counth / 100000) * 100
        counttper = (countt / 100000) * 100

if speed == 4:
    for i in range(1000000):
        rand0m = random.choice(headtails)

        print(rand0m)

        if rand0m == "heads":
            counth += 1

        if rand0m == "tails":
            countt += 1

        counthper = (counth / 1000000) * 100
        counttper = (countt / 1000000) * 100

if speed == 5:
    r = int(input("enter how many flips you wish to do: "))
    for i in range(r):
        rand0m = random.choice(headtails)

        print(rand0m)

        if rand0m == "heads":
            counth += 1

        if rand0m == "tails":
            countt += 1

        counthper = (counth / r) * 100
        counttper = (countt / r) * 100




print("\n\nheads:", counthper,"%", "\nheads was flipped ",counth," times\n\n")
print("tails:", counttper,"%", "\ntails was flipped ",countt," times\n\n")
