
from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale", help="Increases Panda size",
                        type = float, default = 1)
    parser.add_argument("--moving", help="Stops panda from walking",
                        action="store_false")
    parser.add_argument("--background", help="Removes the background",
                        action="store_false")
    parser.add_argument("--rotate_speed", help="Changes camera rotate speed",
                        type = float, default = 1)
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()