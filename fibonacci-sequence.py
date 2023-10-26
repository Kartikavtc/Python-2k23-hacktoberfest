def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Get the number of terms from the user
terms = int(input("Enter the number of Fibonacci terms to generate: "))

if terms <= 0:
    print("Please enter a positive number of terms.")
else:
    fibonacci_sequence = generate_fibonacci(terms)
    print("Fibonacci Sequence:")
    for number in fibonacci_sequence:
        print(number)
