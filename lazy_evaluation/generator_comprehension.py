from my_custom_range_generator import my_custom_range

square = (i * 2 for i in my_custom_range(0, 10))


if __name__ == "__main__":
    print(type(square))

    print(next(square))
    print(next(square))
    print(next(square))
