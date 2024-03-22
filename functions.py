# --- Libraries --- #

import random


# --- Functions --- #

# Function for generating random moves for standard 3x3 cube puzzles
# Possible moves are: Right and Right Inverted (R and R'), Left and Left Inverted (L and L'), Up and Up Inverted (U and U'), Down and Down Inverted (D and D'), Front and Front Inverted (F and F'), Back and Back Inverted (B and B')


def moves(num_moves=20):
    moves = [
        "U ",
        "U' ",
        "D ",
        "D' ",
        "L ",
        "L' ",
        "R ",
        "R' ",
        "F ",
        "F' ",
        "B ",
        "B' ",
    ]
    filtered_moves = []
    scramble_order = []
    counter = 0

    while counter < num_moves:
        if counter == 0:
            scramble_order.append(random.choice(moves))
        else:
            filtered_moves = [
                element for element in moves if element != scramble_order[-1]
            ]
            scramble_order.append(random.choice(filtered_moves))

        counter += 1

    scramble_order = "".join(map(str, scramble_order))

    return scramble_order


# --- Main --- #


def main():
    try:
        num_moves = int(
            input(
                "Enter the number of moves you'd like the scrambler to generate (leave blank for defaults): "
            )
        )
    except ValueError:
        num_moves = 20

    if num_moves == "":
        num_moves = 20

    print(moves(num_moves))


if __name__ == "__main__":
    main()
