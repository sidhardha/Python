# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 40:
    print(a, end=',')
    a, b = b , a+b