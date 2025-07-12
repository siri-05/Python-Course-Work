#Ordered, Key-Value pairs, Mutable, dynamically sized and doesn't allows duplicate keys
d={}
d=dict()
d={'Name':'Sirisha','Course':'DS','Batch':15,3.5:'float',2+4j:3+5j,('a',3,4.6):[1,2,3.5],'Random':3.5}
print("Dictionary: ",d)
print("Access element using keys: ",d['Name'],"    ",d[3.5])
print("Access element if we don't know if element is present:",d.get('DOB'),"   ",d.get("Name"),"   ",d.get('DOB',"DOB doesn't exist"),"    ",d.get('Random',"Random doesn't exist"))
print("Get all the keys: ",d.keys())
print("Get all the values: ",d.values())
print("Get all the key-value pairs in tuples: ",d.items())
d['DOB']='21-05-1998'
d['Skills']={'Java':9,'Python':7}
print("Modifying the dictionary: ",d)
d.setdefault('Batch',3+7j)
d.setdefault('random',7.9)
print("Modify the dictionary with default value: ",d)
d['Batch']=14
print("Update the value of one key: ",d)
d.update({'Batch':15,'Key2':34})
print("Update multiple keys and modify the dictionary: ",d)
print("Length of dictionary: ",len(d))
print("Remove the last element: ",d.popitem())
print("Remove specific index element: ",d.pop('Course'))
del d[3.5]
print("Deleting the specific index and it's memory allocation: ",d)
d.clear()
print("Remove all elements from dictionary: ",d)
d={2:'a',1:'Siri',3:5+2j}
print("Sort the keys in the dictionary: ",sorted(d),"   ",d)
print("Maximum key in the dictionary: ",max(d))
print("Minimum key in the dictionary: ",min(d))