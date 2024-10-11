occ= {}

def occurrence(s):
    for char in s:

        if char in occ:
            occ[char] += 1
        else:
            occ[char] = 1
    # print(occ)

    max_value = 0
    max_key = None
    for key, value in occ.items(): #use .items to access key, value pair
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

# def max_occurrence(occ):
#     v = list(occ.values())
#     k = list(occ.keys())
#     return k[v.index(max(v))]


def main():
    user_input = input("Enter the string: ")
    # occurrence(user_input)
    # max_occurrence()
    result = occurrence(user_input)
    print(result)


if __name__ == "__main__":
        main()