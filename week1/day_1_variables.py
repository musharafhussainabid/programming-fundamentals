"""
A. Python is dynamically typed but strongly typed.

-> Dynamically typed = Python figures out the type at runtime. You don't declare it.
-> Strongly typed = Python won't silently convert types. "5" + 5 crashes. It doesn't guess.




B. There are five premitive types of variables in python:
1. int: it is used to storage integers like 3,22,9,-6 etc
2. float: it is used to storage decimal values like 4.1,2.3,5.592 etc
3. bool: it is used to store boolean values like true:1 or false:0
4. str: it is used to store list of characters like "ALI"
5. NoneType: it store None when now information is given


C.PEP 8 naming:
variables and functions  →  snake_case
constants                →  UPPER_SNAKE_CASE  
classes                  →  PascalCase

D. Truthiness — Python considers these falsy, everything else is truthy:
0, 0.0, "", [], {}, set(), None, False
"""

#premitive types with annotations:

name : str = "Musharaf"
age: int = 26
is_employed: bool = True
middle_name: str | None = None

#constants

GENDER: str = "Male"
FATHER_NAME: str = "XYZ"
YEAR_OF_GRADUATION: str = "2025"



#Let's print the above values using type() and isinstance()

print(type(name))
print(type(YEAR_OF_GRADUATION))
print(isinstance(age,(float)))
print(isinstance(name,(str,int)))

#boolean
print(True + (True*True))
print(True*10 + True)
print(True * False)

#None Checking

company: str | None = None
if company == None:
    print("No company details provided")
else:
    print(company)

#Truthiness in action

falsy_examples = [0,0.0,"", {},[], None, False]

for item in falsy_examples:
    if not item:
        print(f"{repr(item)} is falsy")

#f-strings

monthly_income: float = 14000000458
print(f"Name: {name}")
print(f"Monthly Income: {monthly_income:,.2f} PKR")
print(f"Is None? {middle_name is None}")

# upp = middle_name.upper()
# print(upp) AttributeError: 'NoneType' object has no attribute 'upper'
