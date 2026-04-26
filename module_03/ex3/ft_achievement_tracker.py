def main() -> None:
    """Run the achievement tracker system."""
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unigue_ach = alice.union(bob, charlie)
    print(f"All unique achievements: {unigue_ach}")
    print(f"Total unique achievements: {len(unigue_ach)}")

    common_ach = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common_ach}")

    shared_ach = alice.intersection(bob) | alice.intersection(
        charlie) | bob.intersection(charlie)
    rare_ach = unigue_ach.difference(shared_ach)
    print(f"Rare achievements (1 player): {rare_ach}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
