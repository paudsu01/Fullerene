from __future__ import annotations
from typing import List, Tuple
import argparse
import os
import matplotlib.pyplot as plt

"""
the file to be provided as the positional argument needs to have 72180 rows with 2 columns of data in each row

Line 1: Carbon 2: x-coordinate, total-bond-energy
Line 2: Carbon 2: x-coordinate + 0.01, total-bond-energy
..
Line 201: Carbon 2: x-coordinate + 0.01 * 200, total-bond-energy
Line 202: Carbon 2: x-coordinate - 0.01, total-bond-energy
..
Line 401: Carbon 2: x-coordinate - 0.01 * 200, total-bond-energy
Line 402- 803 (Carbon 2 with changing y coordinates)
...
And then for z coordinates and then for other carbon atoms with the same idea

"""

def parse_data(file: str, start: int, end: int) -> Tuple[List]:

    path = os.path.join(os.path.dirname(__file__), file)
    with open(path, 'r') as infile:
        data = infile.readlines()
    necessary_data = list(map(lambda x: list(map(lambda x: float(x), x.split())), data[start:end]))

    return (necessary_data[:401], necessary_data[401:802], necessary_data[802:])

def plot_graphs(*datasets):
    index_to_name_dict = {0: 'X', 1: 'Y', 2:'Z'}

    fig, axs = plt.subplots(3)
    fig.suptitle(f"Carbon: {args.carbon}")

    for index, data in enumerate(datasets):
        x = [i[0] for i in data]
        y = [i[1] for i in data]
        axs[index].plot(x, y, 'ro', markersize=1)
        axs[index].set_xlabel(f"{index_to_name_dict[index]}-coordinate")
        axs[index].set_ylabel("Total Bond energy")
        axs[index].scatter(x[0], y[0])
    plt.tight_layout()
    return fig

def main(carbon: int, file : str) -> None:

    line_numbers = lambda carbon_id : (1203 * (carbon_id-2), 1203 * (carbon_id-1))
    x_data, y_data, z_data = parse_data(file, *line_numbers(carbon))
    fig = plot_graphs(x_data, y_data, z_data)

    fileName = os.path.join(os.path.dirname(__file__), f'images/carbon-{carbon}.png')
    fig.savefig(fileName)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='File with all coordinates and bond energy values')
    parser.add_argument('-c', '--carbon', help='ID of the carbon to look at the graph of')
    args = parser.parse_args()
    main(int(args.carbon), args.file)
