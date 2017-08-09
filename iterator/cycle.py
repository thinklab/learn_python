#!/usr/bin/env python3
from itertools import cycle
import operator


def my_cycle(seq, counter=None):
    return MyCyclePseudoContainer(seq, counter)


class MyCyclePseudoContainer:
    def __init__(self, seq, counter):
        self.seq = seq
        self.counter = counter

    def __iter__(self):
        return MyCycleIterator(self.seq, self.counter)


class MyCycleIterator:
    def __init__(self, seq, counter):
        # истощить и запомнить в лист
        self.seq = list(seq)
        self.next_lap = 0
        self.next_pos = 0
        self.n_laps = counter

    def __next__(self):
        if self.next_lap == self.n_laps or self.seq == []:
            raise StopIteration()
        ret = self.seq[self.next_pos]
        self.next_pos += 1
        if self.next_pos == len(self.seq):
            self.next_pos = 0
            self.next_lap += 1
        return ret


if __name__ == '__main__':
    print([] * 3)
    print(list(my_cycle([], 3)))
