def power(base, exponent):


    power_num= base ** exponent

    return power_num



def main():
    base = int(input("Enter the base:"))
    exponent = int(input("Enter the exponent:"))
    result=power(base, exponent)
    print(result)


if __name__ == "__main__":
        main()