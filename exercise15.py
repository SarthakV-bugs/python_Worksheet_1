def occurrence_of_word(s,w):


    new_sent = s.split()

    count =0
    for word in new_sent:
        if word== w:
            count +=1
    return count


def main():
    s = input("Enter the sentence:")
    w = input("Enter the word: ")
    print(occurrence_of_word(s,w))


if __name__ == "__main__":
    main()