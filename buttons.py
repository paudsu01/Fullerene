from __future__ import annotations

import config
import vpython

def initialise_buttons():
    global stop_button
    stop_button = vpython.button(text='Run',
                                bind=run_pause_simulation,
                                background=vpython.color.green)

def run_pause_simulation(event):

    config.SIMULATION_PAUSED = False if config.SIMULATION_PAUSED else True
    event.text = 'Run' if config.SIMULATION_PAUSED else 'Pause'
    event.background = vpython.color.green if config.SIMULATION_PAUSED else vpython.color.red

def disable_buttons():
    stop_button.disabled = True

