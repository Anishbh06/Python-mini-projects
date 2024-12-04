def add( n1, n2):
    ans = n1 + n2
    return ans

def sub( n1, n2):
    ans = n1 - n2
    return ans

def mul( n1, n2):
    ans = n1 * n2
    return ans

def div( n1, n2):
    ans = n1 / n2
    return ans

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/":div
}
def calculator():
    num1 = int(input("Enter the first number: "))
    for symbol in operations:
            print(symbol)

    should_continues = True

    while should_continues:
        operation_symbol = input("\nPick the operation to be performed: ")
        num2 = int(input("Enter the first number: "))
        function = operations[operation_symbol]
        first_ans = function(num1,num2)

        print(f" {num1} {operation_symbol} {num2} = {first_ans}")

        if input(f"Type y to continue calculating with {first_ans} or n to exit and a to start new calculation: ") == "y":
         num1 = first_ans
        else:
         should_continues = False
         calculator()


calculator()
        





