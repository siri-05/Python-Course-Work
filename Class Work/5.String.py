#IMMUTABLE
s='Siri'
print(s)
s="Siri"
print(s)
s='''Siri'''
print(s)

fname='Saragadam'
lname='Sirisha'
#concatenation
print("Concatenation: ",fname+lname)
#repetition
print("Repetition: ",lname*10)
#indexing
print("Indexing: ",s[2])
print("Negative Indexing: ",s[-2])
#slicing [start:end+1:step]
names='SirishaSravaniLikkiHitha'
print("Slicing: ",names[0:7]," ",names[7:14]," ",names[14:19]," ",names[19:24])
print("Slicing: get odd positions- ",names[::2],"| get even positions- ",names[1::2])
print("Negative Slicing: ",names[-5:]," ",names[-10:-5]," ",names[-17:-10]," ",names[-24:-17])
print("Reverse of the string: ",names[::-1])
print("Reverse sub-string: ",names[-1:-6:-1]," ",names[-6:-11:-1]," ",names[-11:-18:-1]," ",names[-18:-25:-1])
#membership
print("Check if sub-string is inside the string: ",'Siri' in names," ",'siri' in names," ",'Likki' not in names)

#Built-in functions of String
#length of string
print("Length of the string: ",len(names))
#sort the string
print("Sort the string: ",sorted(names))
#max of string
print("Max of the string: ",max(names))
#min of string
print("Min of the string: ",min(names))
#order(ASCII value) of character
print("Order: ",ord(names[5]))
#char for ASCII value
print("Character: ",chr(1)," ",chr(98)," ",chr(49)," ",chr(64))

#String Methods
p='Python programming'
print("Uppercase: ",p.upper())
print("Lowercase: ",p.lower())
print("Capitalize: ",p.capitalize())
print("Titlecase: ",p.title())
print("Swapcase: ",p.swapcase())
print("Center the string: ",p.center(50,'-'))
print("ljust: ",p.ljust(50,'-'),"   ",p.ljust(50,"*"))
print("rjust: ",p.rjust(50,'-'),"   ",p.rjust(50,"*"))
print("zfill: ",p.zfill(50))
print("Find sub-string in string: ",p.find("programming")," ",p.find("Programming")," ",p.find('o'))
print("rfind: ",p.rfind('o'))
print("Index: ",p.index("programming")," ",p.index('o'))
print("rindex: ",p.rindex('o'))
print("Count: ",p.count('o')," ",p.count('g'))
#casefold