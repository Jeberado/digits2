digit = int(input('Write your digit here: '))

a5 = digit % 10
a4 = (digit//10) % 10
a3 = (digit//100) % 10
a2 = (digit//1000) % 10
a1 = digit // 10000

digit2 = a5*10000 + a4*1000 + a3*100 + a2*10 + a1
print(digit2)