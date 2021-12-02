from typing import List


def count_depth_increase(depths: List[int]) -> int:
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            count += 1

    return count


def count_depth_sliding_window(depths: List[int]) -> int:
    # window size = 3
    count = 0
    for i in range(len(depths) - 3):
        if (depths[i+1] + depths[i+2] + depths[i+3]) > (depths[i] + depths[i+1] + depths[i+2]):
            count += 1

    return count

if __name__ == "__main__":
    depths = []
    with open('day_1_input.txt') as f:
        for line in f:
            depths.append(int(line.strip()))

    print(count_depth_increase(depths))
    print(count_depth_sliding_window(depths))
