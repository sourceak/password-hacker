import string


# loop through file to get ranking
def pass_check(password):
    f = open('100000-most-common-passwords.txt', 'r')

    count = 0

    for line in f:
        count += 1
        line = line[:-1]
        if line == password.lower():
            f.close()
            return f"{password}: ❌ (#{count})"
    return f"{password}: ✅ (Unique)"


# ask the user to input a password
def main():
    while True:
        password = input("Enter a password: ")
        for letter in password:
            if letter in string.ascii_letters or letter in string.punctuation or letter in string.digits:
                print(pass_check(password))
                return
        print("Please enter a valid Password.")


main()
