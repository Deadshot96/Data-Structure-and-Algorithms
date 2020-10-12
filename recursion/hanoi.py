from typing import Text, NoReturn
def hanoi(n: int, s: Text, d: Text, t: Text) -> NoReturn:
    if n == 0:
        return 
    hanoi(n - 1, s, t, d)
    print(f"Move {n} from {s} to {d}")
    hanoi(n - 1, t, d, s)

if __name__ == "__main__":
    n = input("Input the availabel disks: ")
    if n != "":
        hanoi(int(n), 'source', 'dest', 'temp')
