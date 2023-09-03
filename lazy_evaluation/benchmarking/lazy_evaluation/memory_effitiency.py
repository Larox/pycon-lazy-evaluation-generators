import timeit
from typing import Generator
from memory_profiler import profile as mem_profiler


def is_even(number: int) -> bool:
    return number % 2 == 0


def data_generator() -> Generator[int, None, None]:
    for i in range(10**6):
        yield i


@mem_profiler
def get_list_even_lazy_evaluation():
    for item in data_generator():
        is_even(item)


get_list_even_lazy_evaluation()

if __name__ == "__main__":
    print(
        timeit.timeit(
            "get_list_even_lazy_evaluation()",
            setup="from __main__ import get_list_even_lazy_evaluation",
            number=1,
        )
    )
