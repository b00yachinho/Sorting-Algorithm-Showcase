import random
import sys
import time
from algs import Bubble, Insert, Select, Quick, Merge, Count, Bucket, NaturalMerge, Tim, Heap


def sort_it(given_list, what_do):

    if what_do == 1:
        sort = Bubble()
        sort.bubble_sort(given_list)
    elif what_do == 2:
        sort = Insert()
        sort.insertion_sort(given_list)
    elif what_do == 3:
        sort = Select()
        sort.selection_sort(given_list)
    elif what_do == 4:
        sort = Quick()
        sort.quicksort(given_list)
    elif what_do == 5:
        sort = Merge()
        sort.mergesort(given_list)
    elif what_do == 6:
        sort = Count()
        sort.counting_sort(given_list)
    elif what_do == 7:
        sort = Bucket()
        sort.bucket_sort(given_list)
    elif what_do == 8:
        sort = NaturalMerge()
        sort.natural_merge_sort(given_list)
    elif what_do == 9:
        sort = Tim()
        sort.timsort(given_list)
    elif what_do == 10:
        sort = Heap()
        sort.heap_sort(given_list)
    else:
        print("You shouldn't be here...")
        sys.exit(1)

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

tmp = "Execution time may be longer than usual due to the printing of algorithm steps"
print("***" + tmp.upper() + "***")

print("\nSorting algorithms (no particular order):")
for number, name in algorithm_names.items():
    print(f"{number}. {name}")

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
