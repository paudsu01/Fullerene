from __future__ import annotations

import config
import vpython

def initialise_buttons() -> None:
    global run_pause_button
    global stop_button
    run_pause_button = vpython.button(text='Run',
                                bind=run_pause_simulation,
                                background=vpython.color.green)

    vpython.scene.append_to_caption("\t\t")

    stop_button = vpython.button(text='Stop simulation',
                                bind=stop_simulation,
                                background=vpython.color.red)

def stop_simulation(evt: vpython.vpython.button)-> None:

    config.SIMULATION_ENDED = True

def run_pause_simulation(event : vpython.vpython.button) -> None:

    config.SIMULATION_PAUSED = False if config.SIMULATION_PAUSED else True
    event.text = 'Run' if config.SIMULATION_PAUSED else 'Pause'
    event.background = vpython.color.green if config.SIMULATION_PAUSED else vpython.color.red

def disable_buttons() -> None:
    run_pause_button.disabled = True
    stop_button.disabled = True

def enable_buttons() -> None:
    run_pause_button.disabled = False
    stop_button.disabled = False
