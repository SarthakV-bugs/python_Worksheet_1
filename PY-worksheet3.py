#exercise1
# You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
# Create a variable named capitalized_fruits and use list comprehension syntax to produce output like
# ['Mango', 'Kiwi', 'Strawberry', etc...].
from bdb import Breakpoint

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

#exercise 2
# You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
# Make a variable named fruits_with_only_two_vowels. Use list comprehension to produce
# ['mango', 'kiwi', 'strawberry'],a list of fruits with only two vowels.

#without comprehension
fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_only_two_vowels = []

for fruit in fruits:
    vowels_count = 0
    for i in fruit:
        if i in 'aeiou':
            vowels_count += 1

    if vowels_count == 2:
        fruits_with_only_two_vowels.append(fruit)

print(fruits_with_only_two_vowels)

#with comprehension:
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(1 for i in fruit if i in 'aeiou')==2]
print(fruits_with_only_two_vowels)

#exercise 3
# Given org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"], org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"],
# find all similar pairs of genome sequences (one sequence from org1, one from org2) using list comprehension.
# “Similar” means: similarity(seq1, seq2) > threshold

org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]

# Set the threshold
threshold = 0.5

# Use list comprehension
similar_pairs = [
    (seq1, seq2) for seq1 in org1 for seq2 in org2
    if len(seq1) == len(seq2) and sum(1 for a, b in zip(seq1, seq2) if a == b) / len(seq1) > threshold
]


print(similar_pairs)

# Exercise 4
# Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Create a dictionary of numbers and their squares, excluding odd numbers using dictionary comprehension


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict1 = {n:n*n for n in num if n % 2==0}
print(dict1)

#Exercise5
# sentence = "Hello, how are you?". Write a dictionary comprehension to map words to their reverse in a sentence.
# The output should be - {'Hello,': ',olleH', 'how': 'woh', 'are': 'era', 'you?': '?uoy'}

sentence = "Hello, how are you?"
# without comprehension
for word in sentence.split(' '):
    print(word[::-1])

#with comprehension
rev_sen = {word:word[::-1]for word in sentence.split()}
print(rev_sen)

#Exercise 6

# Write  a lambda function to sort a list of strings by the last character

list_str = ['no','way','home']
sorted_str = sorted(list_str, key=lambda x:x[-1])
print(sorted_str)


#Exercise 7
# Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

#arranging them on the basis of number line i.e. negative number before the positive

A= [20,-5,14,-42,12,-9,-7]

new_A = sorted(A, key=lambda x: x>=0)
print(new_A)


#Exercise 8
import time


def logging(func):
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__} with args: {args},kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'result: {func.__name__} returned: {result}')
        return result
    return wrapper


@logging
def add(a,b):
    return a+b
add(2,4)


#Exercise 9

def log_time(func):
    def wrapper(*args):
        start = time.time()
        print(f'Starting {func.__name__}:',start)
        result = func(*args)
        end = time.time()
        print(f'Finished {func.__name__} with args: {args}:',end)
        print(f'Total time:', end-start)
        return result
    return wrapper



@log_time
def fibonacci(n):
    time.sleep(2)
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)



# Exercise 10

def division(a,b):
    try:
        output = a/b
        print(f'The result of {a} divided by {b}: {output}')

    except ZeroDivisionError:
        print('division by zero')
    except ValueError:
        print('Error: Invalid value. Please enter a number.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print('Division done')

division(10,3)
division(10,0)
division(10,'1')
division('a','b')




#Exercise 11

class FormulaError(Exception):
    pass

def user_entry(user_input):

    input_l = user_input.split()
    if len(input_l) != 3:
        raise FormulaError("Input must be consisting of three elements i.e. 'n1', 'op', 'n2' ")
    n1, op, n2 = input_l

    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        raise FormulaError("n1 and n2 must be numbers")
    return n1, op, n2


def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  raise FormulaError("Operation must be either +/-")


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = user_entry(user_input)
  result = calculate(n1, op, n2)
  print(result)


