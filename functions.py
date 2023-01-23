# --- Libraries --- #

import random


# --- Functions --- #

def three_by_three(num_moves=20):
    # Function for generating random moves for standard cube puzzles (e.g. 2x2, 3x3, 4x4, etc.)
    # Possible moves are: Right (R), Right Inverted (R'), Left (L), Left Inverted (L'), Up (U),
    # Up Inverted (U'), Down (D), Down Inverted (D'), Front (F), Front Inverted (F'), Back (B), Back Inverted (B')

    possible_moves = ["R ", "R' ", "L ", "L' ", "U ",
                      "U' ", "D ", "D' ", "F ", "F' ", "B ", "B' "]
    scramble_order = []
    counter = 0
    while counter < num_moves:
        scramble_order.append(random.choice(possible_moves))
        counter += 1
    scramble_order = "".join(scramble_order)
    return scramble_order


# --- Main --- #

def main():

    # Variables
    try:
        num_moves = int(input(
            "Enter the number of moves you'd like the scrambler to generate (default is 20): "))
    except ValueError:
        num_moves = 20

    if num_moves == "":
        num_moves = 20

    print(three_by_three(num_moves))


if __name__ == "__main__":
    main()
