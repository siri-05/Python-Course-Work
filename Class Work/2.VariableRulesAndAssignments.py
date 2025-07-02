myvar=10 #valid and case-sensitive
Myvar=10 #valid and case-sensitive
myvar1=10 #valid
my_var=10 #valid
_myvar=10 #valid
'''
1myvar=10 #invalid
@myvar=10 #invalid
my@var=10 #invalid
my var=10 #invalid
'''
a=10 #assignment
b=20
c=30
d=e=f=40 #same value assignment
g,h,i=50,60,70 #multiple assignment
print("a b c d e f g h i: ",a,b,c,d,e,f,g,h,i,"\nBefore swapping a and b: ",a,b)
a,b=b,a #swapping a and b
print("After swapping a and b: ",a,b)
b=20 #reassignment
del a
print(a)
'''
Traceback (most recent call last):
  File "C:/Users/pddwm/AppData/Local/Programs/Python/Python313/Test.py", line 45, in <module>
    print(a)
NameError: name 'a' is not defined
'''