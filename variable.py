
# 4- Variable 

Name: str = "Masfa"
Age: int = 26
isgirl: bool = True
students: list = ["musab", "masfa", "hadia", "jannat"]

print (Name)
print(Age)
print(type(isgirl))  # how to find the type of variable
print(students)

#  i- CHeck the type of a variable
student_data: dict = {"stu1": "Masfa", "age1":24, "stu2": "Musab", "age2": 16}

print("student_data: ", (student_data))
print("student_data: ", type(student_data))

# ii- Casting
name: str = "python" 
age:int = 23
# type CASTING (want to concatenate name and age)
print(name + age) # Error

# solution
age: int  = str(23)
print(name + age)  # OUTPUT: python23

