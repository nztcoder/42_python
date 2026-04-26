class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")


if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Oak", 200, 365)
    plant_3 = Plant("Cactus", 5, 90)
    plant_4 = Plant("Sunflower", 80, 45)
    plant_5 = Plant("Fern", 15, 120)

    plants_list = [plant_1, plant_2, plant_3, plant_4, plant_5]

    print("=== Plant Factory Output ===")
    total = 0
    for plant in plants_list:
        total += 1
        plant.get_info()
    print()
    print(f"Total plants created: {total}")
