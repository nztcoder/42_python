def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid input!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    good_plants = ["tomato", "lettuce", "carrots"]
    bad_plants = ["tomato", None, "carrots"]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(good_plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
