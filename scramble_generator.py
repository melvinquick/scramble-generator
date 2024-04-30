# --- Libraries --- #

import secrets

# --- Functions --- #

# Function for generating random moves for standard 3x3 cube puzzles
# Possible moves are: Right and Right Inverted (R and R'), Left and Left Inverted (L and L'), Up and Up Inverted (U and U'), Down and Down Inverted (D and D'), Front and Front Inverted (F and F'), Back and Back Inverted (B and B')


class ScrambleGenerator:
    def __init__(self, puzzle_type="3x3"):
        self.puzzle_type = puzzle_type
        self.opposite_moves = {
            "U ": "U' ",
            "U' ": "U ",
            "D ": "D' ",
            "D' ": "D ",
            "L ": "L' ",
            "L' ": "L ",
            "R ": "R' ",
            "R' ": "R ",
            "F ": "F' ",
            "F' ": "F ",
            "B ": "B' ",
            "B' ": "B ",
        }

    def generate_scramble(self, num_moves=25):
        moves = self.get_valid_moves()
        scramble_order = []
        counter = 0

        while counter < num_moves:
            if counter == 0:
                scramble_order.append(secrets.choice(moves))
            else:
                filtered_moves = [
                    move
                    for move in moves
                    if move != self.opposite_moves[scramble_order[-1]]
                ]
                scramble_order.append(secrets.choice(filtered_moves))

            counter += 1

        return "".join(map(str, scramble_order))

    def get_valid_moves(self):
        match self.puzzle_type:
            case "2x2":
                return ["U ", "U' ", "R ", "R' ", "F ", "F' "]
            case "3x3":
                return [
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


# --- Main --- #


def main():
    try:
        num_moves = int(
            input(
                "Enter the number of moves you'd like the scrambler to generate (leave blank for defaults): "
            )
        )
    except ValueError:
        num_moves = 25

    puzzle_type = str(
        input("Select one of the following list [2x2,3x3] (leave blank for defaults): ")
    )
    if puzzle_type == "":
        puzzle_type = "3x3"

    scrambler = ScrambleGenerator(puzzle_type.lower())

    print(scrambler.generate_scramble(num_moves))


if __name__ == "__main__":
    main()
