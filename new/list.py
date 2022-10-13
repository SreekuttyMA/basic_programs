# def list1(a):
#     return max(set(a),key=a.count)
# a=[1,2,1,2,3,4,3,1,1,5,6,1]
# print(list1(a))

# def Most(a):
#     dict1={}
#     count,item=0,''
#     for i in reversed(a):
#         dict1[i]=dict1.get(i,0)
#         if dict1[i]>=count:
#             count,item=dict1[i],i
#         return item




a=[1,2,1,2,3,4,3,1,1,5,6,1]
# print(Most(a))
count=0
l=[]
for i in a:
    l.append(i)
    if i ==i :
        count=count+1
        
print(l,count)
    


