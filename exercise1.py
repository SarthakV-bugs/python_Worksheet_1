def sum_of_sq(n):

    sum=0
    for i in range(1,n+1):
        sq= i ** 2
        sum= sum + sq

    return sum






def main():
    n= int(input("Enter the number:"))
    print(sum_of_sq(n))

if __name__ == "__main__":
    main()