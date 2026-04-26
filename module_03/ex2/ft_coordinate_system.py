import math
import sys


def parse_coord() -> None:
    """
    Parse a coordinate string from command-line arguments and display analytics
    """
    if len(sys.argv) == 2:
        args = sys.argv[1]
        try:
            print(f"Parsing coordinates: \"{args}\"")
            coord = args.split(',')
            int_coord = []
            for val in coord:
                int_coord.append(int(val))
            fin_coord = tuple(int_coord)
            print(f"Parsed position: {fin_coord}")
            start_point = (0, 0, 0)
            res = euclid_distance(start_point, fin_coord)
            print(f"Distance between {start_point} and {fin_coord}: {res:.2f}")

        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    else:
        print("Error parsing coordinates. Example: \"3,4,5\"")


def euclid_distance(p1: tuple, p2: tuple) -> float:
    """Calculate the Euclidean distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    p1 = (0, 0, 0)
    p2 = (10, 20, 5)
    Euclid_dist = euclid_distance(p1, p2)
    print(f"Position created: {p2}")
    print(f"Distance between {p1} and {p2}: {Euclid_dist:.2f}\n")
    parse_coord()
    print("\nUnpacking demonstration:")
    demo = (3, 4, 0)
    x, y, z = demo
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
