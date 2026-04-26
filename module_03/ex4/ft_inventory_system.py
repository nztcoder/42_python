import sys


def main() -> None:
    """
    Parses command-line arguments in the format 'name:quantity',
    constructs an inventory dictionary, calculates distribution statistics,
    categorizes items by scarcity levels, and provides restocking suggestions
    """
    print("=== Inventory System Analysis ===")
    inventory = {}
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        for item in args:
            name, count = item.split(":")
            qty = int(count)
            inventory.update({name: qty})
        total = sum(inventory.values())
        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {len(inventory)}")

        print("\n=== Current Inventory ===")
        sorted_items = sorted(
            inventory.items(), key=lambda x: x[1], reverse=True)
        for name, qty in sorted_items:
            unit = "unit" if qty == 1 else "units"
            percent = qty / total * 100
            print(f"{name}: {qty} {unit} ({percent:.1f}%)")

        print("\n=== Inventory Statistics ===")
        most = max(inventory, key=lambda x: inventory[x])
        least = min(inventory, key=lambda x: inventory[x])
        most_unit = "unit" if inventory[most] == 1 else "units"
        least_unit = "unit" if inventory[least] == 1 else "units"
        print(f"Most abundant: {most} ({inventory[most]} {most_unit})")
        print(f"Least abundant: {least} ({inventory[least]} {least_unit})")

        print("\n=== Item Categories ===")
        moderate = {}
        scarce = {}
        for name, qty in inventory.items():
            if qty > 3:
                moderate.update({name: qty})
            else:
                scarce.update({name: qty})
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        print("\n=== Management Suggestions ===")
        restock = []
        for name, qty in inventory.items():
            if qty == 1:
                restock.append(name)
        print(f"Restock needed: {', '.join(restock)}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {', '.join(inventory.keys())}")
        string_values = [str(val) for val in inventory.values()]
        print(f"Dictionary values: {', '.join(string_values)}")
        print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
    else:
        print("Error parsing arguments. "
              "Input example: sword:1 potion:5 shield:2 armor:3 helmet:1")


if __name__ == "__main__":
    main()
