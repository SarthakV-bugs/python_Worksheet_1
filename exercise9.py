def print_alt_char(s):

    print(s[::2])

def main():
    user_input = input("Enter the string: ")
    print_alt_char(user_input)
if __name__ == "__main__":
        main()