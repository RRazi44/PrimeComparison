import math

def isPrimary(number):
    primary = True
    for testNumber in range(2, round(math.sqrt(number)) + 1):
        if number % testNumber == 0:
            primary = False
    return primary

if __name__ == "__main__":
    for number in range(2, 1000001):
        if isPrimary(number):
            print(number)
