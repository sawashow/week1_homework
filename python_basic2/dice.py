import random


def roll_dice(sides, times):
    results = []
    for _ in range(times):
        dice = random.randint(1, sides)
        results.append(dice)
    return results


def main():
    sides = int(input("サイコロの面の数は?: "))
    times = int(input("何回振りますか?: "))

    print(roll_dice(sides=sides, times=times))


if __name__ == "__main__":
    main()
