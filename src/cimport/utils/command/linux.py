from .base import Console

class ConsoleLinux(Console):

    def is_cmd(self, cmd):
        """
            is_cmd implementation for linux
        """
        return self.run_cmd(['which', cmd]) != f"{cmd} not found"