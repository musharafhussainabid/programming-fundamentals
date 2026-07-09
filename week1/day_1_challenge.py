"""Problem:
A bank wants to store basic information about a new customer account.
The customer's name is whatever your name is, they are 25 years old,
 their monthly salary is 85,000 PKR, they are currently employed,
 and they have not yet set a savings goal (unknown for now).

Your job:
Declare all five variables with correct type annotations
Print a formatted summary line:
"Account holder: Musharaf | Age: 25 | Salary: 85,000.00 PKR/month
| Employed: Yes | Savings goal: Not set"
Print the type of each variable using type()
Verify with isinstance() that salary is a float and age is an int — print the results
Show that bool is a subclass of int by printing is_employed + 1 and explaining the result in comment
Handle the savings goal: if it's None, print "Not set".
If it has a value (test by temporarily setting it to 50000.0), print the formatted amount

Rules:

Type annotations on every variable
Only f-strings
snake_case everywhere
No magic numbers — if you use 0 anywhere to represent something, give it a name"""

"""
This module demonstrates basic Python programming fundamentals including 
data types, type checking, and truthy/falsy evaluation.
"""


def main():
    """Execute the core programming fundamentals challenge script."""
    name: str = "Musharaf"
    age: int = 25
    monthly_salary: float = 85000.0
    is_employed: bool = True
    saving_goals: float | None = 50000.0

    if saving_goals is not None:
        print(f"The saving goals: {saving_goals:.1f}")

    print("====Summary of Customer====")
    print(
        f"Account holder: {name} | Age: {age} | "
        f"Salary: {monthly_salary:,.2f} PKR/month | "
        f"Employed: {'Yes' if is_employed else 'No'} | "
        f"Savings goal: {'Not Set' if saving_goals is None else 'Shown Above'}"
    )

    print(type(name))
    print(type(age))
    print(type(monthly_salary))
    print(type(is_employed))
    print(type(saving_goals))

    print(isinstance(monthly_salary, float))
    print(isinstance(age, int))

    print(
        "This sum operation shows that the bool type is a "
        f"subclass of int--> Result: {is_employed + 1}"
    )


if __name__ == "__main__":
    main()
