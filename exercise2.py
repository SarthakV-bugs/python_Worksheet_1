
def dec_to_bin(D):

    binary= '' #created an empty str

    while D > 0:
        r = D % 2
        binary = str(r) + binary #reverse order printing?
        #binary = binary + str(r) #typecasted int(r) into str to join into the original binary string
        D = D // 2

    return binary



def main():
    D= int(input("Enter the decimal number:"))
    result= dec_to_bin(D)
    print(result)

if __name__ == "__main__":
        main()