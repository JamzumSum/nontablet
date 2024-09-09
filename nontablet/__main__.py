import argparse
from time import sleep

from pyuac import main_requires_admin

from nontablet import set_tablet_mode


def flip_screen():
    from rotatescreen import get_primary_display

    prim = get_primary_display()
    assert prim
    prim.set_landscape_flipped()


@main_requires_admin
def main():
    set_tablet_mode(disable=True)
    if args.flip:
        sleep(args.delay / 1e3)
        flip_screen()


if __name__ == "__main__":
    psr = argparse.ArgumentParser(description="disable windows tablet mode")
    psr.add_argument(
        "--flip", "-F", action="store_true", help="landscape flip the primary display"
    )
    psr.add_argument(
        "--delay",
        type=float,
        default=1000,
        help="Delay time before flipping the display. Only Take effect if --flip presents.",
    )
    args = psr.parse_args()

    main()
