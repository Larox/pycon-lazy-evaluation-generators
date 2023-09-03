from typing import Generator


def my_custom_range(start: int, stop: int, step: int = 1) -> Generator[int, None, None]:
    value = start
    while value < stop:
        yield value
        value = value + step


if __name__ == "__main__":
    range_custom = my_custom_range(1, 10)
    print(type(range_custom))
    print(type(my_custom_range))

    for i in range_custom:
        print(i)
