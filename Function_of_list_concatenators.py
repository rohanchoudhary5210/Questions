#LIST CONCATENATOR
l1=[1,2,3,4,5,6,7,8,9]
l=['rohan', 'jiya']
def lists_concat(a,b):
    if type(a)==list and type(b)==list:
        return a+b
    else:
        return "There is some error in the input"
