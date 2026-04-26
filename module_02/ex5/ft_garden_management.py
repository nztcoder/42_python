class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(
            self, name: str, water_level: int, sunlight_hours: int
            ) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, new_plant: Plant) -> None:
        if new_plant.name == "":
            raise PlantError("Plant name cannot be empty!")
        else:
            self.plants.append(new_plant)
            print(f"Added {new_plant.name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
                plant.water_level += 1
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        if plant.water_level > 10:
            raise WaterError(f"Water level {plant.water_level} "
                             "is too high (max 10)")
        elif plant.sunlight_hours > 12:
            raise GardenError(f"Sunlight hours {plant.sunlight_hours} "
                              "is too high (max 12)")
        else:
            print(f"{plant.name}: healthy (water: {plant.water_level}, "
                  f"sun: {plant.sunlight_hours})")


def test_garden_management() -> None:
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 5, 15)
    bad_plant = Plant("", 5, 5)
    plants = [tomato, lettuce, bad_plant]
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    for plant in plants:
        try:
            manager.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    for plant in manager.plants:
        try:
            manager.check_plant_health(plant)
        except (WaterError, GardenError) as e:
            print(f"Error checking {plant.name}: {e}")

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
