
x, y = 2, 3              # Input style 01
add = x+y
print(add)

print('ENTER AN INPUT')  # Input style 02
a = int(input())         # because Input function is by default a string
b = int(input())
c = int(input())

Sum = a+b+c
print(Sum)                                                      # Print style01
print(str(a) + '+' + str(b) + '+' + str(c) + '=' + str(Sum))    # Print style02
print(a, '+', b, '+', c, '=', Sum)                              # Print style03
print('{}+{}+{}={}'.format(a, b, c, Sum))                       # Print style04


d = int(input('/n ENTER A NUMBER :'))      # Input style 03
total = d + Sum

print(total)


p = 6.8
round(p)
print(p)













