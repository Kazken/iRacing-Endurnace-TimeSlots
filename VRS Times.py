import argparse

def calculate_next_race_values(previous_z):
    y = previous_z + 36000
    z = y + 79200
    k = z + 489600
    return y, z, k

def generate_race_splits(races, initial_x):
    previous_z = initial_x
    for idx, race in enumerate(races, start=1):
        y_next, z_next, k_next = calculate_next_race_values(previous_z)

        # Calculate splits based on the requirements
        if idx == 1:
            split1 = initial_x
            split2 = split1 + 36000
            split3 = split2 + 79200
        else:
            # For subsequent races, ensure Split 1 is 489600 more than Split 3 of the previous race
            split3_prev = split3
            split1 = split3_prev + 489600
            split2 = split1 + 36000
            split3 = split2 + 79200

        print(f"\nRace at {race}")
        print(f"Split 1 is in <t:{split1}:R> on <t:{split1}:F>")
        print(f"Split 2 is in <t:{split2}:R> on <t:{split2}:F>")
        print(f"Split 3 is in <t:{split3}:R> on <t:{split3}:F>")

        # Update previous_z for the next iteration
        previous_z = z_next

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
