def main():
    slow = input("Input: ")
    result = myFunction(slow)
    print (result)

def myFunction(text):
    text = text.replace(" ", "...")
    return text

main()
