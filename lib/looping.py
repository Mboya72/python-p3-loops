# !/usr/bin/env python3

def happy_new_year():
    number = 10
    while number > 0:
        print(number)
        number -= 1
    print("Happy New Year!")

happy_new_year()
pass

def square_integers(int_list):
    return [num ** 2 for num in int_list]

numbers = [1, 2, 3, 4, 5]

squared_numbers = square_integers(numbers)

print(squared_numbers)

pass

def fizzbuzzPrinter():
    for num in range(1, 101):  
        print(fizzbuzz(num))

def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

pass


