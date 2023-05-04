class Bubble:
    def bubble_sort(self, given_list):
        n = len(given_list)

        for i in range(n):
            for j in range(n - i - 1):
                if given_list[j] > given_list[j + 1]:
                    given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
                    print(given_list)
        return given_list


class Insert:
    def insertion_sort(self, given_list):
        for i in range(1, len(given_list)):
            key = given_list[i]
            j = i - 1
            while j >= 0 and key < given_list[j]:
                given_list[j + 1] = given_list[j]
                j -= 1
            given_list[j + 1] = key
            print(given_list)
        return given_list


class Select:
    def selection_sort(self, given_list):
        n = len(given_list)

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if given_list[j] < given_list[min_index]:
                    min_index = j
            given_list[i], given_list[min_index] = given_list[min_index], given_list[i]
            print(given_list)
        return given_list


class Quick:
    def quicksort(self, given_list):
        if len(given_list) <= 1:
            return given_list
        else:
            pivot = given_list[0]
            lower = [x for x in given_list[1:] if x < pivot]
            higher = [x for x in given_list[1:] if x >= pivot]
            sorted_lower = self.quicksort(lower)
            sorted_higher = self.quicksort(higher)
            sorted_given_list = sorted_lower + [pivot] + sorted_higher
            print(sorted_given_list)
            given_list[:] = sorted_given_list
        return given_list


class Merge:
    def mergesort(self, given_list):
        if len(given_list) <= 1:
            return given_list
        else:
            mid = len(given_list) // 2
            left = given_list[:mid]
            right = given_list[mid:]
            left_sorted = self.mergesort(left)
            right_sorted = self.mergesort(right)
            sorted_given_list = self.merge(left_sorted, right_sorted)
            print(sorted_given_list)
            given_list[:] = sorted_given_list
        return given_list

    def merge(self, given_list1, given_list2):
        i = j = 0
        result = []

        while i < len(given_list1) and j < len(given_list2):
            if given_list1[i] < given_list2[j]:
                result.append(given_list1[i])
                i += 1
            else:
                result.append(given_list2[j])
                j += 1
        result.extend(given_list1[i:])
        result.extend(given_list2[j:])
        return result


class Count:
    def counting_sort(self, given_list):
        max_value = max(given_list)
        count = [0] * (max_value + 1)

        for i in range(len(given_list)):
            count[given_list[i]] += 1
        sorted_list = []
        for i in range(len(count)):
            sorted_list += [i] * count[i]
            print(sorted_list)
        given_list[:] = sorted_list
        return given_list


class Bucket:
    def bucket_sort(self, given_list):
        min_value = min(given_list)
        max_value = max(given_list)
        n = len(given_list)

        bucket_count = [0] * (max_value - min_value + 1)
        for i in range(n):
            bucket_count[given_list[i] - min_value] += 1
        sorted_list = []
        for i in range(len(bucket_count)):
            if bucket_count[i] != 0:
                sorted_list += [i + min_value] * bucket_count[i]
                print(sorted_list)
        given_list[:] = sorted_list
        return given_list


class NaturalMerge:
    def natural_merge_sort(self, given_list):
        if len(given_list) <= 1:
            return given_list

        def get_next_run(start):
            end = start + 1
            while end < len(given_list) and given_list[end] >= given_list[end - 1]:
                end += 1
            return start, end

        runs = []
        start = 0
        while start < len(given_list):
            start, end = get_next_run(start)
            runs.append(given_list[start:end])
            start = end

        while len(runs) > 1:
            result = []
            i, j = 0, 1
            while j < len(runs):
                merged = self.merge(runs[i], runs[j])
                result.append(merged)
                i, j = i + 2, j + 2
            if i < len(runs):
                result.append(runs[i])
            runs = result

        given_list[:] = runs[0]
        return given_list

    def merge(self, given_list1, given_list2):
        i = j = 0
        result = []

        while i < len(given_list1) and j < len(given_list2):
            if given_list1[i] < given_list2[j]:
                result.append(given_list1[i])
                i += 1
            else:
                result.append(given_list2[j])
                j += 1

        result.extend(given_list1[i:])
        result.extend(given_list2[j:])
        print(result)
        return result


class Tim:
    def timsort(self, given_list):
        minrun = 32
        n = len(given_list)

        for i in range(0, n, minrun):
            self.insertion_sort(given_list, i, min(i + minrun - 1, n - 1))
        size = minrun

        while size < n:
            for start in range(0, n, size * 2):
                midpoint = start + size - 1
                end = min(start + size * 2 - 1, n - 1)
                print("Merge - start: {}, midpoint: {}, end: {}".format(start, midpoint, end))
                merged_list = self.merge(given_list[start:midpoint + 1], given_list[midpoint + 1:end + 1])
                print("Merged list: {}".format(merged_list))
                given_list[start:start + len(merged_list)] = merged_list
                print("List after merging: {}".format(given_list))
            size *= 2
        return given_list

    def insertion_sort(self, given_list, left, right):
        for i in range(left + 1, right + 1):
            key = given_list[i]
            j = i - 1
            while j >= left and given_list[j] > key:
                given_list[j + 1] = given_list[j]
                j -= 1
            given_list[j + 1] = key
        print("List agter insertion sort: {}".format(given_list))

    def merge(self, given_list1, given_list2):
        i = j = 0
        result = []

        while i < len(given_list1) and j < len(given_list2):
            if given_list1[i] < given_list2[j]:
                result.append(given_list1[i])
                i += 1
            else:
                result.append(given_list2[j])
                j += 1
        result.extend(given_list1[i:])
        result.extend(given_list2[j:])
        return result


class Heap:
    def heap_sort(self, given_list):
        n = len(given_list)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(given_list, n, i)

        for i in range(n - 1, 0, -1):
            given_list[0], given_list[i] = given_list[i], given_list[0]
            self.heapify(given_list, i, 0)
        return given_list

    def heapify(self, given_list, heap_size, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < heap_size and given_list[left] > given_list[largest]:
            largest = left

        if right < heap_size and given_list[right] > given_list[largest]:
            largest = right

        if largest != i:
            given_list[i], given_list[largest] = given_list[largest], given_list[i]
            self.heapify(given_list, heap_size, largest)
        print(given_list)
        return given_list

