# #ex1
# def square_num(N):
#    for i in range(N):
#        i = i**2
#        yield i
# a = int(input())+1
# gen = square_num(a)

# while a > 0:
#    print(next(gen))
#    a= a-1

#ex2
#def even_num(A):
#    for i in range(A):
#        if i%2 == 0:
#                 
#            yield(i)
#v = int(input())+1
#num = even_num(v)

#while v > 0:
#    print(next(num), sep=',', end='')
#    v= v-1
#ex2_1
# def even_num(A):
#    for i in range(A):
#        if i % 2 == 0:
#            yield i

# v = int(input()) + 1
# num = even_num(v)

# res = []
# for n in num:

#    res.append(n)
# print(*res, sep = ',')
# ex3
# def just_num(B):
#     for i in range(B):
#         if i%4 == 0 and i%3 == 0:
#             yield i
# v = int(input())+1
# num = just_num(v)
# print(num)
# while v > 0:
#     print(next(num))
#     v = v-1
#ex3_1
# def just_num(B):
#     for i in range(B):
#         if i%4 == 0 and i%3 == 0:
#             yield i
# v = int(input())+1
# num = just_num(v)

# for n in num:
#     print(n)
    
#ex4
def sqr_num(A, B):
    for i in range(A, B):
        i = i**2
        yield i
a = int(input())
b = int(input())+1

num = sqr_num(a, b)

for n in num:
    print(n)

#ex5
# def down(d):
#     for i in range(d):
#         i = i-1
#         yield i
# c = int(input())
# num = down(c)
# while c >= 0:
#     print(c)
#     c= c-1