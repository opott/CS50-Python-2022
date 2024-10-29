# ask the user for their greeting
greeting = input("Greeting: ")

# convert the greeting to lowercase
greeting = greeting.lower()

# determine what the greeting is and print amount of money
if 'hello' in greeting:
    print("$0")
elif greeting.startswith('h'):
    print("$20")
else:
    print("$100")