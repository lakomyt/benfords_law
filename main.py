from random import randint
from matplotlib import pyplot

def fibonacci(number_of_elements):
    a = 1
    b = 1
    numbers=[a,b]
    for n in range(0,number_of_elements):
        c = a
        a = b
        b = a+c
        numbers.append(b)
    return numbers

def random_numbers(number_of_elements):
    numbers=[]
    for n in range(0,number_of_elements):
        numbers.append(randint(1,1000000))
    return numbers

def natural_numbers(number_of_elements):
    numbers=[]
    for n in range(1,number_of_elements+1):
        numbers.append(n)
    return numbers

def file(filename):
    with open(filename, "r") as data:
        numbers = data.read().split("\n")
    return numbers


print("\
Test benford's law for:\n\
    1. Fibonacci sequence\n\
    2. Random numbers\n\
    3. Natural numbers\n\
    4. Numbers from file")

f = int(input("Select option: "))

if (f == 1):
    number_of_elements = int(input("How many numbers? "))
    numbers = fibonacci(number_of_elements)
    title = f"fibonacci sequence, {number_of_elements} elements"
elif (f == 2):
    number_of_elements = int(input("How many numbers? "))
    numbers = random_numbers(number_of_elements)
    title = f"random numbers, {number_of_elements} elements"
elif (f == 3):
    number_of_elements = int(input("How many numbers? "))
    numbers = natural_numbers(number_of_elements)
    title = f"natural numbers, {number_of_elements} elements"
elif (f == 4):
    filename = input("Enter file path: ")
    numbers = file(filename)
    title = ""

amounts = [0,0,0,0,0,0,0,0,0,0]

for number in numbers:
    amounts[int(str(number)[0])] = amounts[int(str(number)[0])] + 1
print(amounts)
print(sum(amounts))
amounts[:] = [round(x / sum(amounts)*100,2) for x in amounts]
for x in range(1,len(amounts)):
    print(f"{x}: {amounts[x]}%")

pyplot.bar([1,2,3,4,5,6,7,8,9], amounts[1:])
pyplot.xticks([1,2,3,4,5,6,7,8,9])
pyplot.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.4)
pyplot.xlabel("Digit") 
pyplot.ylabel("Occurence at the beginning of a digit in %")
pyplot.title(f"Benford's law, {title}") 
pyplot.show()
