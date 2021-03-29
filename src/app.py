from midi_interface import Listener
from patterns import add_patterns
from integrations import pneumatics


def shutdown():
    """Cleanup scripts"""
    pneumatics.shutdown()


def main():
    """Entrypoint for the application"""
    l = Listener()
    add_patterns(l)
    l.print_notes = False
    l.listen()


if __name__ == '__main__':
    main()
    shutdown()
