numbers = [10, 9, 10, 10, 9, 8]

clean_numbers = [
    number 
    for number in numbers 
    if numbers.count(number) != 1
]

print(clean_numbers)