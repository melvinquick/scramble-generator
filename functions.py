# --- Libraries --- #

import random, time, os

# --- Functions --- #

# Function for generating random moves for standard 3x3 cube puzzles
# Possible moves are: Right and Right Inverted (R and R'), Left and Left Inverted (L and L'), Up and Up Inverted (U and U'), Down and Down Inverted (D and D'), Front and Front Inverted (F and F'), Back and Back Inverted (B and B')


class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False
        self.total_time = 0

    def start_timer(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True

    def stop_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False

    def reset_timer(self):
        self.elapsed_time = 0
        self.is_running = False
        self.total_time = 0

    def log_timer(self):
        if self.is_running:
            self.total_time = time.time() - self.start_time

        return round(self.total_time, 2)


def moves(num_moves=25, puzzle="3x3"):
    opposite_moves = {
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
    # print(opposite_moves)
    filtered_moves = []
    scramble_order = []
    counter = 0

    match puzzle:
        case "2x2":
            moves = [
                "U ",
                "U' ",
                "R ",
                "R' ",
                "F ",
                "F' ",
            ]
            while counter < num_moves:
                if counter == 0:
                    scramble_order.append(random.choice(moves))
                else:
                    filtered_moves = [
                        move
                        for move in moves
                        if move != opposite_moves[scramble_order[-1]]
                    ]
                    scramble_order.append(random.choice(filtered_moves))

                counter += 1
        case "3x3":
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
            while counter < num_moves:
                if counter == 0:
                    scramble_order.append(random.choice(moves))
                else:
                    filtered_moves = [
                        move
                        for move in moves
                        if move != opposite_moves[scramble_order[-1]]
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
        num_moves = 25

    try:
        puzzle = str(input("Select one of the following list [2x2,3x3]: "))
    except ValueError:
        puzzle = "3x3"

    if num_moves == "":
        num_moves = 25

    print(moves(num_moves))


def timer_main():
    timer = Timer()
    command = input(
        "Please enter one of the following commands... \nstart\nctrl-c to quit\n\n>"
    )

    if command == "start":
        timer.start_timer()
    else:
        print("Invalid command. Please try again.")

    while True:
        print(timer.log_timer())


if __name__ == "__main__":
    timer_main()
