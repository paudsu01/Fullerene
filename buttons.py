from __future__ import annotations

import config
import vpython

def initialise_buttons() -> None:
    global run_pause_button
    global stop_button
    global speed_slider
    global speed_w_text 

    run_pause_button = vpython.button(text='Run',
                                bind=run_pause_simulation,
                                background=vpython.color.green)

    vpython.scene.append_to_caption("\t\tSpeed: ")

    speed_slider = vpython.slider(bind=change_simulation_rate,
                                  value=config.SIMULATION_RATE,
                                  min=1,
                                  max=40)

    speed_w_text = vpython.wtext(text=config.SIMULATION_RATE)

    vpython.scene.append_to_caption("\n\n")

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
    speed_slider.disabled = True

def enable_buttons() -> None:
    run_pause_button.disabled = False
    stop_button.disabled = False
    speed_slider.disabled = False

def change_simulation_rate(evt : vpython.vpython.slider) -> None:
    config.SIMULATION_RATE = evt.value
    speed_w_text.text = evt.value
