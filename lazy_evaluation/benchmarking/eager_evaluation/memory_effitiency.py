import timeit
from memory_profiler import profile as mem_profiler


def is_even(number: int) -> bool:
    return number % 2 == 0


@mem_profiler
def get_list_even_eager_evaluation():
    for item in [n for n in range(10**6)]:
        is_even(item)


get_list_even_eager_evaluation()


if __name__ == "__main__":
    print(
        timeit.timeit(
            "get_list_even_eager_evaluation()",
            setup="from __main__ import get_list_even_eager_evaluation",
            number=1,
        )
    )
