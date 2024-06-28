from __future__ import annotations

import argparse
import os
import random
import re

import vpython
import config
import buttons

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
                           opacity=1))
        try:
            ALL_CARBON_VPYTHON_OBJECTS[i].pos = vpython.vector(*SIMULATION[i])
        except IndexError:
            raise IndexError(".DAT file doesn't have 181 columns")

    buttons.initialise_buttons()

    vpython.scene.title = f'Trajectory= <b>1</b>\tTime = <b>{SIMULATION.actual_time:.4f} femtosecond(s)</b>'

def end_simulation() -> None:

    config.SIMULATION_ENDED = True
    buttons.disable_buttons()
    show_restart_button()

def restart_simulation(evt: vpython.vpython.button)-> None:

    # Delete restart button
    evt.delete()

    # Reset simulation time to 0
    SIMULATION.time = 0

    buttons.enable_buttons()
    vpython.scene.title = f'Trajectory= <b>1</b>\tTime = <b>{SIMULATION.actual_time:.4f} femtosecond(s)</b>'
    update_carbon_atoms()

    # Pause the simulation at the beginning
    config.SIMULATION_PAUSED = False
    buttons.run_pause_simulation(buttons.run_pause_button)

    # Allow the start_simulation function to be executed
    config.SIMULATION_ENDED = False


def show_restart_button():
    
    vpython.button(bind=restart_simulation,
                   text='Restart simulation',
                   background=vpython.color.magenta,
                   pos=vpython.scene.title_anchor)

def run_simulation() -> None:

    current_trajectory = 1
    previous_time = SIMULATION.actual_time

    while SIMULATION.time < len(SIMULATION.data) and not config.SIMULATION_ENDED:
        vpython.rate(20)

        if not config.SIMULATION_PAUSED:
            # Determine if we are in a new trajectory
            if SIMULATION.actual_time < previous_time:
                current_trajectory += 1

            update_carbon_atoms()
            vpython.scene.title = f'Trajectory= <b>{current_trajectory}</b>\tTime = <b>{SIMULATION.actual_time:.4f} femtosecond(s)</b>'

            previous_time = SIMULATION.actual_time
            SIMULATION.time += 1

    end_simulation()

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

    ## KEEP THIS LOOP RUNNING FOR VPYTHON TO BE RESPONSIVE EVEN AFTER SIMULATION ENDS ##
    while True:
        vpython.rate(5)
        if not config.SIMULATION_ENDED:
            run_simulation()
