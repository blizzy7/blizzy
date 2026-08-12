def fix_greeting(name):
    # Bug to fix: the function should use name, not an undefined variable.
    name = input("Enter your name: ")
    greeting = f"Hello, {name}."
    return greeting
# Implement fix_greeting(name).
#  Return a greeting in this exact format: Hello, Ada. 
#  Replace Ada with the provided name. 
#  The starter idea contains a common variable-name mistake. 
#  Fix the function so it uses the argument correctly.