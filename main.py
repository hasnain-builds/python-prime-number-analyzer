def is_prime(n):
    """
    Returns True if n is a prime number, otherwise False
    """
    # Step 1: Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Step 2: Check divisibility from 2 to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, not prime

    # Step 3: No divisors found
    return True


def check_single_number():
    try:
        num = int(input("Enter a number to check prime: "))
    except ValueError:
        print("❌ Please enter a valid integer.")
        return

    if is_prime(num):
        print(f"🎉 {num} is a PRIME number.")
    else:
        print(f"❌ {num} is NOT a prime number.")


def check_range():
    try:
        limit = int(input("Find prime numbers up to: "))
    except ValueError:
        print("❌ Please enter a valid integer.")
        return

    if limit < 2:
        print("⚠️ No prime numbers in this range.")
        return

    print(f"✅ Prime numbers up to {limit}:")
    for number in range(2, limit + 1):
        if is_prime(number):
            print(number, end=" ")
    print()  # new line


def main():
    print("🔢 Prime Number Analyzer")
    print("1. Check a single number")
    print("2. Find prime numbers in a range")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        check_single_number()
    elif choice == "2":
        check_range()
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
