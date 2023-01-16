from .base import Console

class ConsoleLinux(Console):

    @staticmethod
    def is_cmd(cmd):
        return ConsoleLinux.run_cmd(['which', cmd]) != f"{cmd} not found"