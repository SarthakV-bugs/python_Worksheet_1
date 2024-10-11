def remove_whitespace(s):
    new_string = s.lstrip()
    return new_string

def main():
    user_input= input("Enter the string with whitespaces: ")
    result = remove_whitespace(user_input)
    print(result)


if __name__ == "__main__":
        main()