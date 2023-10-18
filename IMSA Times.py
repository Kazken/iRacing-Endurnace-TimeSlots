import argparse

def calculate_next_race_values(previous_m):
    k = previous_m - 1080000
    z = k - 72000
    y = z - 39600
    return y, z, k

def generate_race_splits(races, initial_x):
    previous_m = initial_x
    for idx, race in enumerate(races, start=1):
        y_next, z_next, k_next = calculate_next_race_values(previous_m)

        # Calculate splits based on the requirements
        if idx == 1:
            split1 = initial_x
            split2 = split1 + 18000
            split3 = split2 + 39600
            split4 = split3 + 72000
        else:
            split4_prev = split4
            split1 = split4_prev + 1080000
            split2 = split1 + 18000
            split3 = split2 + 39600
            split4 = split3 + 72000

        print(f"\nRace at {race}")
        print(f"Split 1 is in <t:{split1}:R> on <t:{split1}:F>")
        print(f"Split 2 is in <t:{split2}:R> on <t:{split2}:F>")
        print(f"Split 3 is in <t:{split3}:R> on <t:{split3}:F>")
        print(f"Split 4 is in <t:{split4}:R> on <t:{split4}:F>")

        # Update previous_m for the next iteration
        previous_m = k_next

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate race splits based on input variables.")
    parser.add_argument("initial_x", type=int, help="Initial value for x")
    parser.add_argument("races", nargs="+", help="List of races")

    args = parser.parse_args()

    initial_x = args.initial_x
    races = args.races

    print("Results:")

    # Generate race splits for the specified races
    generate_race_splits(races, initial_x)
