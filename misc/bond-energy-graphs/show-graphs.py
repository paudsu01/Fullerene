from __future__ import annotations
from typing import List, Tuple

import argparse
import exceptions
import re
import os

# If I am investigating carbon 'c'
# I need a file for either one of (x,y,z coordinate) and total bond energy for 'c' for that coordinate and pass it as an argument (required)

def plot_graph(x: List[float], y: List[float], initial_x: float, initial_y: float) -> None:
    pass

def process_file(file : str) -> Tuple[float]:

    path = os.path.join(os.path.dirname(__file__), file)
    x_values = []
    y_values = []

    with open(path, 'r') as xf:

        for index, line in enumerate(xf):

            values = line.strip().split()

            if len(values) != 2:
                raise exceptions.TwoColumnsRequiredInDATFile("Two Columns reuqired: First one for coordinate and second one for energy")

            x_value = float(values[0])
            y_value = float(values[1])

            x_values.append(x_value)
            y_values.append(y_value)

            if index == 0:
                initial_x = x_value
                initial_y = y_value

        return x_values, y_values, initial_x, initial_y

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file.dat', help='Provide a file with the 1st column: x coordinate, 2nd column: bond energy')
    args = parser.parse_args()

    pattern = re.compile(r'.*\.dat')
    if pattern.match(vars(args)['file.dat']):
        x_values, y_values, initial_x, initial_y = process_file(vars(args)['file.dat'])
        plot_graph(x_values, y_values, initial_x, initial_y)
    else:
        raise exceptions.DATFileRequired("DAT file required")

