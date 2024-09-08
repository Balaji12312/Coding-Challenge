def is_stepping_number(num):
  prev_digit = None
  while num > 0:
    digit = num % 10
    if prev_digit is not None and abs(digit - prev_digit) != 1:
      return False
    prev_digit = digit
    num //= 10
  return True
def find_stepping_numbers(n, m):
  stepping_numbers = []
  for num in range(n, m + 1):
    if is_stepping_number(num):
      stepping_numbers.append(num)
  return stepping_numbers
n, m = map(int, input("Enter the range (n, m): ").split())

stepping_numbers = find_stepping_numbers(n, m)
print("Stepping numbers in the range:", stepping_numbers)