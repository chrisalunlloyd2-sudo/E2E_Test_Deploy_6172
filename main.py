def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    n = int(input("Enter a positive integer to calculate the nth Fibonacci number: "))
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")