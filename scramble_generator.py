import secrets


class ScrambleGenerator:
    def __init__(self, puzzle_type="3x3"):
        self.puzzle_type = puzzle_type
        self.opposite_moves = {
            "U ": "U' ",
            "U' ": "U ",
            "U2 ": "U2' ",
            "U2' ": "U2 ",
            "D ": "D' ",
            "D' ": "D ",
            "D2 ": "D2' ",
            "D2' ": "D2 ",
            "L ": "L' ",
            "L' ": "L ",
            "L2 ": "L2' ",
            "L2' ": "L2 ",
            "R ": "R' ",
            "R' ": "R ",
            "R2 ": "R2' ",
            "R2' ": "R2 ",
            "F ": "F' ",
            "F' ": "F ",
            "F2 ": "F2' ",
            "F2' ": "F2 ",
            "B ": "B' ",
            "B' ": "B ",
            "B2 ": "B2' ",
            "B2' ": "B2 ",
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
            case "4x4":
                return [
                    "U ",
                    "U' ",
                    "U2 ",
                    "U2' ",
                    "D ",
                    "D' ",
                    "D2 ",
                    "D2' ",
                    "L ",
                    "L' ",
                    "L2 ",
                    "L2' ",
                    "R ",
                    "R' ",
                    "R2 ",
                    "R2' ",
                    "F ",
                    "F' ",
                    "F2 ",
                    "F2' ",
                    "B ",
                    "B' ",
                    "B2 ",
                    "B2' ",
                ]
            case "5x5":
                return [
                    "U ",
                    "U' ",
                    "U2 ",
                    "U2' ",
                    "D ",
                    "D' ",
                    "D2 ",
                    "D2' ",
                    "L ",
                    "L' ",
                    "L2 ",
                    "L2' ",
                    "R ",
                    "R' ",
                    "R2 ",
                    "R2' ",
                    "F ",
                    "F' ",
                    "F2 ",
                    "F2' ",
                    "B ",
                    "B' ",
                    "B2 ",
                    "B2' ",
                ]


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
        input(
            "Select one of the following list [2x2,3x3,4x4] (leave blank for defaults): "
        )
    )
    if puzzle_type == "":
        puzzle_type = "3x3"

    scrambler = ScrambleGenerator(puzzle_type.lower())

    print(scrambler.generate_scramble(num_moves))


if __name__ == "__main__":
    main()
