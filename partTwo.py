import math  

def main():
    number1 = int(input("Enter the first integer: "))  
    number2 = int(input("Enter the second integer: "))
    result = pythag(number1 , number2)
    print (result)


def pythag(A,B):
    C = math.sqrt((A**2)+(B**2))
    return C

main()
