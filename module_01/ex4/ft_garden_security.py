class SecurePlant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        print(f"Plant created: {self.name}")

        """private - encapsulation"""
        self.__height = 0
        self.__days = 0

        """use setting methods"""
        self.set_height(height)
        self.set_age(days)

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print("Invalid operation attempted: "
                  f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Invalid operation attempted: "
                  f"age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__days = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__days

    def get_info(self) -> None:
        print(f"Current plant: "
              f"{self.name} ({self.get_height()}cm, {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 25, 30)
    print()
    plant1.set_height(-5)
    # plant1.set_age(-5)
    print()
    plant1.get_info()
