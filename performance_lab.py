# performance_lab.py

# -------------------------
 1: Find Most Frequent Element (Optimized)
# -------------------------
def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    max_count = 0
    most_freq = numbers[0]

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > max_count:
            max_count = counts[num]
            most_freq = num

    return most_freq

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) - must iterate through all elements to find max frequency
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(k) where k is number of unique elements
- Why this approach? Single-pass calculation avoids building full Counter object; updates max dynamically
- Could it be optimized? Already optimized for single pass and minimal extra space
"""

# -------------------------
 2: Remove Duplicates While Preserving Order
# -------------------------
def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) - storing seen elements
- Why this approach? Preserves order while efficiently checking duplicates
- Could it be optimized? Minimal; dict.fromkeys could be used in Python 3.7+ with similar complexity
"""

# -------------------------
 3: Return All Pairs That Sum to Target
# -------------------------
def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) - store seen elements and pairs
- Why this approach? Efficient single-pass hashing, avoids nested loops
- Could it be optimized? Already linear; nested loops would be O(n^2)
"""

# -------------------------
 4: Simulate List Resizing (Amortized Cost)
# -------------------------
def add_n_items(n, initial_capacity=2):
    capacity = initial_capacity
    arr = [None] * capacity
    size = 0
    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity*2}")
            new_arr = [None] * (capacity * 2)
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
            capacity *= 2
        arr[size] = i
        size += 1
    return arr[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When current size reaches capacity
- Worst-case for single append: O(n) due to copying all elements
- Amortized time per append: O(1) - doubling ensures average cost is constant
- Space complexity: O(n)
- Why doubling reduces cost: Fewer resizes overall; total copying over n elements is ~2n
"""

# -------------------------
 5: Compute Running Totals
# -------------------------
def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) - creating new list
- Why this approach? Single-pass accumulation is efficient
- Could it be optimized? Could do in-place if allowed to save memory
"""

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    print("Problem 1:", most_frequent([1, 3, 2, 3, 4, 1, 3]))  # 3
    print("Problem 2:", remove_duplicates([4, 5, 4, 6, 5, 7]))  # [4, 5, 6, 7]
    print("Problem 3:", find_pairs([1, 2, 3, 4], 5))  # [(1, 4), (2, 3)]
    print("Problem 4:")
    add_n_items(6)  # Should print resizing messages
    print("Problem 5:", running_total([1, 2, 3, 4]))  # [1, 3, 6, 10]
