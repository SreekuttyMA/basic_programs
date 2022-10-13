text = "learn python"

print(text[0]) 
print(text[-1])
print(text[6])
print(text[1:6])
print(text[::-1]) # reverse............ text  ----- txet
#----------------------------------------------------------------------------------------
a=text.split() #### convert string into list
print(a)
print(' '.join(reversed(a))) # (((join is used for convert list to string)))O/P-reverse.............. python learn
#----------------------------------------------------------------------------------------
b=text.count(' ')   # ...to count number of words
b=b+1
print(b)
#----------------------------------------------------------------------------------------
c=text.find('python')  #............. to get index value
print(c)

#################   OR   ###################


b="AttributeError: 'str' object has no attribute 'sort'"


A="TypeError: str.capitalize() takes no arguments (1 given)" # toget index value
print(A.index('no'))
#----------------------------------------------------------------------------------------
print(len(text)) # start with 1

print(text.count('a')) # how many times occur the letter

d = text.capitalize() # to capitalize the first word's first letter 
print(d)

#----------------------------------------------------------------------------------------

string ="python"
string1 ="highlevel"
print('{} is a {} language'.format(string,string1)) ### its output is---> python is a highlevel language
x = "SREEKUTTY.M.A"
print()













