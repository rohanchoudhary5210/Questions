#Enumerate is used to keep a list of iterations
# For i in enumerate(l) will return a tuple of (index of i,i) {where i is the element of list l}

l=[1,2,3,4,5,6,9,77,10]
def index(l):
    l1=[]
    if type(l)==list:
        for i in enumerate(l):
            l1.append(i)
        return l1
    else:
        return "It is not a list"
