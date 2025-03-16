fruit = ['apple', 'banana', 'cherry', 'dates', 'grapes']  
fruit.append('kiwi')   #['apple', 'banana', 'cherry', 'dates', 'grapes', 'kiwi']
print(fruit)
fruit.pop(3)  #['apple', 'banana', 'cherry', 'grapes', 'kiwi'] 
print(fruit) 

fruit.append('dates') #['apple', 'banana', 'cherry', 'grapes', 'kiwi', 'dates'] 
print(fruit)
fruit.insert(2, 'es') #['apple', 'banana', 'dates', 'cherry', 'grapes', 'kiwi', 'ds'] 
print(fruit) 
print(fruit.count('dates')) # 1
print(fruit.index('dates')) # 2 
fruit.remove('dates') #['apple', 'banana', 'cherry', 'grapes', 'kiwi', 'dates']
print(fruit)