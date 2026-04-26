def garden_operations(operation: str) -> None:
    if operation == "value":
        int("abc")
    elif operation == "zero":
        10 / 0
    elif operation == "file":
        open("missing.txt")
    elif operation == "key":
        plants = {"rose": 1}
        plants["missing_plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")
        print()

    try:
        print("Testing KeyError...")
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        garden_operations("zero")
        garden_operations("file")
    except (ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
