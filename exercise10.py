
def concatenate_str(s1,s2):
    # s3 = s1 + s2
    # return s3
    return ''.join([s1,s2])

   

def main():
    s1 = input("Enter the first string: ")
    s2= input("Enter the second string ")
    res=concatenate_str(s1, s2)
    print(res)


if __name__ == "__main__":
        main()