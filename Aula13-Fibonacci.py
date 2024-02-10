def proximo_fibonacci(n1, n2):
    n3 = n1 + n2
    return n3

t1 = 0
print(t1)
t2 = 1
print (t2)

for i in range(3,11):
    t3 = proximo_fibonacci(t1,t2)
    print (t3)
    t1 = t2
    t2 = t3
