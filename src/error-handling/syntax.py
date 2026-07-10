def variables_syntax():
    # Invalid Variable Names
    1st_user = "Alice"     # [INVALID] - Variable names cannot start with numbers
    user-name  = "Bob"     # [INVALID] - Hyphens are not allowed (interpreted as subtraction)
    $money = 187498179     # [INVALID] - Special characters like $ are not allowed
    first name = "Mock"    # [INVALID] - Spaces are not allowed

    # Using Reserved Keywords
    class = "BSCS"         # [INVALID] - 'class' is a reserved keyword
    def = -5               # [INVALID] - 'def' is a reserved keyword

    # C/C++ Style Static Typing
    str first_name         # [INVALID] - Statement has no assignment or valid expression
    int age = 25,          # [INVALID] - 'int' is not a keyword for declaration; trailing comma
    float salary = 4500000.00 # [INVALID] - Invalid type declaration syntax
    str last_name = "John" # [INVALID] - Invalid type declaration syntax

    # Standard Dynamic Initialization
    first_name = "Vikey"   # [CORRECT]
    print(first_name)      # [CORRECT]
    print(first_nam)       # [INVALID] - Runtime NameError (variable not defined)
    age = 25               # [CORRECT]
    salary = 4500000.00    # [CORRECT]

    # Type Annotations
    last_name: str = "Raj"         # [CORRECT]
    gender: str = "Male"           # [CORRECT]
    is_graduated: bool = True      # [CORRECT]
    is_married: bool = False       # [CORRECT]
def function_syntax():
   # Missing Colon and Bracket Syntax Examples
    """
    def wrong_func(){
        print("This is wrong syntax")
    }
    """                    # [INVALID] - Python does not use curly braces for code blocks
    
    """
    def unindented()
        print("Missing colon after the function definition")
    def sum(a,b) return a+b
    """                    # [INVALID] - Both functions miss colons; 'sum' line has invalid inline return

    # Correct Function Definition
    def correct_function():
        print("This is the correct syntax of defining functions.") # [CORRECT]

    # Invalid Parameter Ordering
    def greet(message = "Hello", name):
        pass               # [INVALID] - Non-default argument follows default argument

    # Correct Parameter Ordering
    def greet(name, message = "Hello"):
        pass               # [CORRECT]
    
    # Misspelled Keyword
    deff calculate(w,h):   # [INVALID] - 'deff' is not a valid keyword
        return w*h
        
    # Misplaced Return (Indentation Error)
    def calculate(w,h):
    return w*h             # [INVALID] - IndentationError; return statement must be indented inside the block
