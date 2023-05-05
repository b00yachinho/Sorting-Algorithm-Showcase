import random
import sys
import time
from algs import Bubble, Insert, Select, Quick, Merge, Count, Bucket, NaturalMerge, Tim, Heap


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

algorithm_names = [sorting_classes[i]["name"] for i in range(1, len(sorting_classes) + 1)]

print("Sorting algorithms (no particular order):")
for number, name in enumerate(algorithm_names):
    if number != len(algorithm_names) - 1:
        print(f"{number + 1}. {name},")
    elif number == len(algorithm_names) - 1:
        print(f"{number + 1}. {name}.")
    else:
        print("\nYou shouldn't be here.")
        sys.exit(1)

while True:
    choice = int(input("\nSelect an algorithm -> "))
    if 1 <= choice <= len(algorithm_names):
        print(f"\nSelected {algorithm_names[choice - 1]}...")
        break
    else:
        print("\nWrong value given. Please try again...")

while True:
    steps = input("\nShow steps of the algorithm? (y/n) -> ")
    if steps != 'y' and steps != 'n':
        print('\nWrong value given.')
    elif steps == 'y':
        print("\nExecution time may be longer than expected, due to printing of steps of the algorithm.")
        break
    else:
        break

n = int(input("\nLength of the list -> "))
print()

list_before = [random.randint(1, 100) for _ in range(n)]
list_after = list_before.copy()

sorting_instance = sorting_classes[choice]["class"]
sort_func = sorting_classes[choice]["func"]

start_time = time.time()
sort_func(sorting_instance, list_after, steps)
end_time = time.time()

print("\nList before sorting:", list_before)
print("\nList after sorting:", list_after)
print("\nList sorted in:", end_time - start_time, "seconds.")
