#Sum of elements

lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")

total = 0
sum_of_list = 0
try:

def listsum(lst):
    total = 0
    i = 0
    while i < len(lst):
        total = total + lst[i]
        i = i + 1
    return total

totalsum = listsum(lst);
print('Sum of List using function: ', totalsum)

