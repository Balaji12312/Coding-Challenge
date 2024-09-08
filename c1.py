def find_two_distinct_numbers(arr):
    xor = 0
    for num in arr:
        xor ^= num  
    rightmost_set_bit = xor & -xor  
    num1 = num2 = 0
    for num in arr:
        if num & rightmost_set_bit:
            num1 ^= num  
        else:
            num2 ^= num  
    return sorted([num1, num2])  
A = list(map(int, input("Enter the array elements separated by space: ").split()))
result = find_two_distinct_numbers(A)
print(result)
