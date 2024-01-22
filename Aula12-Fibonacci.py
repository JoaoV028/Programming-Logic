def proximo_fibonacci(a, b):
    c = a + b
    print (c)
    return b, c

t1 = 0
print (t1)

t2 = 1
print (t2)

for _ in range (3,11) :
    t1, t2 = proximo_fibonacci(t1,t2)