# Write a function that accepts any number of integers as positional arguments and any number of a student's
#attributes as keyword arguments and prints the result of multiplying all of the integers with a customized
#greeting based on the keyword arguments. Name the function multiply_and_greet.

def multiply_and_greet(*args,**kwargs):
    a = 1
    keys=kwargs.keys()

    for number in args:
        a *= number
    print(a)
    if "country" in keys:
        print(f"Hello {kwargs['name']} from {kwargs['country']}.")
    elif "sex" in keys:
        print(f"Hello {kwargs['name']} you are {kwargs['sex']}.")
    elif "age" in keys:
        year = 2022 - kwargs["age"]
        print(f"Hello {kwargs['name']} you were born in {year}.")
    elif "name" in keys:
        print(f"Hello {kwargs['name']}.")
    else:
        print(f"Hello human being")