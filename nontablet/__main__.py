import argparse

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
        flip_screen()


if __name__ == "__main__":
    psr = argparse.ArgumentParser(description="disable windows tablet mode")
    psr.add_argument(
        "--flip", "-F", action="store_true", help="landscape flip the primary display"
    )
    args = psr.parse_args()

    main()
