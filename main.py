from __future__ import annotations

import argparse
import os
import random
import re

import vpython

import simulation_model
from exceptions import DATFileRequired


def update_carbon_atoms() -> None:
    for index, carbon in enumerate(ALL_CARBON_VPYTHON_OBJECTS):
        carbon.pos = vpython.vector(*SIMULATION[index])


def initialise_vpython() -> None:
    for i in range(60):
        ALL_CARBON_VPYTHON_OBJECTS.append(
            vpython.sphere(radius=0.1,
                           color=vpython.vector(random.random(),
                                                random.random(),
                                                random.random()),
                           opacity=0.2))
        try:
            ALL_CARBON_VPYTHON_OBJECTS[i].pos = vpython.vector(*SIMULATION[i])
        except IndexError:
            raise IndexError(".DAT file doesn't have 181 columns")

    vpython.scene.title = f'Time = <b>{SIMULATION.actual_time:.4f} femtosecond(s)'
    SIMULATION.time += 1

def run_simulation():

    while True:
        vpython.rate(25)
        update_carbon_atoms()
        vpython.scene.title = f'Time = <b>{SIMULATION.actual_time:.4f} femtosecond(s)'
        SIMULATION.time += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'coordinates.dat',
        help='Provide the .dat file with coordinates data for the carbon atoms'
    )
    args = parser.parse_args()

    fileName = vars(args)['coordinates.dat']
    if not os.path.exists(fileName):
        raise FileNotFoundError("File not found")

    if not re.match(r'.*\.dat', fileName):
        raise DATFileRequired('.dat file required error')

    with open(fileName, 'r') as infile:
        SIMULATION = simulation_model.Simulation(infile.readlines())

    ALL_CARBON_VPYTHON_OBJECTS = []

    initialise_vpython()
    run_simulation()
