import argh
from argh.decorators import arg

from z.cli import cmd, load, dump


def l():
    p = argh.ArghParser()
    argh.set_default_command(p, load)
    p.dispatch()


def d():
    p = argh.ArghParser()
    argh.set_default_command(p, dump)
    p.dispatch()


def main():
    p = argh.ArghParser()
    p.add_commands([cmd, load, dump])
    p.dispatch()


if __name__ == '__main__':
    main()

