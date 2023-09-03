import csv
import timeit
from memory_profiler import profile as mem_profile, memory_usage


@mem_profile
def read_csv_with_eager_evaluation(file_path: str) -> list[str]:
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        return [row for row in csv_reader]


@mem_profile
def loop_csv_line_generator(file_path: str):
    for i in read_csv_with_eager_evaluation(file_path):
        pass


if __name__ == "__main__":
    csv_file_path = "/Users/sebastianarias/Documents/python-conference/lazy_evaluation/lazy_evaluation/examples/large_data_set_processing/organization1m.csv"
    print(f"Memory (Before): {str(memory_usage())} 'MB'")
    loop_csv_line_generator(csv_file_path)
    print(f"Memory (After): {str(memory_usage())} 'MB'")
    timer = timeit.Timer(lambda: read_csv_with_eager_evaluation(csv_file_path))
    print(timer.timeit(1))
