name = "MASALA DOSA" 
print(name.lower()) # masala dosa
print(name.upper()) # MASALA DOSA 
print(name.title()) # Masala Dosa
print(name.capitalize()) # Masala dosa 
print(name.swapcase()) # masala dosa
print(name.islower()) # False
print(name.isupper()) # False
print(name.istitle()) # False
print(name.isalpha()) # False
print(name.isdigit()) # False
print(name.isalnum()) # False
print(name.isspace()) # False
print(name.startswith("MAS")) # True
print(name.endswith("OSA")) # True
print(name.find("S")) # 3
print(name.rfind("S")) # 6
print(name.index("S")) # 3
print(name.rindex("S")) # 6   


str2 = "  Hello World  "
print(str2.strip()) # Hello World -> We remove the space from the start and end of the string
print(str2.lstrip()) # Hello World -> We remove the space from the start of the string 
print(str2.rstrip()) # Hello World -> We remove the space from the end of the string  


str3 = "Hello, World, This, is, me" 
print(str3.replace("Hello", "Hi")) # Hi World This is me  it will replace Hello to Hi 
print(str3.split(", ")) # ['Hello', 'World', 'This', 'is', 'me'] -> It will split the string by space 
# String convert to list  
print(str3.find("is")) # 15 -> It will return the index of the first occurrence of the string  

#  Convert List to String 
list1 = ["Hello", "World", "This", "is", "me"] 
print(" " .join(list1))  

# Length Of String  
str4 = "Hello World"
print(len(str4))  

like = "I like Python ,\"like Java and like C++\" " 
print(like)