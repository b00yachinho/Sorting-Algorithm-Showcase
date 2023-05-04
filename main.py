import random
import sys
import time
from algs import Bubble, Insert, Select, Quick, Merge, Count, Bucket, NaturalMerge, Tim, Heap


def sort_it(given_list, what_do):
    sorting_classes = {
        1: {"name": "Bubble Sort", "class": Bubble(), "func": Bubble.bubble_sort},
        2: {"name": "Insertion Sort", "class": Insert(), "func": Insert.insertion_sort},
        3: {"name": "Selection Sort", "class": Select(), "func": Select.selection_sort},
        4: {"name": "Quick Sort", "class": Quick(), "func": Quick.quicksort},
        5: {"name": "Merge Sort", "class": Merge(), "func": Merge.mergesort},
        6: {"name": "Counting Sort", "class": Count(), "func": Count.counting_sort},
        7: {"name": "Bucket Sort", "class": Bucket(), "func": Bucket.bucket_sort},
        8: {"name": "Natural Merge Sort", "class": NaturalMerge(), "func": NaturalMerge.natural_merge_sort},
        9: {"name": "Timsort", "class": Tim(), "func": Tim.timsort},
        10: {"name": "Heap Sort", "class": Heap(), "func": Heap.heap_sort}
    }

    if what_do not in sorting_classes:
        print("You shouldn't be here...")
        sys.exit(1)

    sorting_instance = sorting_classes[what_do]["class"]
    sort_func = sorting_classes[what_do]["func"]
    sort_func(sorting_instance, given_list)

    return given_list


algorithm_names = {
    1: "Bubble Sort",
    2: "Insertion Sort",
    3: "Selection Sort",
    4: "Quick Sort",
    5: "Merge Sort",
    6: "Counting Sort",
    7: "Bucket Sort",
    8: "Natural Merge Sort",
    9: "Timsort",
    10: "Heap Sort"
}

print("***EXECUTION TIME MAY BE LONGER THAN USUAL DUE TO THE PRINTING OF ALGORITHM STEPS***")

print("\nSorting algorithms (no particular order):")
for number, name in algorithm_names.items():
    if number != 10:
        print(f"{number}. {name},")
    else:
        print(f"{number}. {name}.")

while True:
    choice = int(input("\nSelect an algorithm -> "))
    if choice in algorithm_names:
        print(f"\nSelected {algorithm_names[choice]}...")
        break
    else:
        print("\nWrong value given. Please try again...")

n = int(input("\nLength of the list -> "))
list_before = [random.randint(1, 100) for _ in range(n)]
list_after = list_before.copy()
print()

start_time = time.time()
sort_it(list_after, choice)
end_time = time.time()

print("\nList before sorting:", list_before)
print("\nList after sorting:", list_after)
print("\nList sorted in:", end_time - start_time, "seconds.")
