"""
testrocket.py

This module defines and simulates a rocket (Polaris 1) using the RocketPy library and specs
from the aae me teams
"""

from rocketpy import Rocket, SolidMotor

test_rocket = Rocket(
    radius=0.04,
    mass=6.658,
    inertia=(2.222, 2.222, 0.00532),
    power_off_drag=0.70,
    power_on_drag="./data/test.csv",
    center_of_mass_without_motor=0.75,
    coordinate_system_orientation="nose_to_tail",
)

test_solid = SolidMotor(
    thrust_source="./data/Loki_L1482-LB.csv",
    dry_mass=1.724,
    dry_inertia=(0.0361, 0.0361, 0.00124),
    nozzle_radius=0.0381,
    grain_number=3,
    grain_density=1660.794,
    grain_outer_radius=35 / 1000,
    grain_initial_inner_radius=0.009525,
    grain_initial_height=0.13335,
    grain_separation=5/1000,
    grains_center_of_mass_position=0.25,
    center_of_dry_mass_position=0.25,
    nozzle_position=0,
    burn_time=2.6,
    throat_radius=0.0381 / 2,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

test_rocket.add_motor(test_solid, position=2)

nose_cone = test_rocket.add_nose(length=0.5, kind="von karman", position=0)

fin_set = test_rocket.add_trapezoidal_fins(
    n=4,
    root_chord=0.17,
    tip_chord=0.08,
    span=0.045,
    position=1.825,
    cant_angle=0,
    sweep_angle=51.2,
    airfoil=None,
)

tail = test_rocket.add_tail(
    top_radius=0.04, bottom_radius=0.0381, length=0.5, position=1.5
)

main = test_rocket.add_parachute(
    name="Main",
    cd_s=10.0,
    trigger=200,
)

drogue = test_rocket.add_parachute(
    name="Drogue",
    cd_s=1.0,
    trigger="apogee",
)

test_rocket.all_info()
