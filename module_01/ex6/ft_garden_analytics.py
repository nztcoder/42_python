class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, days: int, color: str,
                 is_blooming: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.is_blooming = is_blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, days: int, color: str,
                 is_blooming: str, prize_points: int) -> None:
        super().__init__(name, height, days, color, is_blooming)
        self.prize_points = prize_points


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, new_plant) -> None:
        self.plants.append(new_plant)
        print(f"Added {new_plant.name} to {self.owner}'s garden")

    def grow(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers ({plant.is_blooming}), "
                      f"Prize points: {plant.prize_points}")
                prize += 1
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers ({plant.is_blooming})")
                flowering += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                regular += 1
        print(f"\nPlants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers\n")


class GardenManager:
    class GardenStats:
        @staticmethod
        def calculate_score(garden) -> int:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points * 4
            return score

    def __init__(self) -> None:
        self.gardens = {}

    def add_garden(self, garden) -> None:
        self.gardens[garden.owner] = garden

    def show_scores(self) -> None:
        scores = []
        for owner, garden in self.gardens.items():
            score = (GardenManager.GardenStats.calculate_score(garden))
            scores.append(f"{owner}: {score}")
        print(f"Garden scores - {', '.join(scores)}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    @classmethod
    def create_garden_network(cls, owners: list):
        res = cls()
        for owner in owners:
            res.add_garden(owner)
        return res


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    plant1 = Plant("Oak Tree", 100, 365)
    plant2 = FloweringPlant("Rose", 25, 15, "red", "blooming")
    plant3 = PrizeFlower("Sunflower", 50, 45, "yellow", "blooming", 10)
    plant4 = Plant("Pine Tree", 50, 330)
    plant5 = FloweringPlant("Tulip", 6, 13, "white", "blooming")
    plant6 = PrizeFlower("Lotus", 5, 23, "pink", "blooming", 7)

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    alice_garden.add_plant(plant1)
    alice_garden.add_plant(plant2)
    alice_garden.add_plant(plant3)
    alice_garden.grow()
    print()
    bob_garden.add_plant(plant4)
    bob_garden.add_plant(plant5)
    bob_garden.add_plant(plant6)
    bob_garden.grow()
    alice_garden.report()
    bob_garden.report()

    # manager = GardenManager()
    # manager.add_garden(alice_garden)
    # manager.add_garden(bob_garden)
    owners = [alice_garden, bob_garden]
    manager = GardenManager.create_garden_network(owners)
    print(f"Height validation test: {GardenManager.validate_height(50)}")
    manager.show_scores()
    print(f"Total gardens managed: {len(manager.gardens)}")
