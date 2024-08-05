#!/usr/bin/python

for num in range(10, 21):
  is_prime = True
  if num <= 1:
    is_prime = False
  elif num <= 3:
    is_prime = True
  elif num % 2 == 0 or num % 3 == 0:
    is_prime = False
  else:
    i = 5
    while i * i <= num:
      if num % i == 0 or num % (i + 2) == 0:
        is_prime = False
        break
      i += 6

  if is_prime:
    print(f"{num} is a prime number")
  else:
    for i in range(2, num):
      if num % i == 0:
        print(f"{num} is divisible by {i}")
        break
