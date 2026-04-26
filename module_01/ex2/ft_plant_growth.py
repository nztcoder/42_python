class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self, cm: int) -> None:
        self.height += cm

    def age(self, duration: int) -> None:
        self.days += duration

    def get_info(self, day_num: int) -> None:
        print(f"=== Day {day_num} ===")
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    curr_day = 1
    first_day_height = plant1.height
    plant1.get_info(curr_day)
    for curr_day in range(2, 8):
        plant1.grow(1)
        plant1.age(1)
    plant1.get_info(curr_day)
    print(f"Growth this week: +{plant1.height - first_day_height}cm")
