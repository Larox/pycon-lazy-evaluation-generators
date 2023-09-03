import timeit
from memory_profiler import profile as mem_profiler


@mem_profiler
def get_even_number_sum_eager() -> int:
    even_numbers_list = [n for n in range(10**6) if n % 2 == 0]
    return sum(even_numbers_list)


get_even_number_sum_eager()


if __name__ == "__main__":
    print(
        "execution time eager evaluation: ",
        timeit.timeit(
            "get_even_number_sum_eager()",
            setup="from __main__ import get_even_number_sum_eager",
            number=1,
        ),
    )
