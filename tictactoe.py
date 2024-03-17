from numpy import array
from os import system

grid = array([array([" " for _ in range(3)]) for _ in range(3)])


def board():
    system("cls")
    for i in grid:
        print(*i)


draw_prob = lambda: len([i for i in grid.flatten() if i in "XO"])==9


def condition(a):
    equalize = lambda *a: a[0] == a[1] == a[2] != " "
    for i in range(3):
        b = a[i, ...]
        if equalize(*b):
            return b[0]
    for i in range(3):
        b = a[..., i]
        if equalize(*b):
            return b[0]
    b = a.diagonal()
    if equalize(*b):
        return b[0]
    b = a[::-1].diagonal()
    if equalize(*b):
        return b[0]


def calc_occupied(a):
    o = list(a)
    return grid[ord(o[0]) - 97, int(o[1]) - 1] in "XO"



def game(sym, px=1):
    print("Positions:")
    print(
        " ".join([f"a{i}" for i in range(1, 4)]),
        " ".join([f"b{i}" for i in range(1, 4)]),
        " ".join([f"c{i}" for i in range(1, 4)]),
        sep="\n",
    )
    print(f"Player {px} chance:")
    p = input("Please Enter Position: ").lower()
    while p not in [f"{x}{i}" for i in range(1, 4) for x in "abc"] or calc_occupied(p):
        print("Invalid Option")
        p = input("Please Enter Position: ").lower()
    o = list(p)
    x = grid[ord(o[0]) - 97, int(o[1]) - 1]
    grid[ord(o[0]) - 97, int(o[1]) - 1] = sym if x == " " else x
    return condition(grid)


def mainloop():
    while True:
        j = game("X")
        if j:
            board()
            print(f"\n{j[0]} wins")
            break
        board()

        if draw_prob():
            print("Draw")
            break

        j = game("O", 2)
        if j:
            board()
            print(f"\n{j[0]} wins")
            break
        board()


if __name__ == "__main__":
    mainloop()
