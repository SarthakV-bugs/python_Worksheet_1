#EX 1
# Write a function to find the sum and average of numbers in a list, L.

def sum_avg(L):
    n=len(L)
    sum=0
    for i in range(0,n):
        sum = sum + L[i]
        avg= sum//n

    print(sum)
    print(avg)


#Ex2
#Write a function to find the minimum and maximum number in a list, L.

def min_max(L):

    max=L[0]
    min=L[0]
    for i in L:
        if i>max:
            max=i
        if i<min:
            min=i
    print(f'max value is {max}')
    print(f'min value is {min}')

#Ex 3
# Write a program to find the even numbers in a list, L.

def even_numbers(L):
    even_list = []
    for i in L:
        if i%2==0:
            even_list.append(i)
    print(even_list)

#Ex4
# Write a program to print the duplicate elements in a list, L.

def dupli(L):
    dupl_list = []
    uniq_list = []

    for x in L:
        if x not in uniq_list:
            uniq_list.append(x)
        elif x not in dupl_list:
            dupl_list.append(x)

    print(dupl_list)

#Ex5
# Write a program to subtract two matrices, m1 and m2, using a list of lists
def subtract_matrices(m1,m2):

    diff = []

    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j]-m2[i][j])
        diff.append(row)
    return diff

# Ex6
# Write a program to extract elements of a list, if it occurs more than k times.

def extract_elem(L,k):

    res = []

    for i in L:
        count = L.count(i)
        if count > k and i not in res: #to not get multiple entries
            res.append(i)
    return res

#Ex7
# Write a program to remove all occurrences of an element from a list, L.
def remove_occ(L,element):
    L = [i for i in L if i != element]
    return L

#
# i=0
#    while i<len(L):
#         if L[i]==element:
#             L.pop(i)
#         else:
#             i+=1
#    return L


#Ex8
# Write a program to extract words from a string list, L whose first character is k.

def extract_K_word(str_L):
    k_word = []
    for word in str_L:
        for i in word:
            if i == 'k':
                k_word.append(word)
    return k_word


#Ex9
# Write a program to iterate over a dictionary and print key and values

def dict_iter(dict1):
    for key, value in dict1.items():
        print(f"Key: {key}, Value: {value}")

#Ex10
# Write a program to sum all values of a dictionary.

def sum_dict(dict2):
    sum=0
    for value in dict2.values():
        sum += value
    print(sum)

#Ex11
# Write a program to find the maximum and minimum value of a dictionary

def max_min_dict(dict2):
    for value in dict2.values(): #getting the first value and then comparing for max and min
            first_value = value
            break

    max_val = first_value
    min_val = first_value

    for value in dict2.values():
        if value > max_val:
            max_val = value
        if value < min_val:
            min_val = value

    print(f'maximum value of dict2: {max_val}')
    print(f'minimum value of dict2: {min_val}')


#Ex12
# Write a program to implement an insertion sort algorithm

def insertion_sort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

#Ex13
# Given a dictionary with a values list, extract the key whose value has the most unique values.
# Input : test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# Output : "Best"
# Explanation : 3 (max) unique elements, 9, 6, 5 of "Best".

def most_uniq_value_inkey(dict3):
    max_count = 0 #initialize the max as 0
    res_key = []
    for key, values in dict3.items():
        uniq_values = set(values) #use set to get unique values

        #get the count of this uniq_values
        uniq_C = len(uniq_values)
        if uniq_C > max_count:
            max_count = uniq_C
            res_key=key

    return res_key



#Ex14
# Remove all duplicate words from given sentence using a dictionary

def rem_dupl_dict(sentence):
    words = sentence.split() #splitting the sentence into words
    uniq_dict = {}  #to store keys

    for word in words:
        uniq_dict[word] = None

    new_sent_uniq = ' '.join(uniq_dict.keys())
    return new_sent_uniq





def main():
    #Ex 1,2,3,4
  num = input('Enter the elements separated by comma: ')
  L = [int(i) for i in num.split(',') ]
  n=len(L)
  print(L)
  sum_avg(L)
  min_max(L)
  even_numbers(L)
  dupli(L)

    #Ex5
  m1 = [[1, 2, 3],
        [3, 4, 5],
        [6, 7, 8]]
  m2 = [[12, 32, 32],
        [21, 54, 76],
        [65, 43, 17]]

  print(subtract_matrices(m1, m2))


    #Ex6
  k = int(input('Enter the times after which the element needs to be extracted: '))
  print(extract_elem(L,k))


    #Ex7
  element = int(input("Enter the element to be removed: "))
  print(remove_occ(L,element))


    #Ex8
  str_L = [word for word in input('Enter the words: ').split(',')]
  print(str_L)
  print(extract_K_word(str_L))

    #Ex9
  dict1 = {1: 'Rahul', 2: 'Suresh', 3: 'Virendra'}
  dict_iter(dict1)

    #Ex10
  dict2 = {'Carrot': 21, 'Tomato': 56, 'banana':98}
  sum_dict(dict2)

    #Ex11
  max_min_dict(dict2)

    # Ex12
  array = [98,21,78,53,18]

  print("Original array:", array)
  insertion_sort(array)
  print("Sorted array:", array)



    #Ex13
  dict3 = {
        "Gfg": [5, 7, 7, 7, 7],
        "is": [6, 7, 7, 7],
        "Best": [9, 9, 6, 5, 5]
    }
  res = most_uniq_value_inkey(dict3)
  print(f'key with most unique values in value: ', res)



    #Ex14
  sentence = 'we are learning dict and now we are removing words repetitive words from dict'
  res = rem_dupl_dict(sentence).capitalize()
  print(f'new sentence after uniq removed:', res)






if __name__ == "__main__":
    main()




