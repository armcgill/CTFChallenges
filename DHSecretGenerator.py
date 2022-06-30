
mod = int(input('Public mod: '))
base = int(input('Public base: '))

a_secret = int(input('A secret: '))
b_secret = int(input('B secret: '))

A_public = (base ** a_secret) % mod
B_public = (base ** b_secret) % mod

print('=================')

print('A public = ' + str(A_public))
print('B public = ' + str(B_public))

a_shared = (B_public ** a_secret) % mod
b_shared = (A_public ** b_secret) % mod

print('A shared secret = ' + str(a_shared))
print('B shared secret = ' + str(b_shared))