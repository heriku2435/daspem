#operator != (tidak sama dengan)
x = 2
y = '2'

z = x != y #true
print(z)

#operator > lebih besar dari
a = 5 > 2 #true
print(a)

b = 10 < 5 #false
print(b)

#operator logika and , OR, NOT
logikaAnd = z & a
logikaAndLagi = z and b
print(logikaAnd) #true
print(logikaAndLagi) #false

#operator OR
logikaOr = z or b
print(logikaOr) #true

#operator NOT
logikaNot = not(z)
print(logikaNot) #false