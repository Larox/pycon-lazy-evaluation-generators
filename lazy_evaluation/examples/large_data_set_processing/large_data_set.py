from typing import Generator
import timeit
import csv

from memory_profiler import profile as mem_profiler, memory_usage


@mem_profiler
def read_csv_with_generator(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            yield row


@mem_profiler
def loop_csv_line_generator(file_path: str):
    for i in read_csv_with_generator(file_path):
        pass


if __name__ == "__main__":
    csv_file_path = "/Users/sebastianarias/Documents/python-conference/lazy_evaluation/lazy_evaluation/examples/large_data_set_processing/organization1m.csv"

    print(f"Memory (Before): {str(memory_usage())} 'MB'")
    loop_csv_line_generator(csv_file_path)
    print(f"Memory (After): {str(memory_usage())} 'MB'")

    timer = timeit.Timer(lambda: read_csv_with_generator(csv_file_path))
    print(timer.timeit(1))
