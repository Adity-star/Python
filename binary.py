def to_binary(n):
   if n == 0:
       return "0"
   elif n == 1:
       return "1"
   else:
       return to_binary(n // 2) + str(n % 2)

n = 23
print("Binary:", to_binary(n))
