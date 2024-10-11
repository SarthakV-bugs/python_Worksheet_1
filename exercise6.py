
def check_for_prime(N):

    if N <= 1: # 0,1 are not prime numbers.
        return False

    if N % 2 != 0 and  N % 3 != 0 and N % 5 != 0 and N % 7 != 0:
        return True
    elif N == 2 or N == 3 or N == 5 or N == 7:
        return True
    else:
        return False



def main():
    check_for_prime(6)
    result = check_for_prime(6)
    print(result)

if __name__ == "__main__":
        main()