# a = 5
# b = 10
# c = 20

a, b, c = 2, 10, 20

a += 5      # a = a + 5
a -= 5      # a = a - 5
a *= 5      # a = a * 5
a /= 5      # a = a / 5
a %= 5      # a = a % 5
a **= 5     # a = a ** 5
a //= 5     # a = a // 5

values = (1, 2, 3, 4, 5)

# a, b, *c = values
# a, *b, c = values
*a, b, c = values

print(a,b,c)