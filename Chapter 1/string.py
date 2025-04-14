# 2- String
# # What is a String in Python?
# A string is just text. Anything inside quotes (' ' or " ") is a string.
# (i) Concatination: "hello" + "world" -> "helloworld"
# (ii) length of string: len(str), e.g., len(hello) + len(world)

name = "Aisha"
greeting = 'Hello'
number_as_text = "123"

# i- Concatination

print("masfa " + "musab")

# print("python" + 123)   # ERROR: typeerror 

### Example ###
str1 = "Hello"
str2 = "World"

concatenated_str = str1 + " " + str2
print("concatenated_str:", concatenated_str)

# ii- length
length_of_str1 = len(str1)

print('length_of_str1:', length_of_str1)

#Escape sequences in strings python
# "\n" is a sign of new/  next line
# "\t" is a sign of tab space

str3 = "This is string string\nwe are creating it in python"
str4 = "This is string string\twe are creating it in python"

print(str3)
print(str4)


# 3- f-string

number_as_text = "123"

print (f"my roll num: {number_as_text} and my name is {name}")