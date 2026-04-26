class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.days} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.days} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.days} days old")
