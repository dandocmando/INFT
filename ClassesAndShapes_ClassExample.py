class A:
    #here a and b both are class variable of class A.
    #and initialize with 0.
    a = 0
    b = 0
    def funA(self,x,y):
        A.a = x
        A.b = y
class B(A):
    def __init__(self):
        #access class A variable from class B.
        print("variable of class A =",A.a)
        print("variable of class B =",A.b)
#class A object
ob1 = A()
#user input no.
a=int(input("enter 1st number "))
b=int(input("enter 2nd number "))
#class B object
ob = B()
#class A method call
ob.funA(a,b)
