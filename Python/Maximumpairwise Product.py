import random
def findmax(l1):
    max = float('-inf')

    for i in l1:
        if i>max:
            max = i
    return max        

def second_max(l1, max_num):
    max = float('-inf')

    for i in l1:
        if i>max and  i != max_num:
            max = i
    return max

a = int(input())
l1 = []
lis = str(input())

lis2 = lis.split(' ')

for i in lis2:
    b = int(i)
    l1.append(b)

max_num = findmax(l1) 
sec_max = second_max(l1,max_num)

print(max_num*sec_max)

# def stress_test():
#     n = random.randint(2,10)
#     print(n) 
#     list = []
#     i=0
#     while i<n:
#         int2 = random.randint(0,1000000)
#         list.append(int2)
#         i = i+1
    
#     while i<n:
#         print(list[i]).spilt(' ')
#         i = i+1

# stress_test()      