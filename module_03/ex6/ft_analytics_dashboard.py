from typing import Any


def main() -> None:
    """
    Executes the Game Analytics Dashboard
    and demonstrates Python comprehension patterns.
    """
    print("=== Game Analytics Dashboard ===")

    players_data: dict[str, dict[str, Any]] = {
        'alice': {
            'level': 41,
            'total_score': 2824,
            'sessions_played': 13,
            'favorite_mode': 'ranked',
            'achievements': {
                'first_kill', 'treasure_hunter', 'speed_demon', 'perfectionist'
                },
            'achievements_count': 4,
            'region': 'north'
        },
        'bob': {
            'level': 16,
            'total_score': 4657,
            'sessions_played': 27,
            'favorite_mode': 'ranked',
            'achievements': {
                'boss_slayer', 'warrior'
                },
            'achievements_count': 2,
            'region': 'east'
        },
        'charlie': {
            'level': 44,
            'total_score': 9935,
            'sessions_played': 21,
            'favorite_mode': 'ranked',
            'achievements': {
                'magician', 'pathfinder', 'boss_slayer'
                },
            'achievements_count': 3,
            'region': 'central'
        },
        'diana': {
            'level': 3,
            'total_score': 1488,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements': {
                'first_kill', 'treasure_hunter', 'speed_demon'
                },
            'achievements_count': 3,
            'region': 'central'
        },
        'eve': {
            'level': 33,
            'total_score': 1434,
            'sessions_played': 81,
            'favorite_mode': 'casual',
            'achievements': {
                'first_kill', 'speed_demon', 'treasure_hunter',
                'boss_slayer', 'perfectionist'
                },
            'achievements_count': 5,
            'region': 'east'
        },
        'frank': {
            'level': 15,
            'total_score': 8359,
            'sessions_played': 85,
            'favorite_mode': 'competitive',
            'achievements': {
                'first_kill'
                },
            'achievements_count': 1,
            'region': 'north'
        }
    }

    print("\n=== List Comprehension Examples ===")
    high_scorers = [
        p for p in players_data if players_data[p]['total_score'] > 2000]
    scores_doubled = [players_data[p]['total_score'] * 2 for p in players_data]
    active = [
        p for p in players_data if players_data[p]['sessions_played'] > 25]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    players_scores = {
        p: score['total_score'] for p, score in players_data.items()
        }
    score_categories = {
        'high': len([
            s for s in players_data.values() if s['total_score'] >= 5000
            ]),
        'medium': len([
            s for s in players_data.values() if s['total_score'] >= 4000
            and s['total_score'] < 5000
            ]),
        'low': len([
            s for s in players_data.values() if s['total_score'] < 4000
            ])
    }
    achievements_count = {
        p: ach['achievements_count'] for p, ach in players_data.items()
        }
    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievements_count}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p for p in players_data.keys()}
    unique_achievements = {
        a for p in players_data for a in players_data[p]['achievements']
        }
    active_regions = {p['region'] for p in players_data.values()}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players_data.keys())}")
    print(f"Total unigue achievements: {len(unique_achievements)}")
    average_score = (
        sum(p['total_score'] for p in players_data.values())
        / len(unique_players)
    )
    print(f"Average score: {average_score:.1f}")
    top = max(players_data, key=lambda p: players_data[p]['total_score'])
    print(f"Top performer: {top} ({players_data[top]['total_score']} points,"
          f"{players_data[top]['achievements_count']} achievements)")


if __name__ == "__main__":
    main()
