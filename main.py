import string
import itertools
import time


# loop through file to get ranking
def pass_check(password):
    f = open('100000-most-common-passwords.txt', 'r')

    count = 0

    # runs through file of common words
    for line in f:
        count += 1
        line = line[:-1]
        if line == password.lower():
            f.close()
            return f"{password}: ❌(#{count} MOST COMMON PASSWORD)"
    f.close()
    return f"{password}: ✅ (Unique)"


def breaker(password, lower, upper, digits, symbols):
    test = ""

    # contours test based on given truth value
    if lower:
        test += string.ascii_lowercase
        print('run 1')
    if upper:
        test += string.ascii_uppercase
        print('run 2')
    if digits:
        test += str(string.digits)
        print('run 3')
    if symbols:
        test += string.punctuation
        print('run 4')

    # list of tuples of every possible test
    cartesian = list(itertools.product(test, repeat=len(password)))

    count = 0
    # loops through the list of tuples to find password
    for couple in cartesian:
        count += 1
        code = ''.join(couple)
        if code == password:
            return f"{password} was cracked in {count:,} guesses."


def main():
    digits = False
    symbols = False
    lower = False
    upper = False
    while True:
        password = input("Enter a password: ")

        # Checks truthiness of type & doubles as a white space checker
        for char in password:
            if char in str(string.digits):
                digits = True

            if char in string.punctuation:
                symbols = True

            if char in string.ascii_lowercase:
                lower = True

            if char in string.ascii_uppercase:
                upper = True

        # validates to make sure the user didn't just enter white space
        if lower or upper or digits or symbols:
            common = pass_check(password)
            print(common)

            # if password not common, breaker runs
            if 'Unique' in common:
                start = time.time()
                print(breaker(password, lower, upper, digits, symbols))
                end = time.time()
                print(f"Time: {(end - start):.4f}s")
                return
            return

        print("Please enter a valid Password.")


main()

# most challenging part was the odometer
