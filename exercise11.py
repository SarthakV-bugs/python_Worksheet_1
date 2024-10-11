def first_occurrences(s,c):

    for char in s:
        if char == c:
         print(s.index(char))
         break



def main():
 s = input("Enter the string: ")
 c = input("Enter the character: ")
 first_occurrences(s,c)

if __name__ == "__main__":
         main()