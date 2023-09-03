import timeit
from typing import Generator
from memory_profiler import profile as mem_profiler


def data_generator() -> Generator[int, None, None]:
    for i in range(10**6):
        if i % 2 == 0:
            yield i


@mem_profiler
def get_even_number_sum_lazy():
    number_generator = data_generator()
    return sum(number_generator)


get_even_number_sum_lazy()

if __name__ == "__main__":
    print(
        timeit.timeit(
            "get_even_number_sum_lazy()",
            setup="from __main__ import get_even_number_sum_lazy",
            number=1,
        )
    )
