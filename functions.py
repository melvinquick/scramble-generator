# --- Libraries --- #

import random


# --- Functions --- #

def three_by_three(num_moves=20):
    # Function for generating random moves for standard cube puzzles (e.g. 2x2, 3x3, 4x4, etc.)
    # Possible moves are: Right (R), Right Inverted (R'), Left (L), Left Inverted (L'), Up (U),
    # Up Inverted (U'), Down (D), Down Inverted (D'), Front (F), Front Inverted (F'), Back (B), Back Inverted (B')

    top_moves = ["U ", "U' "]
    bottom_moves = ["D ", "D' "]
    left_moves = ["L ", "L' "]
    right_moves = ["R ", "R' "]
    front_moves = ["F ", "F' "]
    back_moves = ["B ", "B' "]
    scramble_order = []
    counter = 0

    while counter < num_moves:
        if counter == 0:
            scramble_order.append(random.choice(
                top_moves+bottom_moves+left_moves+right_moves+front_moves+back_moves))
        else:
            match scramble_order[-1]:
                case "U ":
                    scramble_order.append(random.choice(
                        ["U "]+left_moves+right_moves+front_moves+back_moves))
                case "U' ":
                    scramble_order.append(random.choice(
                        ["U' "]+left_moves+right_moves+front_moves+back_moves))
                case "D ":
                    scramble_order.append(random.choice(
                        ["D "]+left_moves+right_moves+front_moves+back_moves))
                case "D' ":
                    scramble_order.append(random.choice(
                        ["D' "]+left_moves+right_moves+front_moves+back_moves))
                case "L ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+["L "]+front_moves+back_moves))
                case "L' ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+["L' "]+front_moves+back_moves))
                case "R ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+["R "]+front_moves+back_moves))
                case "R' ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+["R' "]+front_moves+back_moves))
                case "F ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+left_moves+right_moves+["F "]))
                case "F' ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+left_moves+right_moves+["F' "]))
                case "B ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+left_moves+right_moves+["B "]))
                case "B' ":
                    scramble_order.append(random.choice(
                        top_moves+bottom_moves+left_moves+right_moves+["B' "]))
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
