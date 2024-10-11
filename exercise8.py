

def print_half(s):
    halfStr = ""
    for i in range(0,len(s)//2):
            halfStr += s[i]
    print(halfStr)



def main():
    user_input = input("Enter the string: ")
    print_half(user_input)

if __name__ == "__main__":
        main()