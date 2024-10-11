
from exercise2 import dec_to_bin

def count_1(bin_dig):
    count = 0
    for i in range(0,len(bin_dig)):
        if bin_dig[i] == '1':
            count = count+1

    return count




def main():
    n = int(input("Enter the decimal number:"))
    bin_dig=dec_to_bin(n)
    print(bin_dig)
    count_1(bin_dig)
    print(count_1(bin_dig))



if __name__ == "__main__":
    main()