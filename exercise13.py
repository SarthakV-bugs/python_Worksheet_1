def replace_char(s,c,d):
    new_string = s.replace(c,d)
    return new_string


def main():
   s = input("Enter the string: ")
   c = input("Enter the character to be replaced: ")
   d = input("Enter the character to replace with: ")
   result = replace_char(s,c,d)
   print(result)


if __name__ == "__main__":
        main()