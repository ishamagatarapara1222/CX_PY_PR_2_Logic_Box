print("======================================================================")
print("PR_2 : Logic Box")
print("Pattern Generator and Number Analyzer")
print("======================================================================")

print("Welcome to the pattern Generator and Number Analyzer!")

while True:
    print("\n---------------------------------------------")
    print("Select an option from the menu below:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except (ValueError, EOFError):
        print("\nInput ended. Exiting the program.")
        break

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Please enter a positive integer for the number of rows.")
            continue

        print("Right-angled Triangle Pattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == 2:
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Please enter a positive integer for the number of rows.")
            continue

        print("Pyramid Pattern:")
        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")
            print("* " * (2 * i - 1))

    elif choice == 3:
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Please enter a positive integer for the number of rows.")
            continue

        print("Left-angled Triangle Pattern:")
        for i in range(1, rows + 1):
            print("* " * i)

    elif choice == 4:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        if start > end:
            start, end = end, start

        total = 0
        count = 0
        even = 0
        odd = 0

        for num in range(start, end + 1):
            total += num
            count += 1
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        print(f"\nRange: {start} to {end}")
        print(f"Total numbers: {count}")
        print(f"Sum: {total}")
        print(f"Average: {total / count if count else 0}")
        print(f"Even numbers: {even}")
        print(f"Odd numbers: {odd}")

    else:
        print("Invalid choice. Please select a number from 1 to 4.")