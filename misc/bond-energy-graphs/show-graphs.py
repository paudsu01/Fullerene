from __future__ import annotations
import argparse
import exceptions
import re
import os

def plot_graph(x, y, initial_x, initial_y):
    pass

def process_file(file):

    path = os.path.join(os.path.dirname(__file__), file)

    with open(path, 'r') as xf:
        pass
        

# If I am investigating carbon 'c'
# I need a file for either one of (x,y,z coordinate) and total bond energy for 'c' for that coordinate and pass it as an argument (required)

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

