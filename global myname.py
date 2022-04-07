from re import X
def myfunc():
    global myname
    myname = "hooman" 
myfunc()
print("your age is "+ myname)