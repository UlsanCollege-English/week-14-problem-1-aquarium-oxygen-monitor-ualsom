"""
HW01 — Aquarium Oxygen Monitor (Sliding Window)

Implement max_window_sum(readings, k) to return the maximum sum of any
contiguous subarray of length k.

See README.md for full problem description and constraints.
"""


def max_window_sum(readings, k):
    """
    Return the maximum sum of any contiguous subarray of length k.

    :param readings: list of integers (may be positive, zero, or negative)
    :param k: length of the sliding window (int)
    :return: maximum sum over all windows of size k (int)
    :raises ValueError: if k <= 0, k > len(readings), or readings is empty
    """
    # ---- Input Validation ----
    if not readings:
        raise ValueError("readings cannot be empty")
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(readings):
        raise ValueError("k cannot be larger than number of readings")

    # ---- Compute initial window sum ----
    window_sum = sum(readings[:k])
    max_sum = window_sum

    # ---- Slide the window across the array ----
    for i in range(k, len(readings)):
        window_sum += readings[i]          # add the new element
        window_sum -= readings[i - k]      # remove the old element
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    # Optional manual testing
    sample_readings = [3, 1, 2, 7, 4, 2]
    sample_k = 3
    print(max_window_sum(sample_readings, sample_k))
