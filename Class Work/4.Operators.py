#Arithmetic Operators
a=20
b=10
print("**Arithmetic Operations**\nAddition: ",a+b,"\nSubtraction: ",a-b,"\nMultiplication: ",a*b,
      "\nDivision: ",a/b,"\nFloor Division: ",a//b,"\nModulus: ",a%b,"\nExponentiation: ",a**b)

#Comparison Operators
print("\n**Comparison Operations**\nEqual to: ",a==b,"\nNot equal to: ",a!=b,"\nGreater than: ",a>b,"\nLess than: ",a<b,
      "\nGreater than or equal to: ",a>=b,"\nLess than or equal to: ",a<=b)

#Assignment Operators
a=10 #assign
print("\n**Assignment Operations**\nAssign: ",a)
a+=10
print("Add & assign: ",a)
a-=10
print("Subtract & assign: ",a)
a*=4
print("Multiplication & assign: ",a)
a/=4
print("Divison & assign: ",a)
a=10 #reassign
a//=2
print("Floor divison & assign: ",a)
a%=3
print("Modulus & assign: ",a)
a**=3
print("Exponentiate & assign: ",a)

#Logical Operators
a=20
b=10
print("\n**Logical Operations**\nAND: ",a%2==0 and b%2==0,
      "\nOR: ",a%3==0 or b%2==0,"\nNOT: ",not(a<10))

#Membership Operators
sequence='sirisha'
print("\n**Membership Operations**\nSequence - in: ",'a' in sequence,"    not in: ",'a' not in sequence)
list=['sirisha','hitha']
print("List - in: ",'sirisha' in list,"    not in: ",'hitha' not in list)
tuple=('sirisha','hitha')
print("Tuple - in: ",'sirisha' in tuple,"    not in: ",'hitha' not in tuple)
set={'sirisha','hitha'}
print("Set - in: ",'sirisha' in set,"    not in: ",'hitha' not in set)
dictionary={'Name':'Sirisha','Course':'DS','Batch':'15'}
print("Dictionary - in: ",'Name' in dictionary,"    not in: ",'Batch' not in dictionary)

#Identity Operators
a=[1,2,3,4]
b=[1,2,3,4]
c=a
print("\n**Identity Operations**\nMemory allocation of a: ",id(a),
      "\nMemory allocation of b: ",id(b),"\nMemory allocation of c: ",id(c),
      "\nis: ",a is c,"\nis not: ",a is not c)

#Bitwise Operators
a=5
b=3
print("\n**Bitwise Operations**\nAND: ",a&b,"\nOR: ",a|b,"\nXOR: ",a^b,
      "\nNOT: ",~a,"\nLeft shift: ",a<<1,"\nRight shift: ",b>>1)