def main():
    user_expression = input("Expression: ")
    get_expression(user_expression)
    
def get_expression(user_expression):
    x, y, z = user_expression.split(" ")
    x = float(x)
    z = float(z)
    
    match y:
        case "+":
            solution = x + z
        case "-":
            solution = x - z
        case "/":
            solution = x/z
        case "x" | "*" | "X":
            solution = x * z
    
    print(solution)
    
main()