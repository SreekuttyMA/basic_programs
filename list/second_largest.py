
lst=[]
n=int(input("enter the range"))
for i in range(n):
    ele=int(input())
    lst.append(ele)
lst.sort(reverse=True)
print(lst)
print(lst[1])



