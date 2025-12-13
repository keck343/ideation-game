"""this writes to text files that touch designer reads in

All files are assumed to be in images directory
"""


def change_level_graphic(num):
    with open("level.txt", "w") as f:
        f.write(f"images/level_{num}.png")


def change_back_graphic(num):
    with open("back.txt", "w") as f:
        f.write(f"images/back_{num}.png")


def change_end_graphic(num):
    with open("end.txt", "w") as f:
        f.write(f"images/end_{num}.png")
