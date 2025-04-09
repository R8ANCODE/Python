#conversion data types

a = float(1)

b = int(5.5)

c = complex(1)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#string operations

#concetation
firstname = 'freeda'
lastname = 'gomam'
fullname = firstname+ ' ' +lastname
print("your")
print(fullname)

#repetition
firstname = 'freeda'
lastname = 'gomam'
fullname = firstname * 3
print("your")
print(fullname)

#sliced
firstname = 'freeda'
lastname = 'gomam'

print(firstname[1])
print(lastname[0])

#sliced range
firstname = 'freeda'
lastname = 'gomam'

print(firstname[0:2])
print(lastname[0:3])

#membership
firstname = 'freeda'
lastname = 'gomam'

print('a' in lastname)
print('b' in firstname)

#membership
firstname = 'freeda'
lastname = 'gomam'

print('a' not in lastname)
print('b' not in firstname)
