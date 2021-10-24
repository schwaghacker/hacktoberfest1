def prime(n):
  if n==2:
    return 
  if n%2==0:
    return False
  for i in range(3, n+1, 2):
    while i*i<=n:
        if n%i==0:
          return False
  return True
a = int(input("Please give your number to check if whether is a prime number or not\n"))
if prime(a):
  print(f'{a} is a prime number')
else:
  print(f'{a} is not a prime number')
