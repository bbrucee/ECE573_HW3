from Q1.Q1 import insertion_sort, shell_sort
from Q2.Q2 import kendalltau
from Q3.Q3 import bubblesort
from Q4.Q4 import mergesort_insertion_cutoff, iterative_mergesort, recursive_mergesort
from Q5.Q5 import quicksort, quicksort_insertion_cutoff
import matplotlib.pyplot as plt
import os
import timeit
import functools
from random import shuffle
import random


def shellsort_comps(dataset_number=1):
    shell_sort_comps = []
    partial_insertion_sort_comps = []
    insertion_sort_comps = []
    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q1/data/data{}.{}".format(dataset_number, data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        print(sorted(data_array))
        # ss_comp, p_insert = shell_sort(data_array[:])
        # shell_sort_comps.append(ss_comp)
        # partial_insertion_sort_comps.append(p_insert)
        # insertion_sort_comps.append(insertion_sort(data_array[:]))

    columns = ('Shell Sort: Total Comparisons', 'Shell Sort: Insertion Sort Comparisons', 'Insertion Sort: Comparisons')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(shell_sort_comps, partial_insertion_sort_comps, insertion_sort_comps):
        cell_text.append(["{} Comparisons".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q1: Shell Sort and Insertion Sort Graphs using data{}".format(dataset_number))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 3), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 3), (0, 0))
    plt.plot(data_sizes, shell_sort_comps)
    plt.title("Shell Sort: Total Comparisons", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Number of Comparisons")
    plt.subplot2grid((2, 3), (0, 1))
    plt.plot(data_sizes, partial_insertion_sort_comps)
    plt.title("Shell Sort: Insertion Sort Phase", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Number of Comparisons")
    plt.subplot2grid((2, 3), (0, 2))
    plt.plot(data_sizes, insertion_sort_comps)
    plt.title("Insertion Sort: Comparisons", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Number of Comparisons")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def kendalltau_outputs(dataset_number=1):
    kd_merge_outputs = []
    bubble_outputs = []
    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q2/data/data{}.{}".format(dataset_number, data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()

        kd_merge_outputs.append(kendalltau(data_array))
        bubble_outputs.append(bubblesort(data_array)[1])

    columns = ('Kendall Tau Distance: Merge Sort', 'Kendall Tau Distance: Bubble Sort')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(kd_merge_outputs, bubble_outputs):
        cell_text.append(["Distance is {}".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q2: Kendall Tau Distance Graphs using data{}".format(dataset_number))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_sizes, kd_merge_outputs)
    plt.title("Kendall Tau: Merge Sort O(nlogn)", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Kendall Tau Distance")
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_sizes, bubble_outputs)
    plt.title("Kendall Tau: Bubble Sort O(n^2)", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Kendall Tau Distance")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def kendalltau_timing(dataset_number=1):
    kd_merge_timings = []
    bubble_timings = []
    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q2/data/data{}.{}".format(dataset_number, data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()

        kd_timer = timeit.Timer(functools.partial(kendalltau, data_array))
        kd_merge_timings.append(kd_timer.timeit(1))
        bb_time = timeit.Timer(functools.partial(bubblesort, data_array))
        bubble_timings.append(bb_time.timeit(1))

    columns = ('Kendall Tau Distance: Merge Sort', 'Kendall Tau Distance: Bubble Sort')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(kd_merge_timings, bubble_timings):
        cell_text.append(["{0:.10f} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q2: Kendall Tau Runtime Graphs using data{}".format(dataset_number))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_sizes, kd_merge_timings)
    plt.title("Kendall Tau: Merge Sort O(nlogn)", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_sizes, bubble_timings)
    plt.title("Kendall Tau: Bubble Sort O(n^2)", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def mergesort_vs_mergesort(dataset_number=1):
    rec_comps = []
    ite_comps = []

    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q4/data/data{}.{}".format(dataset_number, data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        rec_comps.append(recursive_mergesort(data_array[:], 0, len(data_array)-1))
        ite_comps.append(iterative_mergesort(data_array[:]))

    columns = ('Recursive Merge Sort', 'Iterative Merge Sort')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(rec_comps, ite_comps):
        cell_text.append(["{} comparisons".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q4: Recursive vs Iterative Merge Sort Comparisons using data{}".format(dataset_number))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_sizes, rec_comps)
    plt.title("Recursive Merge Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Number of Comparisons")
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_sizes, ite_comps)
    plt.title("Iterative Merge Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Number of Comparisons")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def quicksort_vs_mergesort(dataset_number=1):
    ite_ms_timings = []
    ms_timings = []
    qs_timings = []

    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q4/data/data{}.{}".format(dataset_number, data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        ms_timer = timeit.Timer(functools.partial(recursive_mergesort, data_array[:], 0, len(data_array)-1))
        ms_timings.append(ms_timer.timeit(1))
        ite_ms_timer = timeit.Timer(functools.partial(iterative_mergesort, data_array[:]))
        ite_ms_timings.append(ite_ms_timer.timeit(1))
        qs_timer = timeit.Timer(functools.partial(quicksort, data_array[:], 0, len(data_array)))
        qs_timings.append(qs_timer.timeit(1))

    rel_path = "/Q5/data/data{}.{}".format(dataset_number, 32768)
    cwd = os.getcwd()
    abs_file_path = cwd + rel_path
    input_file = open(abs_file_path)
    data_array = []
    for line in input_file.readlines():
        data_array.append(int(line))
    input_file.close()
    data_array = data_array * 256
    if dataset_number == 0:
        data_array.sort()
    else:
        shuffle(data_array)
    data_sizes.append(len(data_array))
    ms_timer = timeit.Timer(functools.partial(mergesort_insertion_cutoff, data_array[:], 0, len(data_array) - 1))
    ms_timings.append(ms_timer.timeit(1))
    qs_timer = timeit.Timer(functools.partial(quicksort_insertion_cutoff, data_array[:], 0, len(data_array)))
    qs_timings.append(qs_timer.timeit(1))

    columns = ('Merge Sort', 'Quick Sort')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(ms_timings, qs_timings):
        cell_text.append(["{0:.10f} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q5: Merge Sort vs Quick Sort Runtime Comparison using data{}".format(dataset_number))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_sizes[:-1], ms_timings[:-1])
    plt.title("Merge Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_sizes[:-1], qs_timings[:-1])
    plt.title("Quick Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def quicksort_vs_mergesort_cutoffs(dataset_number=1):
    ms_timings = []
    qs_timings = []

    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q5/data/data{}.{}".format(dataset_number, data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        ms_timer = timeit.Timer(functools.partial(mergesort_insertion_cutoff, data_array[:], 0, len(data_array) - 1))
        ms_timings.append(ms_timer.timeit(1))
        qs_timer = timeit.Timer(functools.partial(quicksort_insertion_cutoff, data_array[:], 0, len(data_array)))
        qs_timings.append(qs_timer.timeit(1))

    rel_path = "/Q5/data/data{}.{}".format(dataset_number, 32768)
    cwd = os.getcwd()
    abs_file_path = cwd + rel_path
    input_file = open(abs_file_path)
    data_array = []
    for line in input_file.readlines():
        data_array.append(int(line))
    input_file.close()
    data_array = data_array*256
    if dataset_number == 0:
        data_array.sort()
    else:
        shuffle(data_array)
    data_sizes.append(len(data_array))
    ms_timer = timeit.Timer(functools.partial(mergesort_insertion_cutoff, data_array[:], 0, len(data_array) - 1))
    ms_timings.append(ms_timer.timeit(1))
    qs_timer = timeit.Timer(functools.partial(quicksort_insertion_cutoff, data_array[:], 0, len(data_array)))
    qs_timings.append(qs_timer.timeit(1))

    columns = ('Merge-Insertion Hybrid Sort', 'Quick-Insertion Hybrid Sort')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(ms_timings, qs_timings):
        cell_text.append(["{0:.10f} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q5: Merge Sort vs Quick Sort Runtime Comparison w/ N=7 Cutoff on data{}".format(dataset_number))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_sizes[:-1], ms_timings[:-1])
    plt.title("Merge-Insertion Hybrid Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_sizes[:-1], qs_timings[:-1])
    plt.title("Quick-Insertion Hybrid Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def quicksort_varying_cutoffs(dataset_number=1):
    qs_timings = []
    data_sizes = [32768]
    cutoffs = range(10, 10000, 100)
    for cutoff in cutoffs:
        for data_size in data_sizes:
            rel_path = "/Q5/data/data{}.{}".format(dataset_number, data_size)
            cwd = os.getcwd()
            abs_file_path = cwd + rel_path
            input_file = open(abs_file_path)
            data_array = []
            for line in input_file.readlines():
                data_array.append(int(line))
            input_file.close()
            data_array = 4*data_array
            shuffle(data_array)
            qs_timer = timeit.Timer(functools.partial(quicksort_insertion_cutoff, data_array[:], 0, len(data_array), cutoff))
        qs_timings.append(qs_timer.timeit(1))

    columns = ('Quick Sort-Insertion Sort Hybrid',)
    rows = ["N = {}".format(x) for x in cutoffs]
    cell_text = []
    for time_tuple in zip(qs_timings):
        cell_text.append(["{0:10f}".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q5: Quick Sort Varying Cutoff w/ 131072 elements using data{}".format(dataset_number))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
    ax.table(cellText=cell_text[::10], rowLabels=rows[::10], colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0), colspan=2, rowspan=1)
    plt.plot(cutoffs, qs_timings)
    plt.title("Runtime for different cutoffs", y=1.08)
    plt.xlabel("Cutoff for Insertion Sort")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def quicksort_vs_mergesort_bonus():
    ms_timings = []
    qs_timings = []

    data_sizes = [2**x for x in range(10, 25)]
    for data_size in data_sizes:
        data_array = list(range(data_size))
        shuffle(data_array)
        ms_timer = timeit.Timer(functools.partial(recursive_mergesort, data_array[:], 0, len(data_array[:])-1))
        ms_timings.append(ms_timer.timeit(1))
        qs_timer = timeit.Timer(functools.partial(quicksort, data_array[:], 0, len(data_array[:])))
        qs_timings.append(qs_timer.timeit(1))

    columns = ('Merge Sort', 'Quick Sort')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(ms_timings, qs_timings):
        cell_text.append(["{0:.10f} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Bonus: Merge Sort vs Quick Sort Runtime Comparison")
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_sizes[:-1], ms_timings[:-1])
    plt.title("Merge Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_sizes[:-1], qs_timings[:-1])
    plt.title("Quick Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def quicksort_vs_mergesort_bonus_random_range(random_a=0, random_b=10):
    ms_timings = []
    qs_timings = []

    data_sizes = [2**x for x in range(10, 15)]
    for data_size in data_sizes:
        data_array = []
        for _ in range(data_size):
            data_array.append(random.randint(random_a, random_b))
        ms_timer = timeit.Timer(functools.partial(recursive_mergesort, data_array[:], 0, len(data_array[:])-1))
        ms_timings.append(ms_timer.timeit(1))
        qs_timer = timeit.Timer(functools.partial(quicksort, data_array[:], 0, len(data_array[:])))
        qs_timings.append(qs_timer.timeit(1))

    columns = ('Merge Sort', 'Quick Sort')
    rows = ["{} integers".format(x) for x in data_sizes]
    cell_text = []
    for time_tuple in zip(ms_timings, qs_timings):
        cell_text.append(["{0:.10f} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Bonus: Merge Sort vs Quick Sort Runtime Comparison randint({},{})".format(random_a, random_b))
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0))
    plt.plot(data_sizes[:-1], ms_timings[:-1])
    plt.title("Merge Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(data_sizes[:-1], qs_timings[:-1])
    plt.title("Quick Sort", y=1.08)
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=12, h=10)
    plt.show()


def main():
    # shellsort_comps(0)
    shellsort_comps()
    # kendalltau_outputs(0)
    # kendalltau_outputs()
    # kendalltau_timing(0)
    # kendalltau_timing()
    # mergesort_vs_mergesort(0)
    # mergesort_vs_mergesort()
    # quicksort_vs_mergesort(0)
    # quicksort_vs_mergesort()
    # quicksort_vs_mergesort_cutoffs(0)
    # quicksort_vs_mergesort_cutoffs()
    # quicksort_varying_cutoffs(0)
    # quicksort_varying_cutoffs()
    # quicksort_vs_mergesort_bonus_random_range()


if __name__ == '__main__':
    main()