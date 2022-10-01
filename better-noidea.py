#List comprehensions can do this easily, esp when you leverage that True == 1 and False == 0:

n, m, sc_ar = raw_input().split(), raw_input().split()



A = set(raw_input().split())
B = set(raw_input().split())
print sum([(i in A) - (i in B) for i in sc_ar])
