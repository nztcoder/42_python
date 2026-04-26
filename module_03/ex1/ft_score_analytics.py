import sys


def main() -> None:
    """Analyze player scores provided via command-line arguments"""
    print("=== Player Score Analytics ===")
    arguments = sys.argv[1:]
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = []
        try:
            for val in arguments:
                score = int(val)
                scores.append(score)

            total_players = len(scores)
            total_score = sum(scores)
            avg_score = total_score / total_players
            high_score = max(scores)
            low_score = min(scores)
            score_range = high_score - low_score

            print(f"Scores processed: {scores}")
            print(f"Total players: {total_players}")
            print(f"Total score: {total_score}")
            print(f"Average score: {avg_score:.1f}")
            print(f"High score: {high_score}")
            print(f"Low score: {low_score}")
            print(f"Score range: {score_range}")
        except ValueError:
            print("Error: All scores must be integers!")


if __name__ == "__main__":
    main()
