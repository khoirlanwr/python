# program to insert fibonacci number
def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2) 

fib_list = [0, 1]

number = input("Masukkan jumlah deret fibonacci: ")

for num in range(2, number):
  result = fib(num-1) + fib(num-2)  
  fib_list.insert(num, result)
  
print fib_list
