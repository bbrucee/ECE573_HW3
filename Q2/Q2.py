import sys
import os
import csv


# https://www.geeksforgeeks.org/insertion-sort/
# Input is any length array
# After function call array is sorted
# Returns number of comparisons
def insertion_sort(input_array):
    comparisons = 0
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i - 1
        while j >= 0 and key < input_array[j]:
            comparisons += 1
            input_array[j + 1] = input_array[j]
            j -= 1
        comparisons += 1
        input_array[j + 1] = key
    return comparisons


# https://www.geeksforgeeks.org/python-program-for-shellsort/
# Input is any length array
# After function call array is 7-sorted
# Returns number of comparisons
def shell7(input_array):
    comparisons = 0
    for i in range(7, len(input_array)):
        key = input_array[i]
        j = i
        while j >= 7 and input_array[j - 7] > key:
            comparisons += 1
            input_array[j] = input_array[j - 7]
            j -= 7
        comparisons += 1
        input_array[j] = key
    return comparisons


# Input is any length array
# After function call array is 3-sorted
# Returns number of comparisons
def shell3(input_array):
    comparisons = 0
    for i in range(3, len(input_array)):
        key = input_array[i]
        j = i
        while j >= 3 and input_array[j - 3] > key:
            comparisons += 1
            input_array[j] = input_array[j - 3]
            j -= 3
        comparisons += 1
        input_array[j] = key
    return comparisons


# Input is any length array
# After function call array is sorted
# Returns number of comparisons
def shell_sort(input_array):
    comparisons = 0
    insertion_partial = 0
    comparisons += shell7(input_array)
    comparisons += shell3(input_array)
    insertion_partial += insertion_sort(input_array)
    return comparisons+insertion_partial, insertion_partial


def parse_input_file(input_file):
    data_array = []
    for line in input_file.readlines():
        print(line)
        # data_array.append(int(line))
    print("Input data: {}".format(data_array))
    return data_array


def main():
    try:
        # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        rel_path = "/data/data1.1024"
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        print("Input data: {}".format(data_array))
        print("Shell sort called on data_array, used (total, insertion phase) -> {}".format(shell_sort(data_array)))
        print("Does sorted(data_array) equal data_array after shell_sort?: {}".format(data_array == sorted(data_array)))

    except IndexError:
        print("No input data file")


if __name__ == '__main__':
    main()
