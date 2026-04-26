def check_temperature(temp_str: str) -> int | None:
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature {temp} is perfect for plants!")
        return temp
    return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    tests = ["25", "abc", "100", "-50"]
    for val in tests:
        check_temperature(val)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
