class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant: dict) -> None:
    if plant["water"] < 1:
        raise PlantError(f"The {plant['name']} plant is wilting!")


def check_water(amount: int) -> None:
    if amount < 5:
        raise WaterError("Not enough water in the tank!")


def test_custom_error() -> None:
    plant = {"name": "tomato", "water": 0}
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water(4)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant(plant)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water(3)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_error()
