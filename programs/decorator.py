def outer(a):
    def inner():
        print("welcome")
        return a()
    return inner
@outer
def display():
    print("hai hello")
display()




def newfun(sree):
    def friend():
        print("ka ku me")
        return sree()
    return friend

@newfun
def display():
    prin
  
# f = outer(display)
# f()