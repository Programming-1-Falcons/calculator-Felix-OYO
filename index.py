while True:
    variable_one = input("whats the operator? ")
    variable_two = float(input("whats the first number? "))
    variable_three = float(input("whats the second number? "))

    hamster = ""
    if variable_one == "+":
        hamster = variable_two + variable_three
    elif variable_one == "-":
        hamster = variable_two - variable_three
    elif variable_one == "*":
        hamster = variable_two * variable_three
    elif variable_one == "/":
        hamster = variable_two / variable_three
    elif variable_one == "^":
        hamster = variable_two ** variable_three
    
    print(f"{variable_two} {variable_one} {variable_three} = {hamster}")
