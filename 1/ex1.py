#Exercício 1
def gi(n):
  degree = 0
  
  while n > 9:
    sum = 0
    for i in str(n):
      sum += int(i)
    n = sum
    print(n)
    degree += 1
    
  if n == 9:
    return [True,degree]
  else:
    return [False, degree]

    

print(gi(9))
print(gi(999999999999999999999 ))
print(gi(9999999999999999999999999999998))
