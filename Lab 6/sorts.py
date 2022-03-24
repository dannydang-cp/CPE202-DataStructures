import random
import time


def selection_sort(alist):
    counter = 0
    for i in range(0, len(alist) - 1):
        min_value = i

        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_value]:
                min_value = j
            counter += 1

        if min_value != i:
            alist[min_value], alist[i] = alist[i], alist[min_value]

    return counter


def insertion_sort(alist):
    counter = 0
    for i in range(1, len(alist)):
        value_to_sort = alist[i]
        while alist[i - 1] > value_to_sort and i > 0:  # Previous value is greater than the next value
            alist[i], alist[i - 1] = alist[i - 1], alist[i]  # Swap the values
            i -= 1
            counter += 1
        if alist[i - 1] < value_to_sort and i > 0:  # adds 1 to the counter for last comparisons with value_to_sort
            counter += 1

    return counter


def merge_sort(alist):
    counter = 0
    if len(alist) > 1:
        middle_index = len(alist) // 2
        left_half = alist[:middle_index]
        right_half = alist[middle_index:]

        # recursion
        a = merge_sort(left_half)
        b = merge_sort(right_half)

        # Adds the counters from the recursion
        c = a + b

        # merge
        i = 0  # left array index
        j = 0  # right array index
        k = 0  # merged array index

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # left array less than right array at current index
                alist[k] = left_half[i]  # saves the value of left array inside merge array
                i += 1  # increase i to next index as it is saved in the merge array now
            else:
                alist[k] = right_half[j]  # saves the value of right array inside merge array
                j += 1  # increase j index as it is saved inside merge array
            k += 1  # increase k index as new value is in merge array
            counter += 1

        # Adds all the counters together
        counter += c

        # left over element in left array and right array is fully added into merged array
        while i < len(left_half):
            alist[k] = left_half[i]  # saves the last value in the left array into the merge array
            i += 1
            k += 1

        # left over element in right array and left array is fully added into merge array
        while j < len(right_half):
            alist[k] = right_half[j]  # saves the value of right array inside merge array
            j += 1
            k += 1
    return counter




def main():
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 8000)
    start_time = time.time()
    comps = selection_sort(randoms)
    stop_time = time.time()


   # print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()
