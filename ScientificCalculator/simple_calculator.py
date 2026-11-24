def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+,-,*,/,**): ")
    num2 = float(input("Enter secound number: "))
    
    match operator:
        case "+":
            result = num1 + num2
            
        case "-":
            result = num1 - num2
            
        case "*":
            result = num1 * num2
            
        case "/":
            result = num1 / num2
            
        case "**":
            result = num1 ** num2
            
        case _:
            print("Invalid operator!")
            return
        
    print(f"Result: {result}")
    
calculator()