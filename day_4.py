import re
from typing import List

import numpy as np


class Bingo:
    def __init__(self, card: np.ndarray):
        self.card = card
        self.mask = np.zeros_like(self.card, dtype=bool)

    def take_turn(self, input_num) -> bool:
        self._mark_card(input_num)
        return self._check_card()

    def _check_card(self) -> bool:
        col_check = np.all(self.mask, axis=0)
        row_check = np.all(self.mask, axis=1)

        return np.any(col_check) or np.any(row_check)

    def _mark_card(self, number):
        for r, c in np.ndindex(self.card.shape):
            if self.card[r, c] == number:
                self.mask[r, c] = True


def calc_score(bingo_card: Bingo, final_number: int):
    unmarked_nums = bingo_card.card.copy()
    unmarked_nums[bingo_card.mask] = 0
    unmarked_sum = np.sum(unmarked_nums)
    return unmarked_sum * final_number


def find_winning_score(turn_inputs, boards):
    bingo_cards = [Bingo(board) for board in boards]

    for turn in turn_inputs:
        for i, card in enumerate(bingo_cards):
            if card.take_turn(turn):
                return calc_score(card, turn)


def find_losing_score(turn_inputs, boards):
    bingo_cards = [Bingo(board) for board in boards]

    for turn in turn_inputs:
        to_remove = []
        for i, card in enumerate(bingo_cards):
            if card.take_turn(turn):
                if len(bingo_cards) - len(to_remove) == 1:
                    return calc_score(card, turn)
                else:
                    to_remove.append(i)

        # popping changes later indices, so pop in reverse order
        for index in sorted(to_remove, reverse=True):
            bingo_cards.pop(index)


def parse_input(data: List[str]):
    turn_inputs = data[0].strip().split(",")
    turn_inputs = [int(turn) for turn in turn_inputs]

    boards = []
    board_buffer = []
    for i in range(2, len(data)):
        line = data[i].strip()
        if not line:
            boards.append(np.array(board_buffer))
            board_buffer = []
        else:
            row = re.split("\s+", line)
            row = [int(elem) for elem in row]
            board_buffer.append(row)

    boards.append(np.array(board_buffer))

    return turn_inputs, boards


if __name__ == "__main__":
    diagnostics = []
    with open("day_4_input.txt") as f:
        data = f.readlines()
    turn_inputs, boards = parse_input(data)

    winning_score = find_winning_score(turn_inputs, boards)
    print(winning_score)

    losing_score = find_losing_score(turn_inputs, boards)
    print(losing_score)
