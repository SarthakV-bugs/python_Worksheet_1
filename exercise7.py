def ind_digits(n):

    digits = ''

    for i in str(n):
        digits += i

    return digits





def main():
    n = int(input("Enter the number:"))
    result=ind_digits(n)
    for digits in result:
        print(digits)


if __name__ == "__main__":
        main()