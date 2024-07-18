from __future__ import annotations

from typing import List, Tuple


class Simulation:

    def __init__(self, data: List[str]) -> None:
        self.__time = 0
        self.__process_data(data)

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, value: float) -> None:
        self.__time = value

    @property
    def data(self) -> List:
        return self.__data

    def __process_data(self, raw_data: List) -> None:
        self.__data = []
        for row in raw_data:
            if len(row.strip().split()) == 0: continue
            self.__data.append([float(i) for i in row.strip().split()])

    # simulation[0] gives coordinates of the first carbon atom
    # simulation[1] gives coordinates of the second carbon atom
    def __getitem__(self, index: int) -> Tuple[int]:

        realIndex = index * 3
        row = self.data[self.time]

        if type(index) != int:
            raise TypeError("Integer expected for indexing")

        return (row[realIndex], row[realIndex + 1], row[realIndex + 2])

    @property
    def actual_time(self):
        return self.data[self.time][-1]
