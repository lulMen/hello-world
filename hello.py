def main():
    # Start the program by getting the user's name and greeting them
    name = getName()
    sayHello(name)

def getName():
    # Get the user's name via input
    return input("What's your name? ")

def sayHello(name):
    # Output a personalized greeting to the console
    print(f"Hello {name}! How's the weather?")

# Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()