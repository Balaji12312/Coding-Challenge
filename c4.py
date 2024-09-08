def reduce_ticket_cost(ticket_price, k):
  if k >= len(ticket_price):
    return 0  
  digits = sorted(ticket_price)
  for i in range(k):
    digits.pop(0)
  reduced_price = int(''.join(digits))
  return reduced_price
ticket_price = input("Enter the ticket price: ")
k = int(input("Enter the number of digits to remove: "))
reduced_price = reduce_ticket_cost(ticket_price, k)
print("Reduced ticket price:", reduced_price)