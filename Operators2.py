a = 60      # 60 == 0011 1100
b = 13      # 13 == 0000 1101
c = 0       # 0 == 0000 0000

c = a & b   # 12 == 0000 1100
print("Line 1 - value of c is", c)

c = a | b   # 61 == 0011 1101
print("Line 2 - value of c is", c)

c = a ^ b   # 49 == 0011 0001
print("Line 3 - value of c is", c)

c = -a  # -61 == 1100 0011
print("Line 4 - value of c is", c)

c = a << 2;  # 240 == 1111 0000
print("Line 5 - value of c is", c)

c = a >> 2;  # 15 == 0000 1111
print("Line 6 - value of c is", c)


a = 21
b = 13     
c = 0       

c = a + b 
print("Line 1 - value of c is", c)

c += a 
print("Line 2 - value of c is", c)

c *= a 
print("Line 3 - value of c is", c)

c /= a 
print("Line 4 - value of c is", c)
c = 2
c %= a 
print("Line 5 - value of c is", c)

c **= a
print("Line 6 - value of c is", c)

c //= a
print("Line 7 - value of c is", c)


#identify programs

a = 20
b = 20

if (a is b):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b does NOT have the same identity")

p = 44
q = 55

if (a is b):
    print("Line 3 - p and q have different identity")
else:
    print("Line 3 - p and q have the SAME identity")

#Membership Operators

x = "Hello world"
y = {1:'a',2:'b'}

print('H' in x)

print("Hello" not in x)

print(1 in y)

print('a' in y)