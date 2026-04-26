from typing import Generator
import time


def event_generator(n: int) -> Generator[dict, None, None]:
    """
    Generates a sequence of simulated game event dictionaries.
    """
    players = ['alice', 'bob', 'charlie', 'david', 'eve', 'frank']
    actions = ['killed monster', 'found treasure', 'leveled up',
               'died', 'resting at a camp']
    for i in range(1, n + 1):
        player = players[i % len(players)]
        level = (i % 20) + 1
        action = actions[i % len(actions)]
        yield {
            'number': i,
            'player': player,
            'level': level,
            'action': action
        }


def fibonacci() -> Generator[int, None, None]:
    """Yields an infinite sequence of Fibonacci numbers."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Checks if a given integer is a prime number."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_generator() -> Generator[int, None, None]:
    """Yields an infinite sequence of prime numbers starting from 2."""
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def main() -> None:
    """Executes a demonstration of event processing and numeric generators"""
    print("=== Game Data Stream Processor ===\n")

    num_of_events = 1000
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    print(f"Processing {num_of_events} game events...\n")

    start_time = time.time()
    event_gen = event_generator(num_of_events)
    for _ in range(num_of_events):
        event = next(event_gen)
        total += 1
        if total <= 3:
            print(f"Event {event['number']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        if total == 3:
            print("...")
        if event['level'] >= 10:
            high_level += 1
        if event['action'] == 'found treasure':
            treasure += 1
        if event['action'] == 'leveled up':
            level_up += 1
    end_time = time.time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    generate = fibonacci()
    res = []
    for _ in range(10):
        res.append(next(generate))
    print(f"Fibonacci sequence (first 10): {', '.join(str(s) for s in res)}")

    prime = prime_generator()
    prime_res = []
    for _ in range(5):
        prime_res.append(next(prime))
    print(f"Prime numbers (first 5): {', '.join(str(s) for s in prime_res)}")


if __name__ == "__main__":
    main()
