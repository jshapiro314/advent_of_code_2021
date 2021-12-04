from collections import Counter
from typing import List, Tuple


def power_consumption(diagnostics: List[List[int]]) -> int:
    column_lists = list(zip(*diagnostics))

    gamma_rate = []
    epsilon_rate = []
    for col in column_lists:
        common_list = Counter(col).most_common()
        gamma_rate.append(common_list[0][0])
        epsilon_rate.append(common_list[-1][0])

    gamma_str = "".join(gamma_rate)
    epsilon_str = "".join(epsilon_rate)

    gamma_int = int(gamma_str, 2)
    epsilon_int = int(epsilon_str, 2)

    return gamma_int * epsilon_int


def life_support_rating(diagnostics: List[List[int]]) -> int:
    valid_indices = set(range(len(diagnostics)))

    column_lists = list(zip(*diagnostics))

    oxygen_id = _oxygen_id(column_lists)
    co2_id = _co2_id(column_lists)

    oxygen_str = "".join(diagnostics[oxygen_id])
    co2_str = "".join(diagnostics[co2_id])

    oxygen_int = int(oxygen_str, 2)
    co2_int = int(co2_str, 2)

    return oxygen_int * co2_int


def _oxygen_id(column_lists):
    valid_indices = set(range(len(column_lists[0])))
    for col in column_lists:
        subset = [elem for i, elem in enumerate(col) if i in valid_indices]
        most_common_list = Counter(subset).most_common()

        # check if 1 & 0 are tied for most common
        if most_common_list[0][1] == most_common_list[-1][1]:
            most_common = "1"
        else:
            most_common = most_common_list[0][0]

        for i, elem in enumerate(col):
            if elem != most_common:
                valid_indices.discard(i)

        if len(valid_indices) == 1:
            return valid_indices.pop()


def _co2_id(column_lists):
    valid_indices = set(range(len(column_lists[0])))
    for col in column_lists:
        subset = [elem for i, elem in enumerate(col) if i in valid_indices]
        most_common_list = Counter(subset).most_common()

        # check if 1 & 0 are tied for most common
        if most_common_list[0][1] == most_common_list[-1][1]:
            least_common = "0"
        else:
            least_common = most_common_list[-1][0]

        for i, elem in enumerate(col):
            if elem != least_common:
                valid_indices.discard(i)

        if len(valid_indices) == 1:
            return valid_indices.pop()


if __name__ == "__main__":
    diagnostics = []
    with open("day_3_input.txt") as f:
        for line in f:
            line = line.strip()
            chars = [c for c in line]
            diagnostics.append(chars)

    consumption = power_consumption(diagnostics)
    print(consumption)

    life_support = life_support_rating(diagnostics)
    print(life_support)
