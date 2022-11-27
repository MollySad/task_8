x = 1
y = 1
z = 1
n = 2

result = [
    [val1, val2, val3]
    for val1 in range(0, x+1)
    for val2 in range(0, y+1) 
    for val3 in range(0, z+1)
    if val1 + val2 + val3 != n    
]

print(result)