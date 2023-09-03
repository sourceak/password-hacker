import string
import itertools


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


def breaker(password, letters, digits, symbols):
    # all of them
    test = string.ascii_letters + str(string.digits) + string.punctuation

    # contours test based on given truth value
    if not symbols and not digits:
        test = test[:52]
    elif not symbols:
        test = test[:62]
    elif not digits:
        test = test[:52] + test[len(string.ascii_letters) + len(string.digits):]
    if not letters:
        test = test[52:]

    # list of tuples of every possible test
    # find a more efficient method for odometer - cartesian is too memory intensive
    cartesian = list(itertools.product(test, repeat=len(password)))

    count = 0
    # loops through the list of tuples to find password
    for couple in cartesian:
        count += 1
        code = ''.join(couple)
        if code == password:
            return f"{password} was cracked in {count} guesses."


def main():
    digits = False
    symbols = False
    letters = False
    while True:
        password = input("Enter a password: ")

        # Checks truthiness of type & doubles as a white space checker
        for char in password:
            if char in str(string.digits):
                digits = True

            if char in string.punctuation:
                symbols = True

            if char in string.ascii_letters:
                letters = True

        # validates to make sure the user didn't just enter white space
        if letters or digits or symbols:
            common = pass_check(password)
            print(common)

            # if password not common, breaker runs
            if 'Unique' in common:
                print(breaker(password, letters, digits, symbols))
                return
            return

        print("Please enter a valid Password.")


main()

# most challenging part was the odometer
