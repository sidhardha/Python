def greet(name):
    """Function to greet a person with their name."""
    return f"Hello, {name}!"

def main():
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        greeting = greet(name)
        print(greeting)

if __name__ == "__main__":
    main()