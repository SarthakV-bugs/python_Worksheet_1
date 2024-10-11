def anagrams(s,s2):

    #check for length; as anagrams need to have same length
    if len(s) !=  len(s2):

         return False

    #check for the count of the character occurring
    for char in s:
     if char.count(s) == char.count(s2):
        return True
     else:
         return False

def main():

    s = input("Enter the string 1:")
    s2 = input("Enter the string 2: ")
    print(anagrams(s,s2))

if __name__ == "__main__":
    main()

