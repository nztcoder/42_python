class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """calculating shade area"""
        shade_area = 3.14 * (self.trunk_diameter ** 2) / 4
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    tulip = Flower("Tulip", 30, 17, "yellow")
    tulip.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    maple = Tree("Maple", 300, 600, 40)
    maple.produce_shade()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    carrot = Vegetable("Carrot", 10, 30, "autumn", "A")
