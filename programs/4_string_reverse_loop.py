a="sree"
for i in a:
    print(i)
    
### to find len
# for i in range(len(a)):
#     print(i,a[i])
###########reverse of a string    

# a1=""
# for i in a:
#     a1=i+a1
# print(a1)


# ###########using function#################################################
def rev(string):
    s=""
    for i in string:
        s=i+s
    print(s)
rev("sree")


##################################################################################
def stringrev(string):
    string1=string[::-1]
    print(string1)
stringrev("hello")

#################################################################################
  
name="sreekutty"
new = ""
for i in name:
    new = i+new
print(new)
if(new==name):
    print("palindrome")
else:
    print("not")
  
