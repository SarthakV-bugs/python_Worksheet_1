def bin_to_dec(b):

    decimal = 0
    power = 0

    for i in range(len(b)-1 ,-1, -1): #reverse iteration
        bin_dig= int(b[i])

        decimal += bin_dig * (2 ** power)
        power += 1

    return decimal


def main():
   b = input("Enter the binary: ")
   print(bin_to_dec(b))

if __name__ == "__main__":
        main()