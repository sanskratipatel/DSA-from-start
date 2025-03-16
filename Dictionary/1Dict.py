types_dict = { 
    "id": 1, 
    "name": "python",
    "type": "interpreted",
    "use": "web development",
    "year": 1991,
    "framework": "Django"
} 

print(types_dict)
print(types_dict["name"]) 
print(types_dict.get("name")) 
for key ,value in types_dict.items():#id name type use year framework
    print(key, value) 

print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i in types_dict:  #id name type use year framework
    print(i, types_dict[i]) 

print(types_dict.items() )  #dict_items([('id', 1), ('name', 'python'), ('type', 'interpreted'), ('use', 'web development'), ('year', 1991), ('framework', 'Django')])
print(types_dict.keys())  #['apple', 'banana', 'cherry', 'dates', 'grapes', 'kiwi']  

types_dict["new"] = "Vallue"
print(types_dict)  #{'id': 1, 'name': 'python', 'type': 'interpreted', 'use': 'web development', 'year': 1991, 'framework': 'Django', 'new': 'Value'} 
types_dict.pop("new")
print(types_dict)  #{'id': 1, 'name': 'python', 'type': 'interpreted', 'use': 'web development', 'year': 1991, 'framework': 'Django'}
types_dict.popitem()    #('framework', 'Django')
print(types_dict)  #{'id': 1, 'name': 'python', 'type': 'interpreted', 'use': 'web development', 'year': 1991}          
# types_dict.clear() 