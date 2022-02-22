from CalcArt import logo
from CalcModerator import clearConsole

# Write Code 💻
print(logo)

def additon(n1, n2):
    return n1 + n2

def subtraction(n1,n2):
    return n1 - n2

def multiplication(n1,n2):
    return n1 * n2

def normal_Division(n1,n2):
    return n1 / n2

def integar_Division(n1,n2):
    return n1 // n2

def modulus(n1,n2):
    return n1 % n2

def pow(n1,n2):
    return n1 ** n2


mathmatical_Symbol = [" + ", " - ", " * ", " / ", " // ", " % ", " ^ "]

def Calc():
    """Calculate The Result Between Two Numbers, Print Out The Solution And Return The Result"""
    end_Calculation = False
    first_Value = float(input("\n\nKaede : Please Enter The First Value -> "))

    for symbol in mathmatical_Symbol:
            print(f"\n{symbol}")
        
    while not end_Calculation:
        operator = input("\n\nKaede: Choose The Operator You'd Like To Use -> ")
        last_Value = float(input("\n\nKaede : Please Enter The Next Value -> "))

        if operator == "+":
            result = additon(first_Value, last_Value)
        
        elif operator == "-":
            result = subtraction(first_Value, last_Value)
        
        elif operator == "*":
            result = multiplication(first_Value, last_Value)
        
        elif operator == "/":
            result = normal_Division(first_Value, last_Value)
        
        elif operator == "//":
            result = integar_Division(first_Value, last_Value)
        
        elif operator == "%":
            result = modulus(first_Value, last_Value)
        
        elif operator == "^":
            result = pow(first_Value, last_Value)
            
        print(f"\n\nKaede : {first_Value} {operator} {last_Value} = {result}")

        continue_Program = input(f"\n\nKaede : Would You Like To Contiue Calculating With {result}? Y/N -> ").lower()

        if continue_Program == "y":
            first_Value = result
            clearConsole()

        else:
            end_Calculation = True
            Calc()
            
isFinish = False
Calc()
