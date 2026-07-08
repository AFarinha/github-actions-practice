def add(left: int, right: int) -> int:
    return left + right


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 is even: {is_even(4)}")

